# Naive Bayes Classifier on the Iris Dataset

This project implements a **Naive Bayes classifier from scratch** and applies it to the **Iris dataset** to classify two species of iris flowers based on two features. The project also includes a comparison with the `scikit-learn` implementation.

---

## 📌 Objective

To understand and implement a Gaussian Naive Bayes classifier without using machine learning libraries, visualize the decision boundaries, and evaluate its performance using confusion matrix and metrics such as accuracy and precision.

---

## 📁 Dataset

- **Source**: `sklearn.datasets.load_iris()`
- **Classes used**:  
  - *Iris-virginica*  
  - *Iris-versicolor*
- **Features used**:  
  - Petal Length (`petal length (cm)`)  
  - Petal Width (`petal width (cm)`)

---

## 🔍 Sections

### A) Theoretical Background

We explain two classifiers:

- **Optimal Bayes Classifier**:  
  A theoretical classifier that assumes full knowledge of the true underlying data distributions. It gives the lowest possible error (Bayes error), but it's often impractical due to the need for complete distributional information.

- **Naive Bayes Classifier**:  
  A simplification of Bayes classifier that assumes **conditional independence** between features. Despite this strong assumption, it often performs well in practice, especially with high-dimensional data.

**Why Naive Bayes?**
- Computationally efficient
- Works well with small datasets
- Easy to implement
- **Trade-off**: Accuracy may decrease due to incorrect independence assumption, but gain in simplicity and speed is often worth it.

---

### B) Data Visualization

We extract only the petal length and petal width of `virginica` and `versicolor`, and plot them using a 2D scatter plot for visual analysis.

---

### C) Implementation from Scratch

- Assumption: Gaussian distribution for each feature
- Steps:
  1. Compute mean and variance for each feature in each class
  2. Use the Gaussian PDF to compute class-conditional likelihoods
  3. Apply Bayes theorem to get posterior probabilities
  4. Assign the label with the higher posterior

✅ No ML libraries like `sklearn` are used in this part — fully manual implementation.

---

### D) Decision Boundary Visualization

We generate a 2D grid using `numpy.meshgrid`, evaluate the classifier on each point, and use `matplotlib.contourf` to visualize the decision boundary between classes.

---

### E) Evaluation

- **Confusion Matrix**  
- **Accuracy** = (TP + TN) / Total  
- **Precision** = TP / (TP + FP)

We analyze how well the model distinguishes between the two flower species.

---

### F) Comparison with scikit-learn

We re-implement the classifier using `sklearn.naive_bayes.GaussianNB` and compare:
- Accuracy
- Decision boundaries
- Confusion matrix

This shows how close our manual implementation is to a standard library.

---

## ▶️ How to Run

1. Install dependencies:

```bash
pip install matplotlib numpy scikit-learn
```
2. Run the main script:
```bash
python src/main.ipynb
```