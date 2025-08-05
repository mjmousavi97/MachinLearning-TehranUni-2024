# 📊 KMeans Clustering with Silhouette Analysis

This project applies **KMeans clustering** to discover the optimal number of clusters in a dataset using the **Silhouette Score** as an evaluation metric. It uses both standard KMeans and `k-means++` initialization, and demonstrates the use of **Mahalanobis distance** for cluster quality evaluation.

---

## 📁 Project Structure

```
.
├── data/
│   └── dataset-Q6.csv          # Input dataset
├── src/
│   └── main.ipynb              # Jupyter Notebook containing analysis
└── README.md                   # Project documentation
```

---

## 🚀 Overview

1. The dataset is preprocessed and scaled.
2. KMeans clustering is applied across a range of cluster numbers (k = 2 to 10).
3. For each k, the **Silhouette Score** is calculated:
   - First using **Euclidean distance**
   - Then using **Mahalanobis distance**
4. A plot of silhouette scores is created to visualize clustering performance.
5. The optimal k is determined based on the maximum score.

---

## 📈 What is Silhouette Score?

Silhouette Score measures how well each data point fits into its assigned cluster, with values ranging from -1 to 1:

- **+1**: Point is well clustered
- **0**: Point lies on cluster boundary
- **-1**: Point may be in the wrong cluster

---

## 🧪 Mahalanobis vs. Euclidean Distance

| Metric         | Description                                                                 |
|----------------|------------------------------------------------------------------------------|
| Euclidean      | Straight-line distance between points; simple and fast                      |
| Mahalanobis    | Considers variable correlation and scaling; more robust in high dimensions  |

---

## 🧠 Requirements

To install necessary packages:

```bash
pip install -r requirements.txt
```

Example `requirements.txt`:

```
numpy
pandas
matplotlib
scikit-learn
```

---

## ✍️ Author

**Mohammad Javad Mousavi**  
[GitHub](https://github.com/mjmousavi97) • [LinkedIn](https://www.linkedin.com/in/mjmousavi97)

---

## 📜 License

This project is licensed under the MIT License.
