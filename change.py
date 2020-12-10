import pandas as pd

#selects csv to use
df = pd.read_csv('/Users/allisonbeers/Downloads/neuropath_UW.csv', index_col='RID')

#imputes missing values of exam date & converts to time series
#CDR['EST_DATE'] = CDR['EXAMDATE'].fillna(CDR['USERDATE'])
df['EXAMDATE'] = pd.to_datetime(df['EXAMDATE'], format='%Y-%m-%d')


#finds baseline date and change in time since
RID = df.groupby(['RID'])
df['baseline_date']  = RID['EXAMDATE'].min()
df['last_eval'] = RID['EXAMDATE'].max()
df['timedelta'] = df['EXAMDATE'] - df['baseline_date']
df['tot_timedelta'] = df['baseline_date'] - df['last_eval']

#finds baseline scores and change in scores since
filt = (df['EXAMDATE'] == df['baseline_date'])
df['baseline_MEM'] = df.loc[filt]['ADNI_MEM']
df['MEM_delta'] = df['ADNI_MEM'] - df['baseline_MEM']
df['baseline_EF'] = df.loc[filt]['ADNI_EF']
df['EF_delta'] = df['ADNI_EF'] - df['baseline_EF']
df['baseline_LAN'] = df.loc[filt]['ADNI_LAN']
df['LAN_delta'] = df['ADNI_LAN'] - df['baseline_LAN']
df['baseline_VS'] = df.loc[filt]['ADNI_VS']
df['VS_delta'] = df['ADNI_VS'] - df['baseline_VS']

#finds rate of change
timedelta_int = pd.to_numeric(df['timedelta'].dt.days, downcast='integer')
df['MEM_rate'] = (df['MEM_delta'] / timedelta_int)
df['EF_rate'] = (df['EF_delta'] / timedelta_int)
df['LAN_rate'] = (df['LAN_delta'] / timedelta_int)
df['VS_rate'] = (df['VS_delta'] / timedelta_int)

#exports data
df.to_csv('/Users/allisonbeers/Downloads/neuropath_UW_updated.csv')

#ADAS csv
	# import pandas as pd

	# #selects csv to use & defines variables
	# adas = pd.read_csv('/Users/allisonbeers/Downloads/neuropath_ADAS.csv', index_col='RID')
	# adas['EXAMDATE'] = pd.to_datetime(adas['EXAMDATE'], format='%Y-%m-%d')

	# #drops responses with -4 value
	# no_response = adas[adas['TOTAL11'] == -4.0].index #& (adas['TOTALMOD'] == -4.0)]
	# adas.drop(no_response, inplace=True)

	# #finds baseline date and change in time since
	# RID = adas.groupby(['RID'])
	# adas['baseline_date']  = RID['EXAMDATE'].min()
	# adas['last_eval'] = RID['EXAMDATE'].max()
	# adas['timedelta'] = adas['EXAMDATE'] - adas['baseline_date']

	# #finds baseline scores and change in scores since
	# filt = (adas['EXAMDATE'] == adas['baseline_date'])
	# adas['baseline_tot'] = adas.loc[filt]['TOTAL11']
	# adas['tot_delta'] = adas['TOTAL11'] - adas['baseline_tot']
	# adas['baseline_tot_mod'] = adas.loc[filt]['TOTALMOD']
	# adas['tot_mod_delta'] = adas['TOTALMOD'] - adas['baseline_tot_mod']

	# #finds rate of change
	# timedelta_int = pd.to_numeric(adas['timedelta'].dt.days, downcast='integer')
	# adas['tot_rate'] = (adas['tot_delta'] / timedelta_int)
	# adas['tot_mod_rate'] = (adas['tot_mod_delta'] / timedelta_int)

	# #exports data
	# adas.to_csv('/Users/allisonbeers/Downloads/neuropath_ADAS_updated.csv')

#CDR csv
	# import pandas as pd

	# #selects csv to use
	# CDR = pd.read_csv('/Users/allisonbeers/Downloads/neuropath_CDR.csv', index_col='RID')

	# #imputes missing values of exam date & converts to time series
	# CDR['EST_DATE'] = CDR['EXAMDATE'].fillna(CDR['USERDATE'])
	# CDR['EST_DATE'] = pd.to_datetime(CDR['EST_DATE'], format='%Y-%m-%d')


	# #finds baseline date and change in time since
	# RID = CDR.groupby(['RID'])
	# CDR['baseline_date']  = RID['EST_DATE'].min()
	# CDR['last_eval'] = RID['EST_DATE'].max()
	# CDR['timedelta'] = CDR['EST_DATE'] - CDR['baseline_date']

	# #finds baseline scores and change in scores since
	# filt = (CDR['EST_DATE'] == CDR['baseline_date'])
	# CDR['baseline_CDRG'] = CDR.loc[filt]['CDGLOBAL']
	# CDR['CDRG_delta'] = CDR['CDGLOBAL'] - CDR['baseline_CDRG']
	# CDR['CDSOB'] = CDR['CDMEMORY'] + CDR['CDORIENT'] + CDR['CDJUDGE'] + CDR['CDCOMMUN'] + CDR['CDHOME'] + CDR['CDCARE']
	# CDR['baseline_CDSOB'] = CDR.loc[filt]['CDSOB']
	# CDR['CDSOB_delta'] = CDR['CDSOB'] - CDR['baseline_CDSOB']

	# #finds rate of change
	# timedelta_int = pd.to_numeric(CDR['timedelta'].dt.days, downcast='integer')
	# CDR['CDRG_rate'] = (CDR['CDRG_delta'] / timedelta_int)
	# CDR['CDSOB_rate'] = (CDR['CDSOB_delta'] / timedelta_int)

	# #exports data
	# CDR.to_csv('/Users/allisonbeers/Downloads/neuropath_CDR_updated.csv')
