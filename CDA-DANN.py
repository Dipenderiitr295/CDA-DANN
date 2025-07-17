import os
import glob
import yaml
import pandas as pd
import numpy as np
from imblearn.over_sampling import SMOTE  
from scipy.stats import ks_2samp
from sklearn.preprocessing import StandardScaler,MinMaxScaler
from torch.utils.data import TensorDataset, DataLoader
import torch.nn as nn

def read_data(file_path: str, delimiters=None) -> pd.DataFrame:
    if delimiters is None:
        delimiters = [',', ';', r'\s+']
    for d in delimiters:
        try:
            if d == r'\s+':
                df = pd.read_csv(file_path, delim_whitespace=True, engine='python')
            else:
                df = pd.read_csv(file_path, sep=d, engine='python')
            # optionally: label‑encode categorical cols here
            return df
        except Exception:
            continue
    return pd.DataFrame()

def preprocess(df: pd.DataFrame, label_col: str) -> pd.DataFrame:
    """
    Binarize `label_col`, drop non‑numeric columns, and drop NA.
    """
    if label_col not in df:
        return pd.DataFrame()
    # binarize; e.g. df[label_col] = (df[label_col] > 0).astype(int)
    # drop non‑numeric columns
    return df.select_dtypes(include=[np.number]).dropna()

def normalize(df: pd.DataFrame, label_col: str):
    y = df[label_col].values
    X = df.drop(columns=[label_col]).values
    scaler = StandardScaler().fit(X)
    Xs = scaler.transform(X)
    norm_df = pd.DataFrame(Xs, columns=df.columns.drop(label_col))
    norm_df[label_col] = y
    return norm_df, scaler

def balance_and_normalize(df: pd.DataFrame, label_col: str, sampler=None):
    if sampler is None:
        sampler = SMOTE()  # or pass in from config
    X = df.drop(columns=[label_col]).values
    y = df[label_col].values
    X_res, y_res = sampler.fit_resample(X, y)
    df_res = pd.DataFrame(X_res, columns=df.columns.drop(label_col))
    df_res[label_col] = y_res
    return normalize(df_res, label_col)[0]
def compute_similarity(src: pd.DataFrame, tgt: pd.DataFrame) -> float:
    """
    Composite score combining:
      1. Frobenius norm between correlation matrices.
      2. Mean KS‑statistic across shared features.
    """
    common = src.columns.intersection(tgt.columns).drop('label')
    C_src = src[common].corr().fillna(0).values
    C_tgt = tgt[common].corr().fillna(0).values
    corr_dist = np.linalg.norm(C_src - C_tgt, ord='fro')
    ks_vals = [ks_2samp(src[c], tgt[c]).statistic for c in common]
    ks_mean = float(np.mean(ks_vals)) if ks_vals else 0.0
    return corr_dist,ks_mean
    
class GradientReversal(Function):
    @staticmethod
    def forward(ctx, x, lambd):
        ctx.lambd = lambd
        return x.view_as(x)
    @staticmethod
    def backward(ctx, grad):
        return -ctx.lambd * grad, None

def grad_reverse(x, lambd=1.0):
    return GradientReversal.apply(x, lambd)

class DANN(nn.Module):
    def __init__(self, input_dim, feature_dim, hidden_dim, dropout_rate):
        super().__init__()
        self.feature = nn.Sequential()
        self.label = nn.Sequential()
        self.domain = nn.Sequential()
        pass

    def forward(self, x, lambd=0.0):
        feats = self.feature(x)
        y_out = self.label(feats)
        d_out = self.domain(grad_reverse(feats, lambd))
        return y_out, d_out
        pass

def train_dann(model, src_loader, tgt_loader, cfg):
    optimizer = optim.Adam(model.parameters(), lr=cfg['lr'])
    criterion = nn.BCELoss()
    return model

def predict_dann(model, X, device='cpu'):
    """
    Return (binary_preds, probabilities).
    """
    model.eval()
    return np.array([]), np.array([])
    
def main(config_path: str):
    cfg = load_config(config_path)
    data_dir = cfg['data_folder']
    label_col = cfg['label_column']

    files = glob.glob(os.path.join(data_dir, '*.csv'))
    results = []

    for tgt_fp in files:
        df_raw = read_data(tgt_fp)
        df_tgt = preprocess(df_raw, label_col)
        if df_tgt.empty:
            continue

        df_tgt_norm, _ = normalize(df_tgt, label_col)

        # find best source
        best_score, best_src = float('inf'), None
        for src_fp in files:
            if src_fp == tgt_fp:
                continue
            df_src_raw = read_data(src_fp)
            df_src = preprocess(df_src_raw, label_col)
            if df_src.empty:
                continue
            df_src_bal = balance_and_normalize(df_src, label_col, sampler=SMOTE())
            scoreFN, scoreKS = compute_similarity(df_src_bal, df_tgt_norm)
            # Normalize FN scores and KS scores using MinMax individually
            score=alpha*FN+(1-alpha)*KS
            if score < best_score:
                best_score, best_src = score, src_fp

        if best_src is None:
            continue
            
        X_src, y_src = df_src_bal.drop(columns=[label_col]).values, df_src_bal[label_col].values
        X_tgt, y_tgt = df_tgt_norm.drop(columns=[label_col]).values, df_tgt_norm[label_col].values
        src_loader = DataLoader(TensorDataset(torch.tensor(X_src, dtype=torch.float32),
                                             torch.tensor(y_src, dtype=torch.float32).unsqueeze(1)),
                                batch_size=cfg['batch_size'], shuffle=True)
        tgt_loader = DataLoader(TensorDataset(torch.tensor(X_tgt, dtype=torch.float32),
                                             torch.zeros((len(X_tgt),1))),
                                batch_size=cfg['batch_size'], shuffle=True)

        # initialize & train DANN
        model = DANN(input_dim=X_src.shape[1],
                     feature_dim=cfg['feature_dim'],
                     hidden_dim=cfg['hidden_dim'],
                     dropout_rate=cfg['dropout'])
        model = train_dann(model, src_loader, tgt_loader, cfg)
        preds, probs = predict_dann(model, X_tgt)
        # record metrics in `results`

    # finally, save `results` to CSV or JSON

if __name__ == "__main__":
