import pandas as pd

df = pd.read_csv('/Users/allisonbeers/Downloads/scan_dates.csv', index_col='RID')
df['DATE'] = pd.to_datetime(df['DATE'], format='%m/%d/%y')

RID = df.groupby(['RID'])
df['last_scan'] = RID['DATE'].max()

df.to_csv('/Users/allisonbeers/Downloads/scan_dates_updated.csv')


