from sklearn.model_selection import cross_val_score, KFold
from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np

sales_df = pd.read_csv('sales.csv')

# Create X and y arrays
X = sales_df.drop("sales", axis=1).values
print(X.shape)
print(X[:5])
y = sales_df["sales"].values
print(y.shape)
print(y[:5])
# Create a KFold object
kf = KFold(n_splits=6, shuffle=True, random_state=5)

reg = LinearRegression()

# Compute 6-fold cross-validation scores
cv_results = cross_val_score(reg, X, y, cv=kf)

# Print results
print("CV results: {}".format(cv_results))
# Print the mean
print(np.mean(cv_results))

# Print the standard deviation
print(np.std(cv_results))

# Print the 95% confidence interval
print(np.quantile(cv_results, [0.025, 0.975]))
