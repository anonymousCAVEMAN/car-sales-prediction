# 🚗 Car Sales Prediction - Data Science Project

Welcome to the **Car Sales Prediction Project**! 🚀 This project aims to predict the sale price of used cars using **Linear Regression** and advanced regression techniques. We ensure robust analysis by performing extensive EDA, outlier detection, and assumption checks.

---

## 🧰 Project Structure
```
📂 project-root/
├── 📁 artifacts/         # pickels files
├── 📁 data/              # Dataset directory
├── 📁 reserch/            # Trained models
├── 📁 templates/         # html pages for Flask
├── 📁 src/               # Source code for ML pipeline
│   ├── dbfeeder.py       # Data ingestion & preprocessing
│   ├── train.py          # Model training (Linear, Ridge, Lasso, ElasticNet)
│   ├── inference.py      # Inference and prediction
│   └── api.py            # FastAPI integration
├── 📁 reports/           # Model performance reports
└── README.md             # You're here!
```

---

## 🔍 Key Features
- **Car Price Prediction** – Estimate used car sales value with high precision.
- **Linear Regression Pipeline** – Basic to advanced regression models.
- **EDA and Outlier Detection** – Visualizations and anomaly detection.
- **Model Evaluation** – R2 Score, Multicollinearity checks, VIF scores.
- **Streamlit & FastAPI** – Interactive user dashboards and REST API.

---

## 📦 Requirements
```bash
pip install -r request.txt
```

---

## 🚀 Quickstart
1. **Clone the Repository**
   ```bash
   git clone https://github.com/username/car-sales-prediction.git
   cd car-sales-prediction
   ```
2. **Perform EDA**
   ```bash
   python reserch/eda.ipynb
   ```
3. **Launch Flask App**
   ```bash
 python app.py
   ```

---

## 📊 Model Performance
| Model                 | R2 Score  |
|-----------------------|-----------|
| Linear Regression     | 88%       |
| Ridge Regression      | 95%       |
| Lasso Regression      | 95%       |             
| Polynomial (2nd Order)| 93%       |             
| Polynomial (5th Order)| **95%**   |             

---

## 🧪 Assumptions & Analysis
- **No NaN Values** – The dataset is clean with no missing values.
- **Duplicates** – Some duplicate values exist but were retained to reflect real-world conditions.
- **Outliers** – Detected and removed where necessary to improve model performance.
- **Model Assumptions** – Checked for linearity, no autocorrelation, multicollinearity, and homoscedasticity.
- **Polynomial Regression** – Applied up to 5th order with ElasticNet to achieve optimal performance.

---

## 📜 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

## 📧 Contact
For questions or collaboration, reach out at [your-email@example.com](mailto:your-email@example.com).

