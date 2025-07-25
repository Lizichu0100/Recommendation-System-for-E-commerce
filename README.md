# 🛍️ Product Recommendation System for E-commerce Platform 🤖

A machine learning-based recommendation system designed to enhance user experience by suggesting relevant products for e-commerce platforms.

![](images/recommendation-system-Banner.png)

---
## 👥 Contributors


| Student ID  | Name                  | 
|-------------|-----------------------|
| 21280125    | Trần Thị Uyên Nhi    |
| 21280084    | Đặng Thị Kim Anh     |
| 21280109    | Phan Huy Thịnh       |

**Advisor:** TS. Trần Anh Tuấn

---

## 📌 Overview
This project focuses on building a **batch processing pipeline** for training and deploying product recommendation models based on **user behavior data** from the **Amazon Appliance Dataset**.

**Key Features:**
- Data preprocessing & feature engineering.
- Model training and evaluation with multiple recommendation algorithms.
- Top-K product recommendations for given users.
- Visualization and analysis of user-product interactions.

---

## 📊 Dataset
- **Source:** [Amazon Appliance Dataset (UCSD)](https://nijianmo.github.io/amazon/index.html)
- Includes:
  - `Appliances.json` (reviews)
  - `meta_Appliances.json` (metadata)

📂 [Download Raw Data from Google Drive](https://drive.google.com/drive/u/0/folders/131EYUUvpQ6qTQ3ay6__cKqkoEJaOqcgD)

---

## 🔍 Data Pipeline
**Main Flow:**  
`Data Extraction → Preprocessing → Model Training → Evaluation → Deployment`

**Visualization & EDA:**  
- Histograms, Pie Charts, Word Cloud
- Rating distribution, interaction density

![Data Pipeline](images/Capture51.PNG)

---

## 🧠 Models Implemented
- **Matrix Factorization (MF)**  
  Decomposes the user–item interaction matrix into latent factors to capture preferences and product features efficiently.

- **Neural Collaborative Filtering (NCF)**  
  Replaces the dot-product in MF with a neural network to model complex user–item interactions.

- **Multi-Layer Perceptron (MLP)**  
  Learns non-linear relationships between user and item embeddings using multiple fully connected layers.

- **LightGCN**  
  A graph-based recommendation model that propagates embeddings through user–item interaction graphs for improved accuracy.

**Improvement:**  
We further compared **LightGCN** with **UltraGCN**, which removes multi-layer message passing and introduces global similarity constraints, improving both accuracy and computational efficiency.

<p align="center">
  <img src="images/download.png" alt="Precision@10, Recall@10, NDCG@10" width="45%">
  <img src="images/download (1).png" alt="RMSE & MAE" width="45%">
</p>
<p align="center">
  <small><em>Model Comparison using Precision@10, Recall@10, NDCG@10</em></small> &nbsp;&nbsp;&nbsp;
  <small><em>Model Comparison using RMSE & MAE</em></small>
</p>

---

## 📈 Evaluation Metrics
- **Precision@K**
- **Recall@K**
- **F1-Score**
- **NDCG@K**

📷 **Suggested Image from Slide:** *Bar chart of Precision/Recall/NDCG*

---

## 🚀 Features
- Enter `user_id` → Get **Top 5 product recommendations**.
- Display user interaction history.
- Compare predicted vs actual interactions.

---

## 🏗️ Tech Stack
- **Python**, **Pandas**, **NumPy**, **Matplotlib**, **Seaborn**
- **PyTorch** (for GNN models)
- **Scikit-learn**
- **Google Colab** for training

---
