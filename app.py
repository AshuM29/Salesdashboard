# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 00:42:17 2022

@author: Ashu Maheshwari
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(page_title="Oreon Sales Dashboard", page_icon=":bar_chart:", layout="wide")


df = pd.read_excel(r"F:\Oreon\oreonsales.xlsx")

st.sidebar.header("Please Filter Here:")

city=st.sidebar.multiselect(
    "select the City:",
    options=df["City"].unique(),
    default=df["City"].unique()
    )

Customer_type=st.sidebar.multiselect(
    "Select the Customer Type:",
    options=df["Customer_Type"].unique(),
    default=df["Customer_Type"].unique()
    )

gender=st.sidebar.multiselect(
    "Select the Gender:",
    options=df["Gender"].unique(),
    default=df["Gender"].unique()
    )

df_selection = df.query(
    "City == @city & Customer_Type == @Customer_type & Gender == @gender"
    )

st.title(":bar_chart: Sales Dashborad")
st.markdown("##")

total_sales=int(df_selection["Total"].sum())
average_rating=round(df_selection["Rating"].mean(), 1)
star_rating=":star:" * int(round(average_rating, 0))

average_sale_by_transaction=round(df_selection["Total"].mean(), 2)

left_column, middle_column, right_column = st.columns(3)
with left_column:
    st.subheader("Total Sales:")
    st.subheader(f"US $ {total_sales:}")
with middle_column:
    st.subheader("Average Rating:")
    st.subheader(f"{average_rating} {star_rating}")
                  
with right_column:
    st.subheader(("Average Sales Per Transaction:"))
    st.subheader(f"US $ {average_sale_by_transaction}")

st.markdown("---")                  


    
sales_by_product_line=(
    df_selection.groupby(by=["Product"]).sum()[["Total"]].sort_values(by="Total"))

fig_product_sales=px.bar(
    sales_by_product_line,
    x="Total",
    y=sales_by_product_line.index,
    orientation="h",
    title="<b>Sales By Product Line</b>",
    color_discrete_sequence=["#0083B8"] * len(sales_by_product_line),
    template="plotly_white"
    )

fig_product_sales.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
    )
    
st.plotly_chart(fig_product_sales)

sales_by_payment_type=(
    df_selection.groupby(by=["Payment"]).sum()[["Total"]].sort_values(by="Total"))

fig_payment_type=px.bar(
    sales_by_payment_type,
    x="Total",
    y=sales_by_payment_type.index,
    
    title="<b>Sales By Payment Type</b>",
    color_discrete_sequence=["#0083B8"] * len(sales_by_product_line),
    template="plotly_white"
    )

fig_payment_type.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
    )
    
st.plotly_chart(fig_payment_type)

