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

---

## 📈 Evaluation Metrics

- **Precision@K**  
  Measures the proportion of relevant items in the top-K recommended list compared to all recommended items.

- **Recall@K**  
  Indicates how many of the relevant items are included in the top-K recommendations out of all relevant items for a user.

- **F1-Score**  
  Harmonic mean of Precision and Recall, balancing both accuracy and coverage.

- **NDCG@K (Normalized Discounted Cumulative Gain)**  
  Evaluates ranking quality by considering both the relevance and the position of items in the top-K list.

- **RMSE (Root Mean Square Error)**  
  Measures the square root of the average squared differences between predicted and actual ratings (lower is better).

- **MAE (Mean Absolute Error)**  
  Calculates the average absolute difference between predicted and actual ratings, giving a more interpretable error metric.


<p align="center">
  <img src="images/download.png" alt="Model Comparison using Precision@10, Recall@10, NDCG@10" width="500"><br>
  <em>Model Comparison using Precision@10, Recall@10, NDCG@10</em>
</p>

<p align="center">
  <img src="images/download(1).png" alt="Model Comparison using RMSE & MAE" width="500"><br>
  <em>Model Comparison using RMSE & MAE</em>
</p>

---
## 🔍 Model Improvement: LightGCN vs UltraGCN

To enhance recommendation performance, we compared **LightGCN** with **UltraGCN**:

| Aspect               | LightGCN                                  | UltraGCN                                              |
|----------------------|-------------------------------------------|------------------------------------------------------|
| Message Passing      | Multi-layer propagation (costly)         | Removed (simplifies computation)                    |
| Global Similarity    | Not considered                           | Added for better embedding quality                  |
| Efficiency           | Higher computation cost                  | Lower cost, faster training                         |
| Performance Metrics  | Good                                      | Improved Precision@K, Recall@K, NDCG, and RMSE/MAE |

![](images/Capture52.PNG)

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
