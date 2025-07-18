# 🎓 Admission Prediction – Machine Learning Project

This project focuses on predicting key metrics in a university admission dataset using various regression models. The workflow includes data visualization, preprocessing, training different types of models, and evaluating their performance.

---

## 📁 Dataset

The dataset used in this project contains records of students applying to graduate schools, with features such as:

- GRE Score  
- TOEFL Score  
- University Rating  
- SOP (Statement of Purpose)  
- LOR (Letter of Recommendation)  
- CGPA  
- Research  
- Chance of Admit (binary for logistic regression)

---

## 📊 1. Data Exploration

- Visualized distributions of each feature using histograms.
- Created pairplots to investigate pairwise correlations.
- Identified highly correlated features (e.g., CGPA & GRE Score).

---

## 📐 2. Linear Regression (Closed-form Solution)

We applied the **Normal Equation** for predicting `GRE Score`:

$$
\mathbf{w} = (X^T X)^{-1} X^T y
$$

- Feature matrix $X$: all variables except `GRE Score`  
- Target $y$: `GRE Score`  
- Evaluation: Mean Squared Error (MSE) on both training and test sets

---

## 🧠 3. Regularization: Ridge and Lasso Regression

We applied Ridge and Lasso to reduce overfitting and improve generalization:

- **Lasso Regression** minimizes:

$$
J(\mathbf{w}) = \frac{1}{2n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2 + \lambda \sum_{j=1}^{p} |\mathbf{w}_j|
$$

- **Ridge Regression** minimizes:

$$
J(\mathbf{w}) = \frac{1}{2n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2 + \lambda \sum_{j=1}^{p} \mathbf{w}_j^2
$$

- Compared performance for different $\lambda$ values  
- Visualized coefficient paths to understand feature selection

---

## ✅ 4. Logistic Regression for Admission Prediction

We modeled `Chance of Admit` (converted to binary: admit vs. not admit) using a custom implementation of **Logistic Regression** trained via Newton's Method.

The update rule is:

$$
\mathbf{w}_{\text{new}} = \mathbf{w} - (X^T R X)^{-1} X^T (h(\mathbf{w}) - y)
$$

Where:

- $h(\mathbf{w}) = \frac{1}{1 + e^{-X \mathbf{w}}}$ is the sigmoid function  
- $R$ is a diagonal matrix with $h(\mathbf{w}) (1 - h(\mathbf{w}))$

### Evaluation:

- Accuracy, precision, and recall were computed  
- Decision boundary and predicted probabilities were visualized

---

## 📈 Results Summary

| Model                 | Task                     | Evaluation Metric     |
|----------------------|--------------------------|------------------------|
| Linear Regression     | Predict GRE Score         | MSE (train & test)     |
| Lasso / Ridge         | Predict GRE Score         | MSE & weight sparsity  |
| Logistic Regression   | Predict Admission (binary)| Accuracy / Conf. Mat.  |

---

## 🛠️ Requirements

- Python 3.x  
- NumPy, Pandas, Matplotlib, Seaborn  
- scikit-learn  
- Jupyter Notebook  

---

## 🚀 How to Run

1. Clone the repository  
2. Open the `src/main.ipynb` file in Jupyter  
3. Execute the cells sequentially to reproduce all results

---

## 📌 Author

Mohammad Javad Moosavi  
Master’s student, Biomedical Engineering – Bioelectric  
University of Tehran  

---

## 📜 License

This project is for educational purposes as part of the Machine Learning course at University of Tehran.
