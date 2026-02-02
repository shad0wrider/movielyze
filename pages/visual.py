import streamlit as st
import plotly.express as fancyplot
import pandas as pd
import os


movieset = pd.read_csv("./dataset.csv")

genres = movieset["Genre"].drop_duplicates()


if st.selectbox("Select Genre",genres,key="genre_type"):
    genre_type = st.session_state.get("genre_type")

    comedy = movieset[movieset["Genre"] == genre_type]

    top_10 = comedy.sort_values(by=["Rating","Metascore","Votes"],ascending=False).head(10)

    bar = fancyplot.bar(data_frame=top_10,x="Title",y="Rating")

    st.subheader(f"Top 10 {genre_type} Movies by Rating")

    st.dataframe(top_10[["Rating", "Title"]])

    st.plotly_chart(bar)

    total_votes = top_10["Votes"].count()

    st.subheader(f"Top 10 {genre_type} Ordered by Votes")

    chart = fancyplot.pie(top_10,top_10["Title"],top_10["Votes"])

    st.plotly_chart(chart)





