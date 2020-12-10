import pandas as pd

#selects csv to use
df = pd.read_csv('/Users/allisonbeers/Downloads/imaging.csv')
stats = pd.read_csv('/Users/allisonbeers/Downloads/stats.csv')
dates = pd.read_csv('/Users/allisonbeers/Downloads/dates.csv')
df2 = pd.read_csv('/Users/allisonbeers/Downloads/RID.csv')

#RID_list = [42, 53, 108, 149, 183, 256, 408, 448, 492, 565, 567, 691, 702, 723, 724, 830, 834, 916, 985, 1080, 1116, 1118, 1281, 1282, 1308, 1384, 4039, 4223, 4263, 4366, 4526, 4802, 4910, 4936, 5218, 78, 93, 326, 362, 400, 458, 479, 739, 821, 853, 861, 880, 978, 1203, 1246, 1271, 1393, 1425, 4474, 4500, 4770, 4892, 4921, 5017]

#filt = stats.loc[stats['RID'].isin(df['RID'])]

#finds scan date of subject
#filt = dates.loc[dates['RID'].isin(df['RID'])]
#df['scan_date'] = filt['scan_date']

#gets demographics
filt = df.loc[df['RID'].isin(stats['RID'])]
stats['DOD'] = filt['scan_date']
#df['dod'] = df['dod'].fillna(1)
# df['RID2'] = filt['RID']
# df['gender'] = filt['gender']
# df['education'] = filt['education']
# df['age_dod'] = filt['age_dod']
# df['race'] = filt['race']
#df['dod'] = RID[stats.loc[stats['dod']]]

#sorts
#RID = df.groupby(['RID'])
#df['DOD'] = RID['dod']

#exports data
stats.to_csv('/Users/allisonbeers/Downloads/stats_updated.csv')
