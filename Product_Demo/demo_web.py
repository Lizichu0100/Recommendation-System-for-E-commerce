import streamlit as st
import pandas as pd

# Set page config
st.set_page_config(page_title="Amazon Recommendation", page_icon="🛍️", layout="wide")

# Load data
purchase_history = pd.read_csv('purchase_history.csv')
recommendations = pd.read_csv('recommendations.csv')

# UI
st.image("https://upload.wikimedia.org/wikipedia/commons/a/a9/Amazon_logo.svg", width=200)
st.title("🛒 Purchase History & Recommendation Using UltraGCN For Amazon Customers")

# Dropdown
reviewer_names = ['-- Select a Customer --'] + purchase_history['reviewerName'].dropna().unique().tolist()
selected_name = st.selectbox("Choose Customer:", reviewer_names, index=0)

# Display
if selected_name and selected_name != '-- Select a Customer --':
    reviewer_id = purchase_history[purchase_history['reviewerName'] == selected_name]['reviewerID'].values[0]
    
    st.subheader("🧾 Purchase History")
    purchases = purchase_history[purchase_history['reviewerID'] == reviewer_id][['category', 'title', 'brand', 'price']]
    if not purchases.empty:
        st.dataframe(purchases, use_container_width=True)
    else:
        st.write("No purchase history available.")

    st.subheader("✨ Recommendations Using UltraGCN")
    recs = recommendations[recommendations['reviewerID'] == reviewer_id][['category', 'title', 'brand', 'price']]
    if not recs.empty:
        st.dataframe(recs, use_container_width=True)
    else:
        st.write("No recommendations available.")
else:
    st.info("🔍 Please select a customer to view their purchase history and recommendations.")