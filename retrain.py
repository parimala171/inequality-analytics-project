import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

print("Loading RAW dataset...")

df = pd.read_csv(
    "raw_inequality_data.csv",
    usecols=["AGEP", "SCHL", "PINCP","ESR","ST"],
    nrows=300000
)

print("Shape:", df.shape)

df = df.rename(columns={
    "AGEP": "Age",
    "SCHL": "Educ",
    "PINCP": "Income",
    "ESR": "Employment",
    "ST":"State"
})

# Cleaning
df = df[["Age", "Educ", "Income","Employment","State"]]
df = df.dropna()
df = df[df["Income"] > 0]

# Save cleaned data 
df.to_csv("cleaned_inequality_data.csv", index=False)

# Target
df["target"] = (df["Income"] > 50000).astype(int)

X = df[["Age", "Educ","Employment","State"]]
y = df["target"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = RandomForestClassifier()
model.fit(X_train, y_train)

accuracy = model.score(X_test, y_test)
print("Model Accuracy:", accuracy)

#Save model 
pickle.dump(model, open("model.pkl", "wb"))

print("cleaned_inequality_data.csv created")
print("model.pkl created")