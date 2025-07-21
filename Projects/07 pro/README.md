# Project 07

# 🧠 Feature Selection and Dimensionality Reduction on TinyMNIST Dataset

This project applies **feature selection** and **dimensionality reduction** techniques on the TinyMNIST dataset using:

- ✅ Principal Component Analysis (PCA)
- ✅ Forward Selection
- ✅ Backward Elimination

The goal is to reduce dimensionality while maintaining high classification performance using a **Naïve Bayes classifier**.

---

## 📂 Dataset

The dataset used is a small version of MNIST (TinyMNIST):

- `trainData.csv`: Training features  
- `trainLabels.csv`: Training labels  
- `testData.csv`: Testing features  
- `testLabels.csv`: Testing labels

Each image is flattened into a vector. Features are pixel intensities.

---

## 🧪 Algorithms Implemented

### 🔹 1. Principal Component Analysis (PCA)

**Goal:** Reduce dimensionality by finding orthogonal directions (principal components) that capture maximum variance.

**Steps:**
1. Center the data.
2. Compute the covariance matrix.
3. Perform eigen-decomposition.
4. Sort eigenvalues/eigenvectors in descending order.
5. Retain top-`k` eigenvectors that preserve 95% of variance.

📊 The explained variance is plotted to visualize how many components are required to retain 95% of information.

### 🔹 2. Forward Feature Selection

**Goal:** Start with no features and iteratively add the one that improves performance the most.

**Process:**
- Use `GaussianNB` for evaluation.
- Continue until no further improvement in CCR (Classification Correctness Rate).

### 🔹 3. Backward Feature Elimination

**Goal:** Start with all features and remove the one that least affects or improves the model.

**Process:**
- Evaluate accuracy by removing each feature.
- Eliminate the one whose removal increases or least reduces the CCR.
- Repeat until no improvements can be made.

---

## ⚙️ Dependencies

Install required packages using:

```bash
pip install numpy matplotlib scikit-learn
```

---

## 📊 Evaluation Metric

The classifier used is `Gaussian Naive Bayes (GNB)`, and the evaluation metric is **Accuracy (CCR)**.

---

## 📈 Results

- PCA retained ~95% of variance with only `62` components.
- Both forward and backward selection successfully identified a reduced feature set with similar or better CCR.
- Performance comparison of PCA vs. wrapper methods was plotted for analysis.

---

## 📌 Visualizations

- **Eigenvalue Spectrum** (PCA)
- **Cumulative Explained Variance**
- **CCR vs Number of Features** for Forward and Backward Selection

Example:

```python
plt.plot(range(1, len(forward_accuracies) + 1), forward_accuracies)
plt.xlabel('Number of Selected Features')
plt.ylabel('CCR')
```

---

## 🧪 How to Run

1. Place your dataset files in the same folder.
2. Run the Python script to execute PCA, forward selection, and backward elimination.
3. View results and plots.

---

## 📁 File Structure

```
07 pro/
│
├── data/
│   ├── trainData.csv
│   ├── trainLabels.csv
│   ├── testData.csv
│   └── testLabels.csv
├── src/
│   └── main.ipynb
├── images/
├── README.md             # This file
```

---

## ✍️ Author

- 👤 Mohammad Javad
- 📧 mj.mousavi@ut.ac.ir  
- 📍 [GitHub Profile](https://github.com/mjmousavi97)

---

## 📄 License

This project is licensed under the MIT License.
