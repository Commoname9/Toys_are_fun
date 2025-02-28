import streamlit as st
import pandas as pd
import requests
import msal  # Microsoft Authentication Library

# Microsoft Graph API Credentials
CLIENT_ID = "your-client-id"
CLIENT_SECRET = "your-client-secret"
TENANT_ID = "your-tenant-id"
AUTHORITY = f"https://login.microsoftonline.com/{TENANT_ID}"
SCOPES = ["https://graph.microsoft.com/.default"]
EXCEL_FILE_PATH = "/drives/{drive-id}/items/{item-id}/workbook/worksheets('Sheet1')/range(address='A1:Z1000')"

# Authenticate & Get Access Token
def get_access_token():
    app = msal.ConfidentialClientApplication(CLIENT_ID, authority=AUTHORITY, client_credential=CLIENT_SECRET)
    token = app.acquire_token_for_client(SCOPES)
    return token["access_token"]

# Fetch Excel Data from OneDrive/SharePoint
def fetch_excel_data():
    access_token = get_access_token()
    url = f"https://graph.microsoft.com/v1.0/me/drive/root:/YourExcelFile.xlsx:/workbook/worksheets('Sheet1')/usedRange"
    
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        values = data.get("values", [])
        return pd.DataFrame(values[1:], columns=values[0])  # Convert to Pandas DataFrame
    else:
        st.error("Failed to fetch data from Excel Online.")
        return pd.DataFrame()

# Streamlit UI
st.title("Product Data from Excel Online (SSO)")

if st.button("Load Data"):
    df = fetch_excel_data()
    st.dataframe(df)
    def update_excel_online(df):
    access_token = get_access_token()
    url = https://daveandbusters0.sharepoint.com/:x:/s/RedemptionTeam/Ef7HTixT2BpGtdWm62GXD0UBrtJhjXDzpNPo_v9G5tXuyQ?e=4%3AvJfxIi&fromShare=true&at=9&CID=b2737c76-f631-fb61-5c79-5638b59bf6c1('MASTER DATA')/range(address='A1:AF4000')"
    
    headers = {"Authorization": f"Bearer {access_token}", "Content-Type": "application/json"}
    payload = {"values": [df.columns.tolist()] + df.values.tolist()}
    
    response = requests.patch(url, headers=headers, json=payload)

    if response.status_code == 200:
        st.success("Excel data updated successfully!")
    else:
        st.error("Failed to update Excel Online.")

if st.button("Save Changes"):
    update_excel_online(df)

