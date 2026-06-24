import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# =========================================
# PAGE CONFIG
# =========================================
st.set_page_config(page_title="Customer Segmentation Dashboard", layout="wide")
st.title("Customer Segmentation Dashboard")
st.markdown("Cluster-based customer analysis using K-Means")

# df loaded
df = pd.read_csv("frontend/segmentation_data/segmentation.csv")

# =========================================
# BASIC CLEANING
# =========================================
numeric_cols = ['Customer Age', 'Customer Satisfaction Rating']

for col in numeric_cols:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')

# Optional date conversion if needed later
if 'Date of Purchase' in df.columns:
    df['Date of Purchase'] = pd.to_datetime(df['Date of Purchase'], errors='coerce')

# =========================================
# SIDEBAR FILTER
# =========================================
st.sidebar.header("Filters")
selected_cluster = st.sidebar.selectbox(
    "Select Cluster",
    options=["All"] + sorted(df['Cluster'].unique().tolist())
)

if selected_cluster != "All":
    filtered_df = df[df['Cluster'] == selected_cluster].copy()
else:
    filtered_df = df.copy()

# =========================================
# KPI SECTION
# =========================================
st.subheader("Overall KPIs")

total_customers = len(filtered_df)
num_clusters = df['Cluster'].nunique()
avg_age = filtered_df['Customer Age'].mean()
avg_sat = filtered_df['Customer Satisfaction Rating'].mean()

top_ticket_type = filtered_df['Ticket Type'].mode()[0] if filtered_df['Ticket Type'].notna().sum() > 0 else "N/A"
top_product = filtered_df['Product Purchased'].mode()[0] if filtered_df['Product Purchased'].notna().sum() > 0 else "N/A"
top_priority = filtered_df['Ticket Priority'].mode()[0] if filtered_df['Ticket Priority'].notna().sum() > 0 else "N/A"
top_channel = filtered_df['Ticket Channel'].mode()[0] if filtered_df['Ticket Channel'].notna().sum() > 0 else "N/A"

c1, c2, c3, c4 = st.columns(4)
c1.metric("Total Customers", f"{total_customers:,}")
c2.metric("No. of Clusters", num_clusters)
c3.metric("Avg Age", f"{avg_age:.1f}")
c4.metric("Avg Satisfaction", f"{avg_sat:.2f}")

c5, c6, c7, c8 = st.columns(4)
c5.metric("Top Ticket Type", top_ticket_type)
c6.metric("Top Product", top_product)
c7.metric("Top Priority", top_priority)
c8.metric("Top Channel", top_channel)

st.markdown("---")

# =========================================
# CLUSTER SUMMARY TABLE
# =========================================
st.subheader("Cluster Summary Table")

def safe_mode(series):
    mode_val = series.mode()
    return mode_val.iloc[0] if len(mode_val) > 0 else "N/A"

cluster_summary = (
    df.groupby('Cluster')
      .agg(
          Customers=('Ticket ID', 'count'),
          Avg_Age=('Customer Age', 'mean'),
          Avg_Satisfaction=('Customer Satisfaction Rating', 'mean')
      )
      .reset_index()
)

cluster_summary['Customer_%'] = (cluster_summary['Customers'] / len(df) * 100).round(2)

dominant_ticket_type = df.groupby('Cluster')['Ticket Type'].agg(safe_mode).reset_index(name='Top Ticket Type')
dominant_priority = df.groupby('Cluster')['Ticket Priority'].agg(safe_mode).reset_index(name='Top Priority')
dominant_product = df.groupby('Cluster')['Product Purchased'].agg(safe_mode).reset_index(name='Top Product')
dominant_channel = df.groupby('Cluster')['Ticket Channel'].agg(safe_mode).reset_index(name='Top Channel')
dominant_status = df.groupby('Cluster')['Ticket Status'].agg(safe_mode).reset_index(name='Top Ticket Status')

cluster_summary = cluster_summary.merge(dominant_ticket_type, on='Cluster', how='left')
cluster_summary = cluster_summary.merge(dominant_priority, on='Cluster', how='left')
cluster_summary = cluster_summary.merge(dominant_product, on='Cluster', how='left')
cluster_summary = cluster_summary.merge(dominant_channel, on='Cluster', how='left')
cluster_summary = cluster_summary.merge(dominant_status, on='Cluster', how='left')

st.dataframe(cluster_summary, use_container_width=True)

st.markdown("---")

# =========================================
# PLOT 1: CLUSTER SIZE
# =========================================
st.subheader("1. Cluster Size Distribution")

cluster_counts = df['Cluster'].value_counts().sort_index().reset_index()
cluster_counts.columns = ['Cluster', 'Count']

fig_cluster_size = px.bar(
    cluster_counts,
    x='Cluster',
    y='Count',
    text='Count',
    title='Number of Customers in Each Cluster'
)
st.plotly_chart(fig_cluster_size, use_container_width=True)

# =========================================
# PLOT 2: AVG AGE BY CLUSTER
# =========================================
st.subheader("2. Average Age by Cluster")

age_cluster = df.groupby('Cluster', as_index=False)['Customer Age'].mean()

fig_age = px.bar(
    age_cluster,
    x='Cluster',
    y='Customer Age',
    text_auto='.2f',
    title='Average Customer Age by Cluster'
)
st.plotly_chart(fig_age, use_container_width=True)

# =========================================
# PLOT 3: AGE DISTRIBUTION BY CLUSTER
# =========================================
st.subheader("3. Age Distribution by Cluster")

fig_age_box = px.box(
    df,
    x='Cluster',
    y='Customer Age',
    color='Cluster',
    title='Customer Age Distribution Across Clusters'
)
st.plotly_chart(fig_age_box, use_container_width=True)

# =========================================
# PLOT 4: AVG SATISFACTION BY CLUSTER
# =========================================
st.subheader("4. Average Satisfaction by Cluster")

sat_cluster = df.groupby('Cluster', as_index=False)['Customer Satisfaction Rating'].mean()

fig_sat = px.bar(
    sat_cluster,
    x='Cluster',
    y='Customer Satisfaction Rating',
    text_auto='.2f',
    title='Average Satisfaction Rating by Cluster'
)
st.plotly_chart(fig_sat, use_container_width=True)

# =========================================
# PLOT 5: SATISFACTION DISTRIBUTION BY CLUSTER
# =========================================
st.subheader("5. Satisfaction Distribution by Cluster")

fig_sat_box = px.box(
    df,
    x='Cluster',
    y='Customer Satisfaction Rating',
    color='Cluster',
    title='Customer Satisfaction Distribution Across Clusters'
)
st.plotly_chart(fig_sat_box, use_container_width=True)

# =========================================
# PLOT 6: GENDER DISTRIBUTION BY CLUSTER
# =========================================
st.subheader("6. Gender Distribution by Cluster")

gender_cluster = (
    df.groupby(['Cluster', 'Customer Gender'])
      .size()
      .reset_index(name='Count')
)

fig_gender = px.bar(
    gender_cluster,
    x='Cluster',
    y='Count',
    color='Customer Gender',
    barmode='group',
    title='Customer Gender Distribution Across Clusters'
)
st.plotly_chart(fig_gender, use_container_width=True)

# =========================================
# PLOT 7: TICKET TYPE DISTRIBUTION BY CLUSTER
# =========================================
st.subheader("7. Ticket Type Distribution by Cluster")

ticket_type_cluster = (
    df.groupby(['Cluster', 'Ticket Type'])
      .size()
      .reset_index(name='Count')
)

fig_ticket_type = px.bar(
    ticket_type_cluster,
    x='Cluster',
    y='Count',
    color='Ticket Type',
    barmode='stack',
    title='Ticket Type Distribution Across Clusters'
)
st.plotly_chart(fig_ticket_type, use_container_width=True)

# =========================================
# PLOT 8: TICKET PRIORITY DISTRIBUTION BY CLUSTER
# =========================================
st.subheader("8. Ticket Priority Distribution by Cluster")

priority_cluster = (
    df.groupby(['Cluster', 'Ticket Priority'])
      .size()
      .reset_index(name='Count')
)

fig_priority = px.bar(
    priority_cluster,
    x='Cluster',
    y='Count',
    color='Ticket Priority',
    barmode='group',
    title='Ticket Priority Distribution Across Clusters'
)
st.plotly_chart(fig_priority, use_container_width=True)

# =========================================
# PLOT 9: TICKET STATUS DISTRIBUTION BY CLUSTER
# =========================================
st.subheader("9. Ticket Status Distribution by Cluster")

status_cluster = (
    df.groupby(['Cluster', 'Ticket Status'])
      .size()
      .reset_index(name='Count')
)

fig_status = px.bar(
    status_cluster,
    x='Cluster',
    y='Count',
    color='Ticket Status',
    barmode='stack',
    title='Ticket Status Distribution Across Clusters'
)
st.plotly_chart(fig_status, use_container_width=True)

# =========================================
# PLOT 10: PRODUCT PURCHASED BY CLUSTER
# =========================================
st.subheader("10. Product Purchased by Cluster")

product_cluster = (
    df.groupby(['Cluster', 'Product Purchased'])
      .size()
      .reset_index(name='Count')
)

fig_product = px.bar(
    product_cluster,
    x='Cluster',
    y='Count',
    color='Product Purchased',
    barmode='stack',
    title='Product Purchased Distribution Across Clusters'
)
st.plotly_chart(fig_product, use_container_width=True)

# =========================================
# PLOT 11: TICKET CHANNEL DISTRIBUTION BY CLUSTER
# =========================================
st.subheader("11. Ticket Channel Distribution by Cluster")

channel_cluster = (
    df.groupby(['Cluster', 'Ticket Channel'])
      .size()
      .reset_index(name='Count')
)

fig_channel = px.bar(
    channel_cluster,
    x='Cluster',
    y='Count',
    color='Ticket Channel',
    barmode='group',
    title='Ticket Channel Distribution Across Clusters'
)
st.plotly_chart(fig_channel, use_container_width=True)

# =========================================
# PLOT 12: CLUSTER PROFILE HEATMAP
# =========================================
st.subheader("12. Cluster Profiling Heatmap")

heatmap_df = df.groupby('Cluster')[[
    'Customer Age',
    'Customer Satisfaction Rating'
]].mean().copy()

heatmap_norm = (heatmap_df - heatmap_df.min()) / (heatmap_df.max() - heatmap_df.min())

fig_heatmap = px.imshow(
    heatmap_norm,
    text_auto=True,
    aspect='auto',
    title='Normalized Cluster Profile Heatmap'
)
st.plotly_chart(fig_heatmap, use_container_width=True)