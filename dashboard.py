import streamlit as st
from reddit_scraper import get_top_products

st.title("Reddit Top Products Dashboard")

subreddit_name = st.text_input("Enter subreddit name:")
time_filter = st.selectbox("Select time period:", ['Month', 'Year', 'All Time'])

if st.button("Fetch Top Products"):
    top_products = get_top_products(subreddit_name, time_filter.lower())
    st.write(f"Top {len(top_products)} Products:")
    st.write(top_products)
