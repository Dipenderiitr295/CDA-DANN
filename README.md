# CDA-DANN
# Details of Datasets
1 ReLink dataset :"Wu, Rongxin, et al. "Relink: recovering links between bugs and changes." Proceedings of the 19th ACM SIGSOFT symposium and the 13th European conference on Foundations of software engineering. 2011".


2 AEEEM dataset :"D’Ambros, Marco, Michele Lanza, and Romain Robbes. "Evaluating defect prediction approaches: a benchmark and an extensive comparison." Empirical Software Engineering 17 (2012): 531-577".


3 JIRA dataset :"Yatish, Suraj, et al. "Mining software defects: Should we consider affected releases?." 2019 IEEE/ACM 41st international conference on software engineering (ICSE). IEEE, 2019".

4 T. Menzies, R. Krishna, and D. Pryor, “The promise repository of empirical software engineering data (2015),” URL http://promisedata.googlecode. com, 2015.

# Metrics Details of ReLink Dataset
| **Abbreviation**      | **Description**                                                |
| --------------------- | -------------------------------------------------------------- |
| AvgCyclomatic         | Average Cyclomatic Complexity                                  |
| AvgCyclomaticModified | Average Modified Cyclomatic Complexity                         |
| AvgCyclomaticStrict   | Average Strict Cyclomatic Complexity                           |
| AvgEssential          | Average Essential Complexity                                   |
| AvgLine               | Average Lines                                                  |
| AvgLineBlank          | Average Blank Lines                                            |
| AvgLineCode           | Average Code Lines                                             |
| AvgLineComment        | Average Comment Lines                                          |
| CountLine             | Number of Lines                                                |
| CountLineBlank        | Number of Blank Lines                                          |
| CountLineCode         | Number of Code Lines                                           |
| CountLineCodeDecl     | Number of Declarative Code Lines                               |
| CountLineCodeExe      | Number of Executable Code Lines                                |
| CountLineComment      | Number of Comment Lines                                        |
| CountSemicolon        | Number of Semicolons                                           |
| CountStmt             | Number of Statements                                           |
| CountStmtDecl         | Number of Declarative Statements                               |
| CountStmtExe          | Number of Executive Statements                                 |
| MaxCyclomatic         | Maximum Cyclomatic Complexity of all nested functions          |
| MaxCyclomaticModified | Maximum Modified Cyclomatic Complexity of all nested functions |
| MaxCyclomaticStrict   | Maximum Strict Cyclomatic Complexity of all nested functions   |
| RatioCommentToCode    | Ratio of Comment Lines to Code Lines                           |
| SumCyclomatic         | Sum of Cyclomatic Complexity of all nested functions           |
| SumCyclomaticModified | Sum of Modified Cyclomatic Complexity of all nested functions  |
| SumCyclomaticStrict   | Sum of Strict Cyclomatic Complexity of all nested functions    |
| SumEssential          | Sum of Essential Complexity of all nested functions            |

# Metrics Details of AEEEM Dataset
| **Abbreviation**                   | **Description**                                                                    |
| ---------------------------------- | ---------------------------------------------------------------------------------- |
| ck\_oo\_wmc                        | Weighted method count                                                              |
| ck\_oo\_dit                        | Depth of inheritance tree                                                          |
| ck\_oo\_rfc                        | Response for class                                                                 |
| ck\_oo\_noc                        | Number of children                                                                 |
| ck\_oo\_cbo                        | Coupling between objects                                                           |
| ck\_oo\_lcom                       | Lack of cohesion in methods                                                        |
| ck\_oo\_fanin                      | Number of other classes that reference the class                                   |
| ck\_oo\_fanout                     | Number of other classes referenced by the class                                    |
| ck\_oo\_noa                        | Number of attributes                                                               |
| ck\_oo\_nopa                       | Number of public attributes                                                        |
| ck\_oo\_nopra                      | Number of private attributes                                                       |
| ck\_oo\_noai                       | Number of attributes inherited                                                     |
| ck\_oo\_loc                        | Number of lines of code                                                            |
| ck\_oo\_nom                        | Number of methods                                                                  |
| ck\_oo\_nopm                       | Number of public methods                                                           |
| ck\_oo\_noprm                      | Number of private methods                                                          |
| ck\_oo\_nomt                       | Number of methods inherited                                                        |
| WCHU\_wmc                          | Weighted churn of weighted method count                                            |
| WCHU\_dit                          | Weighted churn of depth of inheritance tree                                        |
| WCHU\_rfc                          | Weighted churn of response for class                                               |
| WCHU\_noc                          | Weighted churn of number of children                                               |
| WCHU\_cbo                          | Weighted churn of coupling between objects                                         |
| WCHU\_lcom                         | Weighted churn of lack of cohesion in methods                                      |
| WCHU\_fanin                        | Weighted churn of number of other classes that reference the class                 |
| WCHU\_fanout                       | Weighted churn of number of other classes referenced by the class                  |
| WCHU\_noa                          | Weighted churn of number of attributes                                             |
| WCHU\_nopa                         | Weighted churn of number of public attributes                                      |
| WCHU\_nopra                        | Weighted churn of number of private attributes                                     |
| WCHU\_noai                         | Weighted churn of number of attributes inherited                                   |
| WCHU\_loc                          | Weighted churn of number of lines of code                                          |
| WCHU\_nom                          | Weighted churn of number of methods                                                |
| WCHU\_nopm                         | Weighted churn of number of public methods                                         |
| WCHU\_noprm                        | Weighted churn of number of private methods                                        |
| WCHU\_nomt                         | Weighted churn of number of methods inherited                                      |
| LDHH\_wmc                          | Linear decayed history entropy of weighted method count                            |
| LDHH\_dit                          | Linear decayed history entropy of depth of inheritance tree                        |
| LDHH\_rfc                          | Linear decayed history entropy of response for class                               |
| LDHH\_noc                          | Linear decayed history entropy of number of children                               |
| LDHH\_cbo                          | Linear decayed history entropy of coupling between objects                         |
| LDHH\_lcom                         | Linear decayed history entropy of lack of cohesion in methods                      |
| LDHH\_fanin                        | Linear decayed history entropy of number of other classes that reference the class |
| LDHH\_fanout                       | Linear decayed history entropy of number of other classes referenced by the class  |
| LDHH\_noa                          | Linear decayed history entropy of number of attributes                             |
| LDHH\_nopa                         | Linear decayed history entropy of number of public attributes                      |
| LDHH\_nopra                        | Linear decayed history entropy of number of private attributes                     |
| LDHH\_noai                         | Linear decayed history entropy of number of attributes inherited                   |
| LDHH\_loc                          | Linear decayed history entropy of number of lines of code                          |
| LDHH\_nom                          | Linear decayed history entropy of number of methods                                |
| LDHH\_nopm                         | Linear decayed history entropy of number of public methods                         |
| LDHH\_noprm                        | Linear decayed history entropy of number of private methods                        |
| LDHH\_nomt                         | Linear decayed history entropy of number of methods inherited                      |
| CvsEntropy                         | Entropy of CVS change log                                                          |
| CvsWEntropy                        | Weighted Entropy of CVS change log                                                 |
| CvsLogEntropy                      | Logarithmic Entropy of CVS change log                                              |
| CvsExpEntropy                      | Exponential Entropy of CVS change log                                              |
| CvsLinEntropy                      | Linear Entropy of CVS change log                                                   |
| numberOfNonTrivialBugsFoundUntil   | Number of non-trivial bugs found until the corresponding fix                       |
| numberOfCriticalBugsFoundUntil     | Number of critical bugs found until the corresponding fix                          |
| numberOfHighPriorityBugsFoundUntil | Number of high priority bugs found until the corresponding fix                     |
| numberOfMajorBugsFoundUntil        | Number of major bugs found until the corresponding fix                             |
| numberOfBugsFoundUntil             | Number of bugs found until the corresponding fix                                   |

# Metrics Details of JIRA Dataset
| **Abbreviation**          | **Description**                                                            |
| ------------------------- | -------------------------------------------------------------------------- |
| AvgCyclomatic             | Average cyclomatic complexity for all nested functions or methods          |
| SumCyclomatic             | Sum of cyclomatic complexity of all nested functions or methods            |
| AvgCyclomaticModified     | Average modified cyclomatic complexity for all nested functions or methods |
| SumCyclomaticModified     | Sum of modified cyclomatic complexity of all nested functions              |
| AvgCyclomaticStrict       | Average strict cyclomatic complexity for all nested functions or methods   |
| SumCyclomaticStrict       | Sum of strict cyclomatic complexity of all nested functions or methods     |
| AvgEssential              | Average essential complexity for all nested functions or methods           |
| SumEssential              | Sum of essential complexity of all nested functions or methods             |
| AvgLine                   | Average number of lines for all nested functions or methods                |
| AvgLineBlank              | Average number of blank lines for all nested functions or methods          |
| AvgLineCode               | Average number of lines containing source code for all nested functions    |
| AvgLineComment            | Average number of comment lines for all nested functions or methods        |
| CountClassBase            | Number of immediate base classes                                           |
| CountClassCoupled         | Number of other classes coupled to                                         |
| CountClassDerived         | Number of immediate subclasses                                             |
| MaxInheritanceTree        | Maximum depth of class in inheritance tree                                 |
| PercentLackOfCohesion     | 100% minus the average cohesion for package entities                       |
| CountDeclClass            | Number of classes                                                          |
| CountDeclClassMethod      | Number of class methods                                                    |
| CountDeclClassVariable    | Number of class variables                                                  |
| CountDeclFunction         | Number of functions                                                        |
| CountDeclInstanceMethod   | Number of instance methods                                                 |
| CountDeclInstanceVariable | Number of instance variables                                               |
| CountDeclMethod           | Number of local (non-inherited) methods                                    |
| CountDeclMethodDefault    | Number of local default methods                                            |
| CountDeclMethodPrivate    | Number of local (non-inherited) private methods                            |
| CountDeclMethodProtected  | Number of local protected methods                                          |
| CountDeclMethodPublic     | Number of local (non-inherited) public methods                             |
| CountLine                 | Number of physical lines                                                   |
| CountLineBlank            | Number of blank lines                                                      |
| CountLineCode             | Number of lines containing source code                                     |
| CountLineCodeDecl         | Number of lines containing declarative source code                         |
| CountLineCodeExe          | Number of lines containing executable source code                          |
| CountLineComment          | Number of lines containing comment                                         |
| CountSemicolon            | Number of semicolons                                                       |
| CountStmt                 | Number of statements                                                       |
| CountStmtDecl             | Number of declarative statements                                           |
| CountStmtExe              | Number of executable statements                                            |
| MaxCyclomatic             | Maximum cyclomatic complexity of all nested functions or methods           |
| MaxCyclomaticModified     | Maximum modified cyclomatic complexity of nested functions or methods      |
| MaxCyclomaticStrict       | Maximum strict cyclomatic complexity of nested functions or methods        |
| RatioCommentToCode        | Ratio of comment lines to code lines                                       |
| CountInput\_Min           | Min number of calling subprograms plus global variables read               |
| CountInput\_Mean          | Mean number of calling subprograms plus global variables read              |
| CountInput\_Max           | Max number of calling subprograms plus global variables read               |
| CountOutput\_Min          | Min number of called subprograms plus global variables set                 |
| CountOutput\_Mean         | Mean number of called subprograms plus global variables set                |
| CountOutput\_Max          | Max number of called subprograms plus global variables set                 |
| CountPath\_Min            | Min number of unique paths through a body of code                          |
| CountPath\_Mean           | Mean number of unique paths through a body of code                         |
| CountPath\_Max            | Max number of unique paths through a body of code                          |
| MaxNesting\_Min           | Min of maximum nesting level of control constructs in the function         |
| MaxNesting\_Mean          | Mean of maximum nesting level of control constructs in the function        |
| MaxNesting\_Max           | Max of maximum nesting level of control constructs in the function         |
| COMM                      | Number of Git commits                                                      |
| ADDED\_LINES              | Normalized number of lines added to the module                             |
| DEL\_LINES                | Normalized number of lines deleted from the module                         |
| ADEV                      | Number of active developers                                                |
| DDEV                      | Number of distinct developers                                              |
| MINOR\_COMMIT             | Developers contributing <5% of total code changes                          |
| MINOR\_LINE               | Developers contributing <5% of total LOC                                   |
| MAJOR\_COMMIT             | Developers contributing >5% of total code changes                          |
| MAJOR\_LINES              | Developers contributing >5% of total LOC                                   |
| OWN\_COMMIT               | Proportion of code changes by top contributor                              |
| OWN\_LINE                 | Proportion of lines of code by top contributor                             |

# Metrics Details of PROMISE Dataset
| **Abbreviation** | **Description** |
|------------------|-----------------|
| WMC              | Weighted Methods per Class |
| DIT              | Depth of Inheritance Tree |
| NOC              | Number of Children |
| CBO              | Coupling Between Object Classes |
| RFC              | Response for a Class |
| LCOM             | Lack of Cohesion in Methods |
| CA               | Afferent Couplings |
| CE               | Efferent Couplings |
| NPM              | Number of Public Methods |
| LCOM3            | Lack of Cohesion in Methods (variant of LCOM) |
| LOC              | Lines of Code |
| DAM              | Data Access Metric |
| MOA              | Measure of Aggregation |
| MFA              | Measure of Functional Abstraction |
| CAM              | Cohesion Among Methods of a Class |
| IC               | Inheritance Coupling |
| CBM              | Coupling Between Methods |
| AMC              | Average Method Complexity |
| CC               | McCabe’s Cyclomatic Complexity |
| MAX_CC           | Maximum Value of CC Among Methods in the Class |
| AVG_CC           | Average (Arithmetic Mean) CC of Methods in the Class |

# Selected Source project for each Target Project under CDA, Random, MMD, CS, and KL.

| Target                | CDA            | Random         | MMD               | Chi-square         | KL             |
|-----------------------|----------------|----------------|--------------------|---------------------|----------------|
| Apache                | Zxing          | Safe           | Zxing              | Safe                | Safe           |
| Safe                  | Apache         | Zxing          | Zxing              | Apache              | Zxing          |
| Zxing                 | Apache         | Safe           | Apache             | Apache              | Safe           |
| equinox               | pde            | mylyn          | lucene             | lucene              | pde            |
| jdt                   | pde            | mylyn          | lucene             | lucene              | mylyn          |
| lucene                | pde            | mylyn          | jdt                | equinox             | pde            |
| mylyn                 | pde            | equinox        | jdt                | jdt                 | jdt            |
| pde                   | equinox        | mylyn          | equinox            | lucene              | equinox        |
| activemq-5.8.0    | wicket-1       | hive-0         | derby-10           | jruby-1             | derby-10       |
| derby-10.5.1.1   | jruby-1        | wicket-1       | groovy-1_6_BETA_2  | hbase-0             | activemq-5     |
| groovy-1_6_BETA_2 | wicket-1       | jruby          | hbase-0            | hbase-0             | derby-10       |
| hbase-0.95.2     | hive-0         | groovy-1_6_BETA_2 | hive-0          | groovy-1_6_BETA_2   | hive-0         |
| hive-0.12.0       | hbase-0        | wicket-1       | hbase-0            | jruby-1             | activemq-5     |
| jruby-1.7.0.preview1 | groovy-1_6_BETA_2 | hbase-0   | groovy-1_6_BETA_2  | groovy-1_6_BETA_2   | hbase-0        |
| wicket-1.5.3      | jruby-1        | hive-0         | derby-10           | hbase-0             | activemq-5     |
| ant-1.7          | camel-1        | camel-1        | camel-1            | jedit-4             | camel-1        |
| camel-1.6         | ant-1          | jedit-4        | ant-1              | jedit-4             | ant-1          |
| jedit-4.3         | ant-1          | camel-1        | velocity-1         | velocity-1          | camel-1        |
| prop-2           | ant-1          | jedit-4        | velocity-1         | xalan-2             | xalan-2        |
| velocity-1.6      | ant-1          | xerces-1       | camel-1            | xerces-1            | jedit-4        |
| xalan-2.7        | ant-1          | jedit-4        | camel-1            | jedit-4             | jedit-4        |
| xerces-1.4        | ant-1          | jedit-4        | velocity-1         | velocity-1          | jedit-4        |


## F1 Scores Comparison of CDA-DANN with state of art CPDP Methods

| Target                    | CDA-DANN  | MASTER | CFPS | BurakMHD | ARRAY | SSE  |
|---------------------------|------|--------|------|----------|-------|------|
| Apache                   | 0.70 | 0.73   | 0.71 | 0.69     | 0.73  | 0.67 |
| Safe                     | 0.73 | 0.65   | 0.31 | 0.66     | 0.65  | 0.68 |
| Zxing                    | 0.52 | 0.34   | 0.25 | 0.30     | 0.27  | 0.21 |
| equinox                  | 0.71 | 0.71   | 0.26 | 0.69     | 0.66  | 0.50 |
| jdt                      | 0.59 | 0.39   | 0.46 | 0.46     | 0.45  | 0.42 |
| lucene                   | 0.39 | 0.37   | 0.22 | 0.27     | 0.29  | 0.33 |
| mylyn                    | 0.57 | 0.33   | 0.68 | 0.62     | 0.30  | 0.37 |
| pde                      | 0.35 | 0.35   | 0.24 | 0.32     | 0.34  | 0.30 |
| activemq-5.8.0.csv       | 0.25 | 0.27   | 0.38 | 0.20     | 0.21  | 0.32 |
| derby-10.5.1.1.csv       | 0.41 | 0.43   | 0.41 | 0.22     | 0.35  | 0.39 |
| groovy-1_6_BETA_2.csv    | 0.24 | 0.26   | 0.43 | 0.22     | 0.23  | 0.26 |
| hbase-0.95.2.csv         | 0.54 | 0.52   | 0.49 | 0.02     | 0.50  | 0.48 |
| hive-0.12.0.csv          | 0.25 | 0.23   | 0.18 | 0.04     | 0.21  | 0.17 |
| jruby-1.7.0.preview1.csv | 0.21 | 0.23   | 0.18 | 0.21     | 0.17  | 0.16 |
| wicket-1.5.3.csv         | 0.18 | 0.25   | 0.22 | 0.18     | 0.14  | 0.17 |
| ant-1.7.csv              | 0.48 | 0.49   | 0.43 | 0.52     | 0.47  | 0.38 |
| camel-1.6.csv            | 0.38 | 0.35   | 0.29 | 0.17     | 0.35  | 0.26 |
| jedit-4.3.csv            | 0.09 | 0.04   | 0.08 | 0.15     | 0.05  | 0.16 |
| prop-2.csv               | 0.27 | 0.25   | 0.22 | 0.01     | 0.21  | 0.23 |
| velocity-1.6.csv         | 0.60 | 0.56   | 0.37 | 0.27     | 0.49  | 0.44 |
| xalan-2.7.csv            | 0.71 | 0.54   | 0.48 | 0.42     | 0.73  | 0.65 |
| xerces-1.4.csv           | 0.66 | 0.45   | 0.36 | 0.36     | 0.55  | 0.58 |
| **Average**              | 0.45 | 0.40   | 0.35 | 0.32     | 0.38  | 0.37 |
