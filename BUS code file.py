#!/usr/bin/env python
# coding: utf-8

# In[1]:


# importing libraries
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

# settings
mpl.rcParams['figure.dpi'] = 600
bmtc_df = pd.read_parquet('dataset/BMTC.parquet.gzip')
bmtc_df.head()
BusID	Latitude	Longitude	Speed	Timestamp
0	150212121	13.074558	77.445549	0.0	2019-08-01 07:00:02
1	150212121	13.074558	77.445549	0.0	2019-08-01 07:00:12
2	150212121	13.074558	77.445549	0.0	2019-08-01 07:00:22
3	150212121	13.074558	77.445549	0.0	2019-08-01 07:00:32
4	150212121	13.074558	77.445549	0.0	2019-08-01 07:00:42
print(bmtc_df['Latitude'].max(), bmtc_df['Latitude'].min())
print(bmtc_df['Longitude'].max(), bmtc_df['Longitude'].min())
13.155129 12.794401
77.788345 77.418175
input_df = pd.read_csv('dataset/Input.csv')
input_df.head()
Unnamed: 0	Source_Lat	Source_Long	Dest_Lat	Dest_Long
0	0	12.941644	77.557335	12.942002	77.551605
1	1	12.845487	77.662079	12.845881	77.667892
2	2	12.973492	77.622871	12.957303	77.621246
3	3	12.819298	77.688995	12.814241	77.692986
4	4	12.973240	77.615402	13.016170	77.627800
print(input_df['Source_Lat'].min(), input_df['Source_Lat'].max())
print(input_df['Source_Long'].min(), input_df['Source_Long'].max())
12.794401 13.155079
77.418312 77.788261
ground_truth_df = pd.read_csv('dataset/GroundTruth.csv')
ground_truth_df.head()
Unnamed: 0	TT
0	0	2.833333
1	1	1.500000
2	2	21.250000
3	3	2.000000
4	4	35.733333
def saveBusPath(id):
    busid_path_map = bmtc_df[bmtc_df['BusID'] == id][['Latitude', 'Longitude']]
    busid_path_map['Latitude'] = busid_path_map['Latitude'] - 12.7
    busid_path_map['Longitude'] = busid_path_map['Longitude'] - 77.35
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(busid_path_map['Latitude'].to_numpy(), busid_path_map['Longitude'].to_numpy(), s=0.01)
    fig.savefig(f'dataset/bus_paths/{id}.png')
    plt.close(fig)
def printBusPath(id):
    busid_path_map = bmtc_df[bmtc_df['BusID'] == id]
    busid_path_map['Latitude'] = busid_path_map['Latitude'] - 12.7
    busid_path_map['Longitude'] = busid_path_map['Longitude'] - 77.35
    fig, ax = plt.subplots()
    ax.scatter(busid_path_map['Latitude'].to_numpy(), busid_path_map['Longitude'].to_numpy(), s=0.01)
    min_time = busid_path_map[busid_path_map['Timestamp'] == busid_path_map['Timestamp'].min()]
    ax.scatter(min_time['Latitude'], min_time['Longitude'], s=3, color='red')
    plt.show()
for id in bmtc_df['BusID'].unique()[0:5]:
    print('id =', id)
    printBusPath(id)
id = 150212121
tmp/ipykernel_59651/967297625.py:3:(SettingWithCopyWarning:)
A value is trying to be set on a copy of a slice from a DataFrame.
Try using .loc[row_indexer,col_indexer] = value instead

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
  busid_path_map['Latitude'] = busid_path_map['Latitude'] - 12.7
tmp/ipykernel_59651/967297625.py:4:(SettingWithCopyWarning:)
A value is trying to be set on a copy of a slice from a DataFrame.
Try using .loc[row_indexer,col_indexer] = value instead

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
  busid_path_map['Longitude'] = busid_path_map['Longitude'] - 77.35

id = 150218000

id = 150218006

id = 150218010

id = 150218014

bmtc_df.dtypes
BusID                 int64
Latitude            float64
Longitude           float64
Speed               float64
Timestamp    datetime64[ns]
dtype: object


# In[ ]:




