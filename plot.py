from matplotlib import pyplot as plt
import pandas as pd 

#histogram

#reads csv with data and desired RIDs
df = pd.read_csv('/Users/allisonbeers/Downloads/NPI_lasso.csv')
df2 = pd.read_csv('/Users/allisonbeers/Downloads/RID.csv')

d = df[df['RID'].duplicated()].index
df.drop(d, inplace=True)

#ax = plt.gca()

filt_LB = df.loc[df['RID'].isin(df2['LB_RID'])]
filt_AD = df.loc[df['RID'].isin(df2['AD_RID'])]

rate_LB = filt_LB['NPIL']
rate_AD = filt_AD['NPIL']

#plots rates side by side
plt.hist([rate_LB, rate_AD], bins=2, edgecolor='black', color=['blue', 'white'], label=['AD/LBD', 'AD'])

#plt.hist(rate_AD, bins=5, edgecolor='black', hatch='x', color='red', label='AD')
plt.legend(['AD/LBD', 'AD'], loc='upper right')
plt.xlabel('Recorded Presence of NPIL Element')
plt.xticks(ticks=[0.25, 0.75], labels=['No', 'Yes'])
plt.yticks(ticks=[0, 5, 10, 15, 20, 25, 30])
plt.ylabel('Total Number of Patients')
#plt.title('Tau/ABeta Ratios Among Patients')
plt.show()


#scatter plot
#reads csv with data and desired RIDs
# df = pd.read_csv('/Users/allisonbeers/Downloads/CDR_plot.csv')
# df2 = pd.read_csv('/Users/allisonbeers/Downloads/RID.csv')

# #ax = plt.gca()

# filt_LB = df.loc[df['RID'].isin(df2['LB_RID'])]
# filt_AD = df.loc[df['RID'].isin(df2['AD_RID'])]
# #LB = df.loc[filt_LB]

# x_LB = filt_LB['timedelta_int']
# y_LB = filt_LB['CDSOB_delta']

# x_AD = filt_AD['timedelta_int']
# y_AD = filt_AD['CDSOB_delta']

# plt.scatter(x_LB, y_LB, color='blue', label='LB/AD')
# plt.scatter(x_AD, y_AD, color='red', label='AD')
# plt.legend(['AD/LBD', 'AD'], loc='upper right')
# plt.xlabel('Days Since Baseline Exam')
# plt.ylabel('Change in CDR SOB Score')
# plt.title('Change in CDR SOB Score Over Time')
# plt.show()

#other things

#plots everyone
# df = pd.read_csv('/Users/allisonbeers/Downloads/CDR_plot.csv', index_col='RID')

# ax = plt.gca()

# df.plot(kind='scatter', x='timedelta_int', y='CDSOB_delta', color='red', label='CDR', ax=ax)
# df.plot(kind='scatter', x='timedelta_int', y='CDRG_delta', color='blue', label='CDR Global', ax=ax)

# plt.xlabel('Days')
# plt.ylabel('Change in CDR Score')
# plt.title('Change in CDR Score Over Time')
# plt.show()

# LB_RID = [42, 53, 108, 149, 183, 256, 408, 448, 492, 565, 567, 691, 702, 723, 724, 830, 834, 916, 985, 1080, 1116, 1118, 1281, 1282, 1308, 1384, 4039, 4223, 4263, 4366, 4526, 4802, 4910, 4936, 5218]

# AD_RID = [78, 93, 326, 362, 400, 458, 479, 739, 821, 853, 861, 880, 978, 1203, 1246, 1271, 1393, 1425, 4474, 4500, 4770, 4892, 4921, 5017]

# #plots by groups
# df = pd.read_csv('/Users/allisonbeers/Downloads/CDR_plot.csv')

# ax = plt.gca()

# for x in LB_RID:
# 	filt_LB = df.loc[(df['RID'] == x)]
# 	filt_LB.plot(kind='scatter', x='timedelta_int', y='CDSOB_delta', color='red', ax=ax)

# for y in AD_RID:
# 	filt_AD = (df['RID'] == y)
# 	df.loc[filt_AD].plot(kind='scatter', x='timedelta_int', y='CDSOB_delta', color='blue', ax=ax)

# plt.xlabel('Days Since Baseline Exam')
# plt.ylabel('Change in CDR Score')
# plt.title('Change in CDR Score Over Time')
# plt.show()
