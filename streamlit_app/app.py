
import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
transactions_df = pd.read_csv('../data/transactions_aggregated.csv')
insurance_df = pd.read_csv('../data/insurance_aggregated.csv')
users_df = pd.read_csv('../data/users_aggregated.csv')

st.set_page_config(layout='wide')
st.title("📊 PhonePe Dashboard")

tab1, tab2, tab3 = st.tabs(["Transactions", "Insurance", "Users"])

with tab1:
    st.header("Transaction Overview")
    categories = transactions_df['name'].unique()
    selected_category = st.selectbox("Select Category", categories)

    filtered_df = transactions_df[transactions_df['name'] == selected_category]
    fig = px.line(filtered_df, x='from', y='amount', title=f'{selected_category} - Amount Over Time')
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Total Transaction Amount by Category")
    group = transactions_df.groupby('name')['amount'].sum().reset_index()
    fig2 = px.bar(group.sort_values(by='amount', ascending=False), x='name', y='amount', color='name')
    st.plotly_chart(fig2, use_container_width=True)

with tab2:
    st.header("Insurance Overview")
    fig3 = px.line(insurance_df, x='from', y='amount', title='Insurance Transaction Amount Over Time')
    st.plotly_chart(fig3, use_container_width=True)

    st.subheader("Insurance Transaction Count Over Time")
    fig4 = px.area(insurance_df, x='from', y='count')
    st.plotly_chart(fig4, use_container_width=True)

with tab3:
    st.header("User Device Analytics")
    brand_counts = users_df.groupby('brand')['count'].sum().reset_index().sort_values(by='count', ascending=False)
    fig5 = px.bar(brand_counts, x='brand', y='count', title="Total Users by Device Brand", color='brand')
    st.plotly_chart(fig5, use_container_width=True)
