from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("dashboard.html")

@app.route("/predict", methods=["POST"])
def predict():
    age = float(request.form["age"])
    education = float(request.form["education"])
    esr = float(request.form["esr"])
    st = float(request.form["st"])

    prediction = model.predict([[age, education, esr, st]])[0]

    result = "High Income" if prediction == 1 else "Low Income"

    return render_template("result.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)