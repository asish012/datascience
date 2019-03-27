## Selecting data

| Operation     | Syntax                | Result    | Example                     |
|:--------------|:----------------------|:----------|:----------------------------|
| Select Item<br>from Series | s[index] | Object    | s[0] \| s['a'] \| s.loc[0]  |
| Select Column | df[col] \| df.col     | Series    | df['column1'] \| df.column1 |
| Select Row    | df.loc[index]         | Series    | df.loc['a']                 |
| Select Row    | df.loc[position]      | Series    | df.loc[2]                   |
| Select Rows   | df[n:n] \| df.loc[n:n]| DataFrame | df[1:4]  \|  df.loc[2:]     |
| Select Rows   | df.loc[vector_bool]   | DataFrame | df.loc[df > 0]              |
|||||
| Select Rows   | df.where(vector_bool) | DataFrame | df.where(df > 0)            |
| Select Rows   | df.where(vector_bool) | DataFrame | df.where(df > 0, 0) <br> _inserts 0 where condition is false_ |


## Deleting data

| Operation                     | Syntax                       | Result    | Example                                |
|:------------------------------|:-----------------------------|:----------|:---------------------------------------|
| Delete Column <br> (inspace)  | del df[column name]          |        | del df['column1']                         |
| Delete Column <br> (inspace)  | df.pop(column name)          | Series | df.pop('column1')                         |
| Delete Column <br> (from view)| df.drop(column_name, axis=1) |        | df.drop('column1', axis=1)                |
| Delete Row <br> (from view)   | df.drop(column_name, axis=0) |        | df.drop('row1', axis=0) <br>df.drop(df.index[2]) |


## Contatenation
- Performs concatenation operation along an axis, while performing optional set logic (union or intersection) on the other axis
  > If we have parameter *axis=0*, it will concatenate along 0-axis and make union of 1-axis
  > If we have parameter *axis=1*, it will concatenate along 1-axis and make union of 0-axis
- We can perform 2 join operations (outer, inner)
- We can construct hierarchical index by passing *key* parameter (see example)
- pd.concat() is in main namespace

- Function definition:
  ```
  pd.concat(objs, axis=0, join='outer', ignore_index=False, ...)
  ```
- DataFrames:
  **df1**

  |   | A  | B  | C  | D  |
  |---|:---|:---|:---|:---|
  | 0 | A0 | B0 | C0 | D0 |
  | 1 | A1 | B1 | C1 | D1 |
  | 2 | A2 | B2 | C2 | D2 |
  | 3 | A3 | B3 | C3 | D3 |

  **df2**

  |   | B  | D  | F  |
  |---|:---|:---|:---|
  | 2 | B2 | D2 | F2 |
  | 3 | B3 | D3 | F3 |
  | 6 | B6 | D6 | F6 |
  | 7 | B7 | D7 | F7 |

- Example: Concat along index axis (axis=0) (makes union of axis-1)
  ```
  result = pd.concat([df1, df2])
  ```
  **Output:**

  |   | A   | B   | C   | D   | F   |
  |---|:----|:----|:----|:----|:----|
  | 0 | A0  | B0  | C0  | D0  | NaN |
  | 1 | A1  | B1  | C1  | D1  | NaN |
  | 2 | A2  | B2  | C2  | D2  | NaN |
  | 3 | A3  | B3  | C3  | D3  | NaN |
  | 2 | NaN | B2  | NaN | D2  | F2  |
  | 3 | NaN | B3  | NaN | D3  | F3  |
  | 6 | NaN | B6  | NaN | D6  | F6  |
  | 7 | NaN | B7  | NaN | D7  | F7  |

- Example: Concat along column axis (axis=1) (makes union of axis-0)
  ```
  result = pd.concat([df1, df2], axis=1)
  ```
  **Output:**

  |   | A   | B   | C   | D   | B   | D   | F   |
  |---|:----|:----|:----|:----|:----|:----|:----|
  | 0 | A0  | B0  | C0  | D0  | NaN | NaN | NaN |
  | 1 | A1  | B1  | C1  | D1  | NaN | NaN | NaN |
  | 2 | A2  | B2  | C2  | D2  | B2  | D2  | F2  |
  | 3 | A3  | B3  | C3  | D3  | B3  | D3  | F3  |
  | 6 | NaN | NaN | NaN | NaN | B6  | D6  | F6  |
  | 7 | NaN | NaN | NaN | NaN | B7  | D7  | F7  |

- Example: Inner join
  ```
  result = pd.concat([df1, df2], axis=1, join='inner')
  ```
  **Output:**

  |   | A  | B  | C  | D  | B  | D  | F  |
  |---|:---|:---|:---|:---|:---|:---|:---|
  | 2 | A2 | B2 | C2 | D2 | B2 | D2 | F2 |
  | 3 | A3 | B3 | C3 | D3 | B3 | D3 | F3 |

- Example: Left inner join
  ```
  result = pd.concat([df1, df2], axis=1, join='inner', join_axes=[df1.index])
  ```
  **Output:**

  |   | A   | B   | C   | D   | B   | D   | F   |
  |---|:----|:----|:----|:----|:----|:----|:----|
  | 0 | A0  | B0  | C0  | D0  | NaN | NaN | NaN |
  | 1 | A1  | B1  | C1  | D1  | NaN | NaN | NaN |
  | 2 | A2  | B2  | C2  | D2  | B2  | D2  | F2  |
  | 3 | A3  | B3  | C3  | D3  | B3  | D3  | F3  |

- Example: Hierarchical indexing using *key*
  ```
  pd.concat([df1, df2], axis=0, keys=['x', 'y'])
  ```

  **Output**

  |   |   | A   | B   | C   | D   | F   |
  |---|---|:----|:----|:----|:----|:----|
  | x | 0 | A0  | B0  | C0  | D0  | NaN |
  |   | 1 | A1  | B1  | C1  | D1  | NaN |
  |   | 2 | A2  | B2  | C2  | D2  | NaN |
  |   | 3 | A3  | B3  | C3  | D3  | NaN |
  | y | 2 | NaN | B2  | NaN | D2  | F2  |
  |   | 3 | NaN | B3  | NaN | D3  | F3  |
  |   | 6 | NaN | B6  | NaN | D6  | F6  |
  |   | 7 | NaN | B7  | NaN | D7  | F7  |


## Append
- It's a shortcut of concatenation along axis-0
- pd.append() is an instance method of Series and DataFrame

- Function definition:
  ```
  pd.append(other, ignore_index=False, ...)
  ```

- Example: 
  ```
  result = df1.append(df2)
  ```
  **Output:**

  |   | A   | B   | C   | D   | F   |
  |---|:----|:----|:----|:----|:----|
  | 0 | A0  | B0  | C0  | D0  | NaN |
  | 1 | A1  | B1  | C1  | D1  | NaN |
  | 2 | A2  | B2  | C2  | D2  | NaN |
  | 3 | A3  | B3  | C3  | D3  | NaN |
  | 2 | NaN | B2  | NaN | D2  | F2  |
  | 3 | NaN | B3  | NaN | D3  | F3  |
  | 6 | NaN | B6  | NaN | D6  | F6  |
  | 7 | NaN | B7  | NaN | D7  | F7  |
  
  > Note: Result is same as `pd.concat([df1, df2])`

- Example: Append a row (Series)
  ```
  s = pd.Series('Xa Xb Xc Xd'.split(), index='A B C D'.split())
  result = df1.append(s, ignore_index=True)
  ```
  **Output:**

  |   | A  | B  | C  | D  |
  |---|:---|:---|:---|:---|
  | 0 | A0 | B0 | C0 | D0 |
  | 1 | A1 | B1 | C1 | D1 |
  | 2 | A2 | B2 | C2 | D2 |
  | 3 | A3 | B3 | C3 | D3 |
  | 4 | Xa | Xb | Xc | Xd |


## Merge
- Similar to database join Operation
- Column-name passed as 'on' parameter must be present in both the left and right DataFrame objects
- Doesn't take into account **indices** from either dataframes
- pd.merge() is part of pandas main namespace <br>
  It is also available as object method of Series and DataFrame

- Function definition:
  ```
  pd.merge(left, right, how='inner', on=None, left_on=None, right_on=None, left_index=False, right_index=False, ...)
  ```

- Example:
  ```
  result = pd.merge(df1, df2)
  ```
  **Output:**

  |   | A  | B  | C  | D  | F  |
  |---|:---|:---|:---|:---|:---|
  | 0 | A2 | B2 | C2 | D2 | F2 |
  | 1 | A3 | B3 | C3 | D3 | F3 |

  > Note: Notice the index here. It has created a new index without considering indices from either of the input data frames.

- Example: Outer join. (union of keys from both frames)
  ```
  pd.merge(df1, df2, how='outer')
  ```
  **Output:**

  |   | A   | B   | C   | D   | F   |
  |---|:----|:----|:----|:----|:----|
  | 0 | A0  | B0  | C0  | D0  | NaN |
  | 1 | A1  | B1  | C1  | D1  | NaN |
  | 2 | A2  | B2  | C2  | D2  | F2  |
  | 3 | A3  | B3  | C3  | D3  | F3  |
  | 6 | NaN | B6  | NaN | D6  | F6  |
  | 7 | NaN | B7  | NaN | D7  | F7  |

- Example: Inner join (intersection of keys from both frames)
  ```
  pd.merge(df1, df2, how='inner')
  ```
  **Output:**

  |   | A   | B   | C   | D   | F   |
  |---|:----|:----|:----|:----|:----|
  | 2 | A2  | B2  | C2  | D2  | F2  |
  | 3 | A3  | B3  | C3  | D3  | F3  |

- Example: Join on column
  ```
  pd.merge(df1, df2, on=['B'])
  ```
  **Output:**

  |   | A   | B   | C   | D_x | D_y | F   |
  |---|:----|:----|:----|:----|:----|:----|
  | 0 | A2  | B2  | C2  | D2  | D6  | F6  |
  | 1 | A3  | B3  | C3  | D3  | D7  | F7  |

  > Note: 'B' is the key column on what inner-join was performed. Also notice the totaly new index.


## Join
- Unlike *merge* operation *join* doesn't ignore indices. By default it uses dataframe's indices as key to perform join operation
- Combines columns of two potentially-different-indexed dataframes
- Available as object function (object act as *left* dataframe of *merge* operation)

- Function definition:
  ```
  df1.join(other, on=None, how='left', lsuffix='', rsuffix='', sort=False)
  ```

- Example:
  ```
  df1.join(df2, lsuffix='_l', rsuffix='_r')
  ```

  |   | A   | B_l | C   | D_l | B_r | D_r | F   |
  |---|:----|:----|:----|:----|:----|:----|:----|
  | 0 | A0  | B0  | C0  | D0  | NaN | NaN | NaN |
  | 1 | A1  | B1  | C1  | D1  | NaN | NaN | NaN |
  | 2 | A2  | B2  | C2  | D2  | B2  | D2  | F2  |
  | 3 | A3  | B3  | C3  | D3  | B3  | D3  | F3  |

  > Note: Same result can be achieved with *merge* function along with some additional parameters
    ```
    pd.merge(df1, df2, left_index=True, right_index=True, how='left')
    ```

    |   | A   | B_x | C   | D_x | B_y | D_y | F   |
    |---|:----|:----|:----|:----|:----|:----|:----|
    | 0 | A0  | B0  | C0  | D0  | NaN | NaN | NaN |
    | 1 | A1  | B1  | C1  | D1  | NaN | NaN | NaN |
    | 2 | A2  | B2  | C2  | D2  | B2  | D2  | F2  |
    | 3 | A3  | B3  | C3  | D3  | B3  | D3  | F3  |

## More about Pandas-Datastructure
[GregReda : Pandas Datastructure](http://www.gregreda.com/2013/10/26/intro-to-pandas-data-structures/)
