import streamlit as st
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Google Sheets API Setup
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("your-credentials.json", scope)
client = gspread.authorize(creds)

# Open the Google Sheet (Replace with your sheet name)
SHEET_URL = "https://docs.google.com/spreadsheets/d/1OxgayjvbqRoMH7BOEcv62bcSieOKBE9ulQMfZYGos5U/edit"
spreadsheet = client.open_by_url(SHEET_URL)
sheet = spreadsheet.sheet1  # Access the first sheet

# Read data into a Pandas DataFrame
data = sheet.get_all_records()
df = pd.DataFrame(data)

# Streamlit UI
st.title("Product Data from Google Sheets")
st.write("Live product data from Google Sheets:")
st.dataframe(df)

# Allow user to add new product
st.subheader("Add New Product")
product_name = st.text_input("Product Name")
category = st.text_input("Category")
price = st.number_input("Price", min_value=0.01)

if st.button("Add Product"):
    sheet.append_row([product_name, category, price])
    st.success("Product added successfully!")

