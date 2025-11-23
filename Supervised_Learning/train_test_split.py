from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

churn_df = pd.read_csv("churn.csv")

y = churn_df["churn"].values
X = churn_df[["account_length", "customer_service_calls"]].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size =0.3, random_state = 21, stratify=y)

# original proportions
unique, counts = np.unique(y, return_counts=True)
print(dict(zip(unique, counts)))
print(np.unique(y_train, return_counts=True))
print(np.unique(y_test, return_counts=True))
