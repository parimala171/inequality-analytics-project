import schedule
import time
import pandas as pd
import pickle
from sklearn.ensemble import RandomForestClassifier

def retrain():
    print("Auto retraining started...")

    df_old = pd.read_csv("raw_inequality_data.csv")
    df_new = pd.read_csv("new_data.csv")

    df = pd.concat([df_old, df_new])

    df = df[["AGE", "EDUC", "INCTOT"]]
    df = df.dropna()
    df = df[df["INCTOT"] > 0]

    df["target"] = (df["INCTOT"] > 50000).astype(int)

    X = df[["AGE", "EDUC"]]
    y = df["target"]

    model = RandomForestClassifier()
    model.fit(X, y)

    pickle.dump(model, open("model.pkl", "wb"))

    print("Model auto-updated!")

# every 1 hour
schedule.every(1).hours.do(retrain)

while True:
    schedule.run_pending()
    time.sleep(1)