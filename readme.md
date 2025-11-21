# 📘 Insurance Charges Prediction using Linear Regression

This project predicts **medical insurance charges** based on a person’s age, BMI, number of children, and smoking status.  
A **Linear Regression** model is trained using the *insurance.csv* dataset and deployed using **Streamlit**.

---

## 📂 Project Structure
```text
Insurance_Prediction/
│── insurance.csv
│── model.sav
│── app.py
│── main.py (model training)
│── README.md
│── requirements.txt
```
---

## 🚀 Project Features

- Predicts **insurance charges** using:
  - Age  
  - BMI  
  - Number of children  
  - Smoker / Non-smoker  
- Shows detailed model performance:
  - R² Score  
  - Cross-Validated R²  
  - MSE / RMSE  
  - MAE  

---

## 📊 Final Model Performance

| Metric | Score |
|--------|-------|
| **R² Score (Test Set)** | 0.69 |
| **Cross-Validated R²** | 0.75 |
| **MSE (Test Set)** | 42,995,813.23 |
| **Average CV MSE** | 36,910,766.63 |
| **RMSE (Test Set)** | 6,557.12 |
| **Average CV RMSE** | 6,072.42 |
| **MAE (Test Set)** | 4,572.02 |
| **Average CV MAE** | 4,195.56 |

### ✔ Interpretation

- **Model explains 69% variance on test data**  
- **Cross-validation shows the model generalizes ~75%**, which is excellent  
- Average prediction error:
  - MAE: ~₹4,100–₹4,500  
  - RMSE: ~₹6,100–₹6,500  

---

## 🧠 Model Details

### Algorithm Used  
- **Linear Regression** (Sklearn)

### Preprocessing  
- Removed missing values  
- One-hot encoding for `smoker`  
- Train-test split (80%–20%)

---

## 🧾 Streamlit App Usage

Run the app:

```bash
streamlit run app.py
```

- Enter age, BMI, number of children, and smoker status
- Get predicted insurance charges
- See model accuracy in the app

## 📦 Requirements

The project requires the following Python packages:

```bash
pandas
streamlit
scikit-learn
pickle
```