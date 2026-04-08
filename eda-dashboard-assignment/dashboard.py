import streamlit as st
import matplotlib.pyplot as plt
from fetch_data import fetch_posts, clean_data, get_posts_per_user

st.title("📊 Simple Data Dashboard")

# Fetch and clean data
df = fetch_posts()
df = clean_data(df)

# Dataset preview
st.subheader("📄 Dataset Preview")
st.dataframe(df.head())

# Posts per user
st.subheader("📊 Posts per User")
posts_per_user = get_posts_per_user(df)

fig1, ax1 = plt.subplots()
ax1.bar(posts_per_user["user_id"], posts_per_user["post_count"])
ax1.set_xlabel("User ID")
ax1.set_ylabel("Number of Posts")
ax1.set_title("Posts per User")

st.pyplot(fig1)

# Post length distribution
st.subheader("📈 Post Length Distribution")

fig2, ax2 = plt.subplots()
ax2.hist(df["post_length"], bins=20)
ax2.set_xlabel("Post Length")
ax2.set_ylabel("Frequency")
ax2.set_title("Distribution of Post Length")

st.pyplot(fig2)