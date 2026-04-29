# 📊 Income Inequality Analysis and Prediction
### using Machine Learning and Power BI

🌍 **Aligned with SDG Goal 10 – Reduced Inequalities**

---

## 🧠 Project Overview

This project analyzes income inequality and predicts income categories using Machine Learning.

It helps to understand the gap between different income groups and provides insights through an interactive dashboard.

---

## 🎯 Objectives

- Analyze income distribution  
- Identify poverty levels  
- Predict income category (High / Low)  
- Visualize insights using Power BI  

---

## 📂 Dataset

- Source: US Census (ACS Data)  
- Records: ~300,000  

### Features:
- Age  
- Education  
- Employment  
- Income  
- State  

📌 Note: Dataset is large and not included in this repository.

---

## 🧹 Data Preprocessing

- Selected required columns  
- Handled missing values  
- Converted data types  
- Created new columns:
  - Income_Group  
  - Poverty  
  - Target  

---

## 📊 Exploratory Data Analysis

- Income distribution  
- Age vs Income  
- Education vs Income  
- Poverty analysis  

### 🔍 Key Insights:
- Higher education leads to higher income  
- Unemployment leads to lower income  
- Income varies across regions  

---

## 🤖 Machine Learning

- Model: Random Forest Classifier  
- Type: Supervised Learning  

### Input:
- Age, Education, Employment, State  

### Output:
- 0 → Low Income  
- 1 → High Income  

---

## 🌐 Flask Application

- User inputs:
  - Age  
  - Education  
  - Employment  
  - State  

- Output:
  - Predicted Income Category  

---

## 📊 Power BI Dashboard

Includes:

- Income Distribution  
- Poverty Rate  
- Age vs Income  
- Education vs Income  
- Regional Analysis  

---

## 🌍 SDG Alignment

This project supports:

### **SDG Goal 10 – Reduced Inequalities**

✔ Identifies income disparities  
✔ Analyzes economic gaps  
✔ Provides data-driven insights  

---

## 🔮 Future Improvements

- Add more features  
- Improve model accuracy  
- Use deep learning  
- Real-time data integration  

---

## 🛠️ Technologies Used

- Python  
- Pandas, NumPy  
- Scikit-learn  
- Flask  
- Power BI  
- Git & GitHub  

---

## ▶️ How to Run

```bash
pip install -r requirements.txt
python retrain.py
python app.py

📁 Project Structure
INEQUALITY_ANALYTICS_PROJECT/
│
├── app.py
├── retrain.py
├── auto_retrain.py
├── requirements.txt
├── Dockerfile
├── README.md

📌 Conclusion
Income inequality analyzed successfully
ML model predicts income category
Dashboard provides clear insights
Supports SDG Goal 10

🙌 Author
Parimala.S
