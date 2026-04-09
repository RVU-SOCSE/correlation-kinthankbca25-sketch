Python 3.13.12 (tags/v3.13.12:1cbe481, Feb  3 2026, 18:22:25) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.

============================================================================ RESTART: C:/Users/kinth/py13.py ===========================================================================
Employee Details:
   EmployeeID     Name   Department
0         101    Alice           HR
1         102      Bob  Engineering
2         103  Charlie  Engineering
3         104    David           HR
4         105      Eva    Marketing

Employee Salaries:
   EmployeeID  Salary
0         101   50000
1         102   70000
2         103   80000
3         104   55000
4         105   60000

Sales Region 1:
        Date Region  Sales
0 2024-01-01  North    250
1 2024-01-02  North    300
2 2024-01-03  North    200
3 2024-01-04  North    400
4 2024-01-05  North    350

Sales Region 2:
        Date Region  Sales
0 2024-01-01  South    300
1 2024-01-02  South    320
2 2024-01-03  South    280
3 2024-01-04  South    360
4 2024-01-05  South    310

Average Salary per Department:
Department
Engineering    75000.0
HR             52500.0
Marketing      60000.0
Name: Salary, dtype: float64

Merged Employee Data:
   EmployeeID     Name   Department  Salary
0         101    Alice           HR   50000
1         102      Bob  Engineering   70000
2         103  Charlie  Engineering   80000
3         104    David           HR   55000
4         105      Eva    Marketing   60000
Stock Prices Data:
            Price
Date             
2024-01-01    150
2024-01-02    155
2024-01-03    152
2024-01-04    158
2024-01-05    160

Market Volume Data:
            Volume
Date              
2024-01-01    1000
2024-01-02    1100
2024-01-03    1050
2024-01-04    1150
2024-01-05    1200

Joined Stock Prices and Market Volume Data:
            Price  Volume
Date                     
2024-01-01    150    1000
2024-01-02    155    1100
2024-01-03    152    1050
2024-01-04    158    1150
2024-01-05    160    1200

Consolidated Sales Data:
        Date Region  Sales
0 2024-01-01  North    250
1 2024-01-02  North    300
2 2024-01-03  North    200
3 2024-01-04  North    400
4 2024-01-05  North    350
0 2024-01-01  South    300
1 2024-01-02  South    320
2 2024-01-03  South    280
3 2024-01-04  South    360
4 2024-01-05  South    310
>>> 
=========================================================================== RESTART: C:/Users/kinth/py14a.py ===========================================================================

=========================================================================== RESTART: C:/Users/kinth/py14b.py ===========================================================================
>>> 
============================================================================ RESTART: C:/Users/kinth/py15.py ===========================================================================
Traceback (most recent call last):
  File "C:/Users/kinth/py15.py", line 5, in <module>
    sns.heatmo(df.corr(numeric_only=True),annot=True)
AttributeError: module 'seaborn' has no attribute 'heatmo'. Did you mean: 'heatmap'?
>>> 
============================================================================ RESTART: C:/Users/kinth/py15.py ===========================================================================
Traceback (most recent call last):
  File "C:/Users/kinth/py15.py", line 5, in <module>
    sns.heatmap(df.corr(numeric_only=True),annot=True)
NameError: name 'df' is not defined. Did you mean: 'df2'?
>>> 
============================================================================ RESTART: C:/Users/kinth/py15.py ===========================================================================
>>> import pandas as pd
>>> import matplotlib.pyplot as plt
>>> import seaborn as sns
>>> df2 = pd.read_csv(r"C:/Users/kinth/OneDrive/Scans/laptop.csv")
>>> sns.heatmap(df2.corr(numeric_only=True),annot=True)
<Axes: >
>>> 
>>> plt.show()
