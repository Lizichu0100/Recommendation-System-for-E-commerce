# 🛍️ Product Recommendation System for E-commerce Platform 🤖

A machine learning-based recommendation system designed to enhance user experience by suggesting relevant products for e-commerce platforms.

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

📷 **Suggested Image from Slide:** *Pipeline diagram* (Slide: "DATA PIPELINE")

---

## 🧠 Models Implemented
- **Matrix Factorization (MF)**
- **Neural Collaborative Filtering (NCF) / MLP**
- **LightGCN**
- **UltraGCN (improved version)**

📷 **Suggested Image from Slide:** *UltraGCN vs LightGCN comparison chart*

---

## 📈 Evaluation Metrics
- **Precision@K**
- **Recall@K**
- **F1-Score**
- **NDCG@K**

📷 **Suggested Image from Slide:** *Bar chart of Precision/Recall/NDCG*

---

## 🚀 Features
- Enter `user_id` → Get **Top-K product recommendations**.
- Display user interaction history.
- Compare predicted vs actual interactions.

---

## 🏗️ Tech Stack
- **Python**, **Pandas**, **NumPy**, **Matplotlib**, **Seaborn**
- **PyTorch** (for GNN models)
- **Scikit-learn**
- **Google Colab** for training

---
