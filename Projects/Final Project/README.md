# Voice Classification Project 🎙️

This project was developed as part of the **Machine Learning course at the University of Tehran**.  
The goal is to classify audio recordings of participants in the class by **gender** using both classical machine learning algorithms and deep learning models.

---

## 📂 Dataset
The dataset consists of raw voice recordings collected from students of the course.

### Preprocessing Steps
1. **File renaming** → Fixed problematic file names using the `os` library (not included in repo).  
2. **Label correction** → Some files had incorrect labels, which were fixed.  
3. **Data cleaning** → Very weak/low-volume recordings were removed.  
4. **Bandpass filter** →  A **1st-order Butterworth band-pass filter** was applied to the audio signals. The cutoff frequencies were normalized with respect to the **Nyquist frequency** (half of the sampling rate), and the filter was applied using `filtfilt` to avoid phase shifts.

5. **Splitting** → The cleaned dataset was divided into:
   - 80% training  
   - 20% testing  

All audio data goes through a **preprocessing pipeline** before feature extraction.
### Preprocessed Data
After preprocessing and feature extraction, two main CSV files are stored in `data/preprocessed/`:

- **`df_combined.csv`** → Contains metadata and processed information for **56 participants** (28 female, 28 male). This file is mainly used for the **classification task**.  
- **`processed_features (1).csv`** → Contains the **extracted features** for each audio file after preprocessing.  


---

## 🎼 Feature Extraction
We extracted a wide range of features to capture spectral, temporal, and perceptual characteristics of the audio:

- **MFCCs (13 coefficients)**
- **Spectral Centroid**
- **Spectral Bandwidth**
- **Spectral Contrast**
- **Zero Crossing Rate**
- **Root Mean Square (RMS) Energy**  

Since the audio files had varying lengths for each participant, 24 features were initially extracted for each audio file. Then, we computed the **mean**, **standard deviation (std)**, and **maximum** of each feature, which resulted in a final set of **72 features** for each audio file.


---

## 🤖 Models Implemented

### Machine Learning Models
- **K-Nearest Neighbors (KNN)**  
- **Support Vector Machine (SVM)**   

### Deep Learning Models
- **Multi layer perseptron (MLP)**  

---

## 📊 Evaluation
The performance of each model was assessed using multiple metrics:
- **Accuracy**  
- **Precision**  
- **Recall**  
- **F1-Score**  

Additionally, **Confusion Matrices** were generated for all models to visualize classification performance.

---


## 🧑‍💻 Contributors
- Mohammad Javad Mousavi  
- Ali Farzadfar

---

## 📌 Notes
- The raw dataset is **not uploaded** due to privacy concerns.  

---

## 📖 License
This project is released under the MIT License.
