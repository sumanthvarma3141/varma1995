Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:54:40) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
>>> import numpy as np
>>> s = pd.Series([1,3,5,np.nan,6,8])
>>> s
0    1.0
1    3.0
2    5.0
3    NaN
4    6.0
5    8.0
dtype: float64
>>> dates = pd.date_range('20130101', periods=6)
>>> dates
DatetimeIndex(['2013-01-01', '2013-01-02', '2013-01-03', '2013-01-04',
               '2013-01-05', '2013-01-06'],
              dtype='datetime64[ns]', freq='D')
>>> df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
>>> df
                   A         B         C         D
2013-01-01 -0.411172  1.050868  0.218198  0.927397
2013-01-02  0.349921 -1.254727 -1.101459  1.290130
2013-01-03  1.964690 -0.679447  0.644232  0.750052
2013-01-04 -0.063583  0.464827  1.000784  0.381610
2013-01-05  0.724189 -0.944167  1.124889  0.897737
2013-01-06 -1.222003  0.650685 -0.218867 -0.605794
>>> df2 = pd.DataFrame({ 'A' : 1.,'B' : pd.Timestamp('20130102'),'C' : pd.Series(1,index=list(range(4)),dtype='float32'),'D' : np.array([3] * 4,dtype='int32'),'E' : pd.Categorical(["test","train","test","train"]),'F' : 'foo' })
>>> df2
     A          B    C  D      E    F
0  1.0 2013-01-02  1.0  3   test  foo
1  1.0 2013-01-02  1.0  3  train  foo
2  1.0 2013-01-02  1.0  3   test  foo
3  1.0 2013-01-02  1.0  3  train  foo
>>> df2.dtypes
A           float64
B    datetime64[ns]
C           float32
D             int32
E          category
F            object
dtype: object
>>> df2.<TAB>
SyntaxError: invalid syntax
>>> #viewing data
>>> df.head()
                   A         B         C         D
2013-01-01 -0.411172  1.050868  0.218198  0.927397
2013-01-02  0.349921 -1.254727 -1.101459  1.290130
2013-01-03  1.964690 -0.679447  0.644232  0.750052
2013-01-04 -0.063583  0.464827  1.000784  0.381610
2013-01-05  0.724189 -0.944167  1.124889  0.897737
>>> df.tail()
                   A         B         C         D
2013-01-02  0.349921 -1.254727 -1.101459  1.290130
2013-01-03  1.964690 -0.679447  0.644232  0.750052
2013-01-04 -0.063583  0.464827  1.000784  0.381610
2013-01-05  0.724189 -0.944167  1.124889  0.897737
2013-01-06 -1.222003  0.650685 -0.218867 -0.605794
>>> df.index
DatetimeIndex(['2013-01-01', '2013-01-02', '2013-01-03', '2013-01-04',
               '2013-01-05', '2013-01-06'],
              dtype='datetime64[ns]', freq='D')
>>> df.columns
Index(['A', 'B', 'C', 'D'], dtype='object')
>>> df.values
array([[-0.41117217,  1.05086805,  0.21819804,  0.92739682],
       [ 0.34992051, -1.25472677, -1.10145888,  1.29012993],
       [ 1.96469038, -0.67944738,  0.64423203,  0.75005226],
       [-0.06358307,  0.46482744,  1.0007835 ,  0.38161   ],
       [ 0.72418924, -0.9441669 ,  1.12488881,  0.89773727],
       [-1.22200288,  0.65068532, -0.21886725, -0.60579359]])
>>> df.describe()
              A         B         C         D
count  6.000000  6.000000  6.000000  6.000000
mean   0.223674 -0.118660  0.277963  0.606855
std    1.083801  0.957783  0.839896  0.662719
min   -1.222003 -1.254727 -1.101459 -0.605794
25%   -0.324275 -0.877987 -0.109601  0.473721
50%    0.143169 -0.107310  0.431215  0.823895
75%    0.630622  0.604221  0.911646  0.919982
max    1.964690  1.050868  1.124889  1.290130
>>> #transporting your data
>>> df.T
   2013-01-01  2013-01-02  2013-01-03  2013-01-04  2013-01-05  2013-01-06
A   -0.411172    0.349921    1.964690   -0.063583    0.724189   -1.222003
B    1.050868   -1.254727   -0.679447    0.464827   -0.944167    0.650685
C    0.218198   -1.101459    0.644232    1.000784    1.124889   -0.218867
D    0.927397    1.290130    0.750052    0.381610    0.897737   -0.605794
>>> #sorting by an axis
>>> df.sort_index(axis=1, ascending=False)
                   D         C         B         A
2013-01-01  0.927397  0.218198  1.050868 -0.411172
2013-01-02  1.290130 -1.101459 -1.254727  0.349921
2013-01-03  0.750052  0.644232 -0.679447  1.964690
2013-01-04  0.381610  1.000784  0.464827 -0.063583
2013-01-05  0.897737  1.124889 -0.944167  0.724189
2013-01-06 -0.605794 -0.218867  0.650685 -1.222003
>>> df.sort_values(by='B')
                   A         B         C         D
2013-01-02  0.349921 -1.254727 -1.101459  1.290130
2013-01-05  0.724189 -0.944167  1.124889  0.897737
2013-01-03  1.964690 -0.679447  0.644232  0.750052
2013-01-04 -0.063583  0.464827  1.000784  0.381610
2013-01-06 -1.222003  0.650685 -0.218867 -0.605794
2013-01-01 -0.411172  1.050868  0.218198  0.927397
>>> #selection
>>> #getting
>>> df['A']
2013-01-01   -0.411172
2013-01-02    0.349921
2013-01-03    1.964690
2013-01-04   -0.063583
2013-01-05    0.724189
2013-01-06   -1.222003
Freq: D, Name: A, dtype: float64
>>> #Selecting via [], which slices the rows
>>> df[0:3]
                   A         B         C         D
2013-01-01 -0.411172  1.050868  0.218198  0.927397
2013-01-02  0.349921 -1.254727 -1.101459  1.290130
2013-01-03  1.964690 -0.679447  0.644232  0.750052
>>> df['20130102':'20130104']
                   A         B         C         D
2013-01-02  0.349921 -1.254727 -1.101459  1.290130
2013-01-03  1.964690 -0.679447  0.644232  0.750052
2013-01-04 -0.063583  0.464827  1.000784  0.381610
>>> #selection by label
>>> #for a getting a ceoss section using label
>>> df.loc[dates[0]]
A   -0.411172
B    1.050868
C    0.218198
D    0.927397
Name: 2013-01-01 00:00:00, dtype: float64
>>> #Selecting on a multi-axis by label
>>>  df.loc[:,['A','B']]
SyntaxError: unexpected indent
>>> #Showing label slicing, both endpoints are included
>>> df.loc['20130102':'20130104',['A','B']]
                   A         B
2013-01-02  0.349921 -1.254727
2013-01-03  1.964690 -0.679447
2013-01-04 -0.063583  0.464827
>>> #Reduction in the dimensions of the returned object
>>> df.loc['20130102',['A','B']]
A    0.349921
B   -1.254727
Name: 2013-01-02 00:00:00, dtype: float64
>>> #For getting a scalar value
>>> df.loc[dates[0],'A']
-0.41117217189746974
>>> #For getting fast access to a scalar (equiv to the prior method)
>>> df.at[dates[0],'A']
-0.41117217189746974
>>> #selection by position
>>> #Select via the position of the passed integers
>>> df.iloc[3]
A   -0.063583
B    0.464827
C    1.000784
D    0.381610
Name: 2013-01-04 00:00:00, dtype: float64
>>> #By integer slices, acting similar to numpy/python
>>> df.iloc[3:5,0:2]
                   A         B
2013-01-04 -0.063583  0.464827
2013-01-05  0.724189 -0.944167
>>> #By lists of integer position locations, similar to the numpy/python style
>>> df.iloc[[1,2,4],[0,2]]
                   A         C
2013-01-02  0.349921 -1.101459
2013-01-03  1.964690  0.644232
2013-01-05  0.724189  1.124889
>>> #For slicing rows explicitly
>>> df.iloc[1:3,:]
                   A         B         C         D
2013-01-02  0.349921 -1.254727 -1.101459  1.290130
2013-01-03  1.964690 -0.679447  0.644232  0.750052
>>> #For slicing columns explicitly
>>> df.iloc[:,1:3]
                   B         C
2013-01-01  1.050868  0.218198
2013-01-02 -1.254727 -1.101459
2013-01-03 -0.679447  0.644232
2013-01-04  0.464827  1.000784
2013-01-05 -0.944167  1.124889
2013-01-06  0.650685 -0.218867
>>> #For getting a value explicitly
>>> df.iloc[1,1]
-1.2547267724699074
>>> #For getting fast access to a scalar (equiv to the prior method)
>>> df.iat[1,1]
-1.2547267724699074
>>> #Boolean indexing
>>> df[df.A > 0]
                   A         B         C         D
2013-01-02  0.349921 -1.254727 -1.101459  1.290130
2013-01-03  1.964690 -0.679447  0.644232  0.750052
2013-01-05  0.724189 -0.944167  1.124889  0.897737
>>> df[df > 0]
                   A         B         C         D
2013-01-01       NaN  1.050868  0.218198  0.927397
2013-01-02  0.349921       NaN       NaN  1.290130
2013-01-03  1.964690       NaN  0.644232  0.750052
2013-01-04       NaN  0.464827  1.000784  0.381610
2013-01-05  0.724189       NaN  1.124889  0.897737
2013-01-06       NaN  0.650685       NaN       NaN
>>> #using the isin() method for filtering:
>>> df2 = df.copy()
>>> df2
                   A         B         C         D
2013-01-01 -0.411172  1.050868  0.218198  0.927397
2013-01-02  0.349921 -1.254727 -1.101459  1.290130
2013-01-03  1.964690 -0.679447  0.644232  0.750052
2013-01-04 -0.063583  0.464827  1.000784  0.381610
2013-01-05  0.724189 -0.944167  1.124889  0.897737
2013-01-06 -1.222003  0.650685 -0.218867 -0.605794
>>> df2[df2['E'].isin(['two','four'])]
Traceback (most recent call last):
  File "C:\Users\ksuma\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\indexes\base.py", line 2525, in get_loc
    return self._engine.get_loc(key)
  File "pandas\_libs\index.pyx", line 117, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 139, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 1265, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 1273, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'E'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    df2[df2['E'].isin(['two','four'])]
  File "C:\Users\ksuma\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\frame.py", line 2139, in __getitem__
    return self._getitem_column(key)
  File "C:\Users\ksuma\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\frame.py", line 2146, in _getitem_column
    return self._get_item_cache(key)
  File "C:\Users\ksuma\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\generic.py", line 1842, in _get_item_cache
    values = self._data.get(item)
  File "C:\Users\ksuma\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\internals.py", line 3843, in get
    loc = self.items.get_loc(item)
  File "C:\Users\ksuma\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\indexes\base.py", line 2527, in get_loc
    return self._engine.get_loc(self._maybe_cast_indexer(key))
  File "pandas\_libs\index.pyx", line 117, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 139, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 1265, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 1273, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'E'
>>> s1 = pd.Series([1,2,3,4,5,6], index=pd.date_range('20130102', periods=6))
>>> s1
2013-01-02    1
2013-01-03    2
2013-01-04    3
2013-01-05    4
2013-01-06    5
2013-01-07    6
Freq: D, dtype: int64
>>> df.at[dates[0],'A'] = 0
>>> df
                   A         B         C         D
2013-01-01  0.000000  1.050868  0.218198  0.927397
2013-01-02  0.349921 -1.254727 -1.101459  1.290130
2013-01-03  1.964690 -0.679447  0.644232  0.750052
2013-01-04 -0.063583  0.464827  1.000784  0.381610
2013-01-05  0.724189 -0.944167  1.124889  0.897737
2013-01-06 -1.222003  0.650685 -0.218867 -0.605794
>>> #Setting values by position
>>> df.iat[0,1] = 0
>>> df
                   A         B         C         D
2013-01-01  0.000000  0.000000  0.218198  0.927397
2013-01-02  0.349921 -1.254727 -1.101459  1.290130
2013-01-03  1.964690 -0.679447  0.644232  0.750052
2013-01-04 -0.063583  0.464827  1.000784  0.381610
2013-01-05  0.724189 -0.944167  1.124889  0.897737
2013-01-06 -1.222003  0.650685 -0.218867 -0.605794
>>> #Setting by assigning with a numpy array
>>> df.loc[:,'D'] = np.array([5] * len(df))
>>> df
                   A         B         C  D
2013-01-01  0.000000  0.000000  0.218198  5
2013-01-02  0.349921 -1.254727 -1.101459  5
2013-01-03  1.964690 -0.679447  0.644232  5
2013-01-04 -0.063583  0.464827  1.000784  5
2013-01-05  0.724189 -0.944167  1.124889  5
2013-01-06 -1.222003  0.650685 -0.218867  5
>>> df
                   A         B         C  D
2013-01-01  0.000000  0.000000  0.218198  5
2013-01-02  0.349921 -1.254727 -1.101459  5
2013-01-03  1.964690 -0.679447  0.644232  5
2013-01-04 -0.063583  0.464827  1.000784  5
2013-01-05  0.724189 -0.944167  1.124889  5
2013-01-06 -1.222003  0.650685 -0.218867  5
>>> df2 = df.copy()
>>> df2
                   A         B         C  D
2013-01-01  0.000000  0.000000  0.218198  5
2013-01-02  0.349921 -1.254727 -1.101459  5
2013-01-03  1.964690 -0.679447  0.644232  5
2013-01-04 -0.063583  0.464827  1.000784  5
2013-01-05  0.724189 -0.944167  1.124889  5
2013-01-06 -1.222003  0.650685 -0.218867  5
>>> #missing data
>>> df1 = df.reindex(index=dates[0:4], columns=list(df.columns) + ['E'])df1.loc[dates[0]:dates[1],'E'] = 1
SyntaxError: invalid syntax
>>> df1.dropna(how='any')
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    df1.dropna(how='any')
NameError: name 'df1' is not defined
>>> 
KeyboardInterrupt
>>>  df1 = df.reindex(index=dates[0:4], columns=list(df.columns) + ['D'])df1.loc[dates[0]:dates[1],'D'] = 1
SyntaxError: unexpected indent
>>> df1 = df.reindex(index=dates[0:4], columns=list(df.columns) + ['D'])df1.loc[dates[0]:dates[1],'D'] = 1
SyntaxError: invalid syntax
>>> 
