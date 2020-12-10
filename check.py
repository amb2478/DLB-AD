import pandas as pd

df = pd.read_csv('/Users/allisonbeers/Downloads/glm.csv')

#if df['i.p.value'] < .05:
	#print (df['variable'], df['i.term'], df['i.p.value'])

sig_findings = pd.DataFrame()
filt = (df['i.term'] == 'variable')
df =df[filt]

sig = df.loc[df['i.p.value'] < .05]
sig_findings = sig_findings.append(sig)
#sig_findings = sig_findings.append(filt)

sig_findings.to_csv('/Users/allisonbeers/Downloads/glm.csv')