import pandas as pd

df = pd.read_csv('/Users/allisonbeers/Downloads/total.csv')

baseline_data = pd.DataFrame()
baseline = df.loc[df['interscan'] == 0]
baseline_data = baseline_data.append(baseline)
#sig_findings = sig_findings.append(filt)

baseline_data.to_csv('/Users/allisonbeers/Downloads/baseline_data.csv')