import pandas as pd
from sklearn.linear_model import Lasso
import matplotlib.pyplot as plt

#reads csv with target variables
df = pd.read_csv('/Users/allisonbeers/Downloads/total_lasso.csv')
#df.drop(['Group'])
#d = df['Measure.volume']
#df.drop(d, inplace=True)
X = df.drop('Group', axis=1).values
y = df['Group']
names = df.drop('Group', axis=1).columns

#instantiates & fits regressor
lasso = Lasso(alpha=0.1, normalize=True)
lasso.fit(X, y)
lasso_coef = lasso.coef_

#plots coefficients
_=plt.plot(range(len(names)), lasso_coef)
_=plt.xticks(range(len(names)), names, rotation=60)

plt.title('Lasso Coefficients')
plt.show()