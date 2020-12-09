import pandas as pd

#selects csv to use
df = pd.read_csv('/Users/allisonbeers/Downloads/NPIQ_new.csv', index_col='RID')

#imputes missing values of exam date & converts to time series
df['ESTDATE'] = df['EXAMDATE'].fillna(df['USERDATE'])
df['ESTDATE'] = pd.to_datetime(df['ESTDATE'], format='%Y-%m-%d')

#gets rid of rows with duplicate estdates
#d = df[df['ESTDATE'].duplicated()].index
#df.drop(d, inplace=True)

#finds baseline date and change in time since
RID = df.groupby(['RID'])
df['baseline_date']  = RID['ESTDATE'].min()
df['last_eval'] = RID['ESTDATE'].max()
df['tot_timedelta'] = df['last_eval'] - df['baseline_date']

#finds baseline scores and change in score to last eval
first = (df['ESTDATE'] == df['baseline_date'])
last = (df['ESTDATE'] == df['last_eval'])

df['baseline_score'] = df.loc[first]['NPISCORE']
df['last_score'] = df.loc[last]['NPISCORE']
df['score_delta'] = (df['last_score'] - df['baseline_score'])

#finds rate of change
df['timedelta_int'] = pd.to_numeric(df['tot_timedelta'].dt.days, downcast='integer')
df['score_delta_rate'] = (df['score_delta'] / df['timedelta_int'])

#exports data
df.to_csv('/Users/allisonbeers/Downloads/NPIQ_delta.csv')

#drops missing values
#no_response = df[df[''] == -4.0].index #& (adas['TOTALMOD'] == -4.0)]
#df.drop(no_response, inplace=True)

#CDR SOB
# df['CDSOB'] = df['CDMEMORY'] + df['CDORIENT'] + df['CDJUDGE'] + df['CDCOMMUN'] + df['CDHOME'] + df['CDCARE']
# df['baseline_CDSOB'] = df.loc[first]['CDSOB']
# df['last_CDSOB'] = df.loc[last]['CDSOB']
# df['CDSOB_delta'] = df['last_CDSOB'] - df['baseline_CDSOB']

#MMSE struggles
	# import pandas as pd

	# #selects csv to use
	# df = pd.read_csv('/Users/allisonbeers/Downloads/neuropath_MMSE_updated.csv', index_col='RID')

	# #imputes missing values of exam date & converts to time series
	# df['ESTDATE'] = df['EXAMDATE'].fillna(df['USERDATE'])
	# df['ESTDATE'] = pd.to_datetime(df['ESTDATE'], format='%Y-%m-%d')


	# #finds baseline date and change in time since
	# RID = df.groupby(['RID'])
	# df['baseline_date']  = RID['ESTDATE'].min()
	# df['last_eval'] = RID['ESTDATE'].max()
	# df['tot_timedelta'] = df['last_eval'] - df['baseline_date']

	# #finds baseline scores and change in score to last eval
	# first = (df['ESTDATE'] == df['baseline_date'])
	# last = (df['ESTDATE'] == df['last_eval'])

	# df['baseline'] = df.loc[first]['MMSCORE']
	# #df['last_score'] = df.loc[last]['MMSCORE']
	# #df['tot_delta'] = df['last_score'] - df['baseline']


	# #finds rate of change
	# #timedelta_int = pd.to_numeric(df['tot_timedelta'].dt.days, downcast='integer')
	# #df['tot_rate'] = (df['tot_delta'] / timedelta_int)

	# d = df[df.index.duplicated()]
	# print(d)

	# #exports data
	# df.to_csv('/Users/allisonbeers/Downloads/neuropath_MMSE_updated.csv')

#UW NPS
# import pandas as pd

# #selects csv to use
# df = pd.read_csv('/Users/allisonbeers/Downloads/neuropath_UW.csv', index_col='RID')

# #converts column to timeseries
# df['EXAMDATE'] = pd.to_datetime(df['EXAMDATE'], format='%Y-%m-%d')

# #finds baseline date and change in time since
# RID = df.groupby(['RID'])
# df['baseline_date']  = RID['EXAMDATE'].min()
# df['last_eval'] = RID['EXAMDATE'].max()
# df['tot_timedelta'] = df['last_eval'] - df['baseline_date']

# #finds baseline scores and change in score to last eval
# first = (df['EXAMDATE'] == df['baseline_date'])
# last = (df['EXAMDATE'] == df['last_eval'])

# df['baseline_MEM'] = df.loc[first]['ADNI_MEM']
# df['last_MEM'] = df.loc[last]['ADNI_MEM']
# df['MEM_delta'] = (df['last_MEM'] - df['baseline_MEM'])

# df['baseline_EF'] = df.loc[first]['ADNI_EF']
# df['last_EF'] = df.loc[last]['ADNI_EF']
# df['EF_delta'] = (df['last_EF'] - df['baseline_EF'])

# df['baseline_LAN'] = df.loc[first]['ADNI_LAN']
# df['last_LAN'] = df.loc[last]['ADNI_LAN']
# df['LAN_delta'] = (df['last_LAN'] - df['baseline_LAN'])

# df['baseline_VS'] = df.loc[first]['ADNI_VS']
# df['last_VS'] = df.loc[last]['ADNI_VS']
# df['VS_delta'] = (df['last_VS'] - df['baseline_VS'])

# #finds rate of change
# df['timedelta_int'] = pd.to_numeric(df['tot_timedelta'].dt.days, downcast='integer')
# df['MEM_delta_rate'] = (df['MEM_delta'] / df['timedelta_int'])
# df['EF_delta_rate'] = (df['EF_delta'] / df['timedelta_int'])
# df['LAN_delta_rate'] = (df['LAN_delta'] / df['timedelta_int'])
# df['VS_delta_rate'] = (df['VS_delta'] / df['timedelta_int'])

# #exports data
# df.to_csv('/Users/allisonbeers/Downloads/neuropath_UW_updated.csv')