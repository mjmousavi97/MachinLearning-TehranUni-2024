
# 📊 PDF Estimation Project: Histogram, Parzen Window, and K-Nearest Neighbors (KNN)

## 🎯 Objective
This project demonstrates how to estimate the **probability density function (PDF)** from 1000 samples drawn from a **uniform distribution $U(-1, 1)$**, using the following three methods:

1. **Histogram Estimation**  
2. **Parzen Window Estimation** with Gaussian kernel  
3. **K-Nearest Neighbors (KNN) Estimation** *(Coming soon)*

---

## 📌 Step A: Sample Generation 

We first generate **1000 samples** from a uniform distribution:

```python
samples = np.random.uniform(-1, 1, size=1000)
```
## 📉 Histogram-Based PDF Estimation

We estimated the PDF using a **manual histogram approach**:

- The data range \([-1, 1]\) is divided into $ \sqrt{n} $ bins.
- For each bin, we count how many samples fall inside.
- The estimated PDF for each bin is computed as:

$$
\hat{f}(x_i) = \frac{\text{count}_i}{n \cdot \Delta x}
$$

### Key Observations:
- The result is **blocky and discrete**.
- Sensitive to bin width ($\Delta x$):  
  - Small bins → noisy  
  - Large bins → oversmoothing  
- Although the true distribution is uniform, sampling noise creates fluctuations in the histogram.

---

## 📊 Step B: Parzen Window Estimation (Gaussian Kernel)

We estimate the PDF using the **Parzen window method** with a **Gaussian kernel**:

### Kernel formula:
$$
K(u) = \frac{1}{\sqrt{2\pi}} e^{-\frac{u^2}{2}}
$$

### Parzen Estimator:
$$
\hat{f}_h(x) = \frac{1}{n h} \sum_{i=1}^{n} K\left(\frac{x - x_i}{h}\right)
$$

### Bandwidths tested:
- $h = 0.1$
- $h = 0.5$
- $h = 1.0$
- $h = 2.0$

### 🧠 Observations:

| Bandwidth $h$ | Behavior |
|---------------|----------|
| 0.1 | High variance, overfitting |
| 0.5 | Best balance between detail and smoothness |
| 1.0 | Smoother, slight underfitting |
| 2.0 | Over-smoothed, detail lost |

📎 *See detailed analysis in `results_analysis.md`*

---

## 📉 Step C: Manual Histogram Estimation

We manually divide the data range into bins and count the number of samples per bin. This produces a blocky approximation of the PDF.

- Bin width: $\Delta x \approx 0.0645$
- Sensitive to bin count and alignment
- Less smooth than Parzen; shows random fluctuations

---

## 🚧 Step D: K-Nearest Neighbor Estimation (Upcoming)

In this step, we will implement **KNN-based PDF estimation** for the following values of $k$:
- $k = 1$
- $k = 5$
- $k = 20$
- $k = 50$

The method will compute local densities using:

$$
\hat{f}_k(x) = \frac{k}{n \cdot V(x)}
$$

Where $V(x)$ is the volume (interval length in 1D) required to capture the $k$ nearest neighbors of point $x$.

👉 **This section will be implemented next.**

---

## 📎 References

- Parzen, E. (1962). On Estimation of a Probability Density Function and Mode. *The Annals of Mathematical Statistics.*
- Bishop, C. M. (2006). *Pattern Recognition and Machine Learning.* Springer.
- Hastie, Tibshirani, Friedman (2009). *The Elements of Statistical Learning.*

---

## ✅ Summary

| Method | Type | Pros | Cons |
|--------|------|------|------|
| Histogram | Discrete | Simple | Blocky, sensitive to bin size |
| Parzen | Continuous | Smooth, tunable | Sensitive to bandwidth |
| KNN | Local Density | Adaptive to data | Still to be implemented |

---

## 📌 Run Instructions

```bash
# Install dependencies
pip install numpy matplotlib

# Run the Parzen estimation script
python src/main.py
```

---


Created by [ Mohammad Javad ], 2025  
Feel free to fork, star ⭐, or suggest improvements!
