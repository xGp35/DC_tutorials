import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import Lasso

sales_df = pd.read_csv('sales.csv')

# Create X and y arrays
X = sales_df.drop("sales", axis=1).values
y = sales_df["sales"].values

sales_columns = sales_df.drop("sales", axis=1).columns

# Instantiate a lasso regression model
lasso = Lasso(alpha = 0.3)

# Compute and print the coefficients
lasso_coef = lasso.fit(X,y).coef_
print(lasso_coef)
plt.bar(sales_columns, lasso_coef)
plt.xticks(rotation=45)
plt.show()