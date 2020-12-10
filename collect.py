import pandas as pd

#selects csv files to use to collect data
df = pd.read_csv('/Users/allisonbeers/Downloads/NPIQ_new.csv', index_col='RID', low_memory=False)
df2 = pd.read_csv('/Users/allisonbeers/Downloads/RID.csv', low_memory=False)

#median = df.loc[df['BATCH'] == 'MEDIAN']
#df.drop(median, labels='BATCH', axis=0)

#instantiates df & collects data
neuropath_df = pd.DataFrame()

# filt_LB = df.loc[df.index.isin(df2['LB_RID'])]
# neuropath_df = neuropath_df.append(filt_LB)

# filt_AD = df.loc[df.index.isin(df2['AD_RID'])]
# neuropath_df = neuropath_df.append(filt_AD)

A = df.loc[df['NPIA'] == 1]
neuropath_df = neuropath_df.append(A)

B = df.loc[df['NPIB'] == 1]
neuropath_df = neuropath_df.append(B)

C = df.loc[df['NPIC'] == 1]
neuropath_df = neuropath_df.append(C)

D = df.loc[df['NPID'] == 1]
neuropath_df = neuropath_df.append(D)

E = df.loc[df['NPIE'] == 1]
neuropath_df = neuropath_df.append(E)

F = df.loc[df['NPIF'] == 1]
neuropath_df = neuropath_df.append(F)

G = df.loc[df['NPIG'] == 1]
neuropath_df = neuropath_df.append(G)

H = df.loc[df['NPIH'] == 1]
neuropath_df = neuropath_df.append(H)

I = df.loc[df['NPII'] == 1]
neuropath_df = neuropath_df.append(I)

J = df.loc[df['NPIJ'] == 1]
neuropath_df = neuropath_df.append(J)

K = df.loc[df['NPIK'] == 1]
neuropath_df = neuropath_df.append(K)

L = df.loc[df['NPIL'] == 1]
neuropath_df = neuropath_df.append(L)

neuropath_df.to_csv('/Users/allisonbeers/Downloads/NPI_ones.csv')


#old way
#desired RIDs
#RID_list = [42, 78, 53, 93, 108, 326, 149, 362, 183, 400, 256, 458, 408, 479, 448, 739, 492, 821, 565, 853, 567, 861, 691, 880, 702, 978, 723, 1203, 724, 1246, 830, 1271, 834, 1393, 916, 1425, 985, 1080, 1116, 1118, 1281, 1282, 1308, 1384, 4474, 4500, 4770, 4892, 4921, 5017, 4039, 4223, 4263, 4366, 4526, 4802, 4910, 4936, 5218]

#for x in RID_list:
	#new = df.loc[df['RID'] == x]
	#neuropath_df = neuropath_df.append(new, ignore_index=True)


#exports data with only desired RIDs
#neuropath_df.to_csv('/Users/allisonbeers/Downloads/neuropath_MMSE.csv')

#ADAS
	# import pandas as pd

	# #selects csv files to use to collect data
	# CDR = pd.read_csv('/Users/allisonbeers/Downloads/ADASSCORES.csv')

	# #desired RIDs
	# RID_list = [42, 78, 53, 93, 108, 326, 149, 362, 183, 400, 256, 458, 408, 479, 448, 739, 492, 821, 565, 853, 567, 861, 691, 880, 702, 978, 723, 1203, 724, 1246, 830, 1271, 834, 1393, 916, 1425, 985, 1080, 1116, 1118, 1281, 1282, 1308, 1384, 4474, 4500, 4770, 4892, 4921, 5017, 4039, 4223, 4263, 4366, 4526, 4802, 4910, 4936, 5218]

	# #instantiates df & collects data
	# neuropath_ADAS = pd.DataFrame()

	# for x in RID_list:
	# 	new = adas.loc[adas['RID'] == x]
	# 	neuropath_ADAS = neuropath_ADAS.append(new, ignore_index=True)


	# #exports data with only desired RIDs
	# neuropath_ADAS.to_csv('/Users/allisonbeers/Downloads/neuropath_ADAS.csv')



