import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import pickle

df = pd.read_csv("clean_dataset.csv")

X = df.drop("weight_loss_kg", axis=1)
y = df["weight_loss_kg"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestRegressor()
model.fit(X_train, y_train)

pickle.dump(model, open("model.pkl", "wb"))

print("Model trained and saved!")