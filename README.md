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

# Selected source for each target under CDA, Random, MMD, CD, and KL.

| Target                | CDA                 | Random               | MMD                  | CS                   | KL                   |
|-----------------------|---------------------|----------------------|----------------------|----------------------|----------------------|
| Apache                | Zxing               | Safe                 | Zxing                | Safe                 | Safe                 |
| Safe                  | Apache              | Zxing                | Zxing                | Apache               | Zxing                |
| Zxing                 | Apache              | Safe                 | Apache               | Apache               | Safe                 |
| equinox               | pde                 | mylyn                | lucene               | lucene               | pde                  |
| jdt                   | pde                 | lucene               | lucene               | lucene               | mylyn                |
| lucene                | pde                 | equinox              | equinox              | jdt                  | pde                  |
| mylyn                 | pde                 | equinox              | jdt                  | jdt                  | jdt                  |
| pde                   | equinox             | mylyn                | equinox              | lucene               | equinox              |
| activemq-5            | wicket-1            | groovy-1_6_BETA_1    | wicket-1             | hive-0               | wicket-1             |
| derby-10              | hive-0              | hbase-0              | jruby-1              | wicket-1             | groovy-1_6_BETA_1    |
| groovy-1_6_BETA_1     | jruby-1             | derby-10             | hive-0               | jruby-1              | derby-10             |
| hbase-0               | hive-0              | wicket-1             | hive-0               | jruby-1              | wicket-1             |
| hive-0                | hbase-0             | activemq-5           | hbase-0              | groovy-1_6_BETA_1    | hbase-0              |
| jruby-1               | groovy-1_6_BETA_1   | derby-10             | activemq-5           | groovy-1_6_BETA_1    | wicket-1             |
| wicket-1              | activemq-5          | groovy-1_6_BETA_1    | groovy-1_6_BETA_1    | hbase-0              | activemq             |
| ant-1                 | xalan-2             | synapse-1            | log4j-1              | log4j-1              | log4j-1              |
| ivy-2                 | xalan-2             | ant-1                | jedit-4              | synapse-1            | synapse-1            |
| jedit-4               | xalan-2             | ant-1                | xalan-2              | synapse-1            | log4j-1              |
| log4j-1               | ant-1               | synapse-1            | ivy-2                | ant-1                | ant-1                |
| synapse-1             | ant-1               | ivy-2                | ivy-2                | log4j-1              | xalan-2              |
| tomcat                | xalan-2             | ant-1                | jedit-4              | ivy-2                | xalan-2              |
| xalan-2               | jedit-4             | tomcat               | jedit-4              | jedit-4              | synapse-1            |
