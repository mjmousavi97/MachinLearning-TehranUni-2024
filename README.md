<p align="center">
  <img src="images/gear.png" alt="Gear" width="200"/>
  &nbsp;&nbsp;&nbsp;
  <img src="images/images.png" alt="Banner" width="200"/>
</p>

# 🧠 Machine Learning Projects – University of Tehran

This repository contains a collection of machine learning projects I completed during the Fall 2024 semester at the **School of Electrical and Computer Engineering**, **University of Tehran**.

- 🎓 **Course**: Machine Learning  
- 📅 **Semester**: Spring 2024  
- 👨‍🏫 **Instructors**: 
  - [Dr. Babak N Araabi – Google Scholar](https://scholar.google.com/citations?hl=en&user=FTcata0AAAAJ)
  - [Dr. Mohammad-Reza A. Dehaqani – Google Scholar](https://scholar.google.com/citations?user=HuMGDxIAAAAJ&hl=en)
 
- 🏆 **Final Grade**: 19.75 / 20

---
 ## 📚 Projects

This repository is a growing collection of my machine learning projects.  
So far, I have completed and uploaded the following projects:

| # | Project Title                              | Description                                                                                     | Status       |
|---|-------------------------------------------|-------------------------------------------------------------------------------------------------|--------------|
| 1 | Apple vs Banana Image Classification      | Extracted features (mean intensity and channel intensity ratio) from apple and banana images, performed preprocessing, and classified them using simple threshold-based rules (without ML models). | ✅ Completed |
| 2 | Naive Bayes Classifier (Manual vs. Library) | Implemented Naive Bayes from scratch to separate two classes and compared it with sklearn's implementation. | ✅ Completed |
| 3 | Polynomial Regression Cross-Validation Simulation | Simulated data to analyze the impact of polynomial degree (1 to 25) on model performance using 10-fold cross-validation, computed mean & variance of MSE, and visualized bias-variance trade-off. | ✅ Completed |
| 4 | PDF Estimation Using Histogram, Parzen, and KNN | Estimated the probability density function (PDF) of a 1D dataset using three different non-parametric methods: manual Histogram, Parzen window (with Gaussian kernel), and K-Nearest Neighbors. Visualized and compared their behavior for various parameter settings. | ✅ Completed |
| 5 | KNN Classification on Synthetic Data      | Simulated uniform data for two classes (balanced and imbalanced), evaluated KNN with varying `k` and Euclidean/Cosine distances, analyzed impact of Gaussian noise and class imbalance. | ✅ Completed |
| 6 | Regression and Classification on Admission Data | Applied Linear Regression (normal equation), Lasso and Ridge regularization, and Logistic Regression (using Newton's method) to predict GRE scores and admission outcomes. Included visualization and evaluation (MSE, accuracy, confusion matrix). | ✅ Completed |
| 7 | Feature Selection and PCA on TinyMNIST Dataset | Performed PCA from scratch (manual covariance matrix and eigendecomposition), applied Forward and Backward feature selection to reduce dimensionality and improve classification performance on TinyMNIST. | ✅ Completed |
| 8 | Hard Margin & Kernelized SVM with CVXPY | Implemented Hard Margin SVM using the primal formulation and Kernelized SVM with RBF kernel using the dual formulation. Used CVXPY for convex optimization, visualized decision boundaries and support vectors, and achieved 100% training accuracy on kernelized model. | ✅ Completed |

🚀 More projects will be added soon as I continue exploring new ML techniques and datasets.

---

## 🚀 Final Project – Speaker Identification and Gender Classification Using Audio Data

The final course project focused on **classifying both the gender and the identity of individuals using audio data**. Key highlights of the project:

- 🔉 **Audio Preprocessing**: Extracting MFCCs and normalization  
- 🧪 **Modeling**: Binary (gender) and multi-class (identity) classification  
- 🛠 **Algorithms Used**:  
  - Support Vector Machines (SVM)  
  - Multi-Layer Perceptron (MLP)  
  - K-Nearest Neighbors (KNN)  
- 📊 **Evaluation**: Accuracy, Confusion Matrix, Cross-validation  

The project successfully achieved high accuracy on both tasks using carefully extracted features and tuned models.

---


> Note: projects will be gradually uploaded and documented in this repository.

---
## ▶️ How to Run

To run a project:

```bash
cd project_folder/
python src/main.py