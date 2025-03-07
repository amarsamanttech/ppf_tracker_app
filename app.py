# app.py
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from ppf_data import ppf_data
from data_processing import calculate_ppf_balance, project_ppf_balance, sample1, sample2, sample3, sample4, sample5, sample6, sample7
from datetime import date

# Theme selection in sidebar
st.sidebar.header("Theme")
theme = st.sidebar.selectbox("Choose Theme", ["Dark", "Light"])

# Define CSS for dark and light themes
# Define CSS for dark and light themes
if theme == "Dark":
    css = """
    <style>
    .stApp {
        background-color: #1E1E1E;
        color: #D3D3D3;
    }
    [data-testid="stSidebar"] {
        background-color: #2A2A2A;
        color: #D3D3D3;
        border-right: 2px solid #00FFFF;
    }
    [data-testid="stSidebar"] .css-1d391kg, [data-testid="stSidebar"] * {
        color: #D3D3D3;
    }
    h1, h2, h3 {
        color: #00FFFF;
        text-shadow: 0 0 5px #00FFFF;
    }
    .stButton>button {
        background: linear-gradient(45deg, #FF00FF, #00FFFF);
        color: #1E1E1E;
        border: none;
        border-radius: 10px;
        box-shadow: 0 0 10px #FF00FF;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background: linear-gradient(45deg, #00FF00, #FF00FF);
        box-shadow: 0 0 15px #00FF00;
    }
    [data-testid="stSidebar"] .stButton>button {
        background: linear-gradient(45deg, #FF00FF, #00FFFF);
        color: #1E1E1E;
        border: none;
        border-radius: 10px;
        box-shadow: 0 0 10px #FF00FF;
        transition: all 0.3s ease;
    }
    [data-testid="stSidebar"] .stButton>button:hover {
        background: linear-gradient(45deg, #00FF00, #FF00FF);
        box-shadow: 0 0 15px #00FF00;
    }
    [data-testid="stSidebar"] .stButton>button[label="Download Template"] {
        background-color: #00FFFF;
        color: #1E1E1E;
        font-weight: bold;
        border: 2px solid #FF00FF;
        border-radius: 12px;
        box-shadow: 0 0 12px #00FFFF, 0 0 20px #FF00FF;
        padding: 5px 10px;
        transition: all 0.3s ease;
    }
    [data-testid="stSidebar"] .stButton>button[label="Download Template"]:hover {
        background-color: #FF00FF;
        border: 2px solid #00FFFF;
        box-shadow: 0 0 15px #FF00FF, 0 0 25px #00FFFF;
    }
    .stSlider > div > div > div > div {
        background-color: #00FFFF;
        border-radius: 5px;
    }
    .stNumberInput > div > input {
        background-color: #3A3A3A;
        color: #D3D3D3;
        border: 2px solid #00FFFF;
        border-radius: 8px;
        box-shadow: 0 0 5px #00FFFF;
        transition: box-shadow 0.3s ease;
    }
    .stNumberInput > div > input:hover {
        box-shadow: 0 0 10px #00FFFF;
    }
    .stRadio > label {
        color: #D3D3D3;
        background-color: #3A3A3A;
        padding: 5px 10px;
        border-radius: 5px;
        margin: 2px 0;
    }
    .stRadio > label:hover {
        background-color: #4A4A4A;
        box-shadow: 0 0 5px #FF00FF;
    }
    .stSelectbox > div > div {
        background-color: #3A3A3A;
        color: #D3D3D3;
        border: 2px solid #00FFFF;
        border-radius: 8px;
        box-shadow: 0 0 5px #00FFFF;
    }
    .stFileUploader > div > div > button {
        background: linear-gradient(45deg, #FF00FF, #00FFFF);
        color: #1E1E1E;
        border: none;
        border-radius: 10px;
        box-shadow: 0 0 10px #FF00FF;
        transition: all 0.3s ease;
    }
    .stFileUploader > div > div > button:hover {
        background: linear-gradient(45deg, #00FF00, #FF00FF);
        box-shadow: 0 0 15px #00FF00;
    }
    /* Updated table styling for dark theme */
    [data-testid="stTable"] {
        background-color: #2A2A2A !important;
        color: #D3D3D3 !important;
        border: 1px solid #4A4A4A !important;
    }
    [data-testid="stTable"] table {
        background-color: #2A2A2A !important;
        color: #D3D3D3 !important;
        border-collapse: collapse !important;
    }
    [data-testid="stTable"] th {
        background-color: #3A3A3A !important;
        color: #00FFFF !important;
        border: 1px solid #4A4A4A !important;
        font-weight: bold;
    }
    [data-testid="stTable"] td {
        background-color: #2A2A2A !important;
        color: #D3D3D3 !important;
        border: 1px solid #4A4A4A !important;
    }
    </style>
    """
else:  # Light Theme
    css = """
    <style>
    .stApp {
        background-color: #FFFFFF;
        color: #333333;
    }
    [data-testid="stSidebar"] {
        background-color: #F0F0F0;
        color: #333333;
    }
    [data-testid="stSidebar"] .css-1d391kg, [data-testid="stSidebar"] * {
        color: #333333;
    }
    h1, h2, h3 {
        color: #FF00FF;
    }
    .stButton>button {
        background-color: #00FFFF;
        color: #333333;
        border: none;
    }
    .stButton>button:hover {
        background-color: #00FF00;
        color: #333333;
    }
    .stSlider > div > div > div > div {
        background-color: #FF00FF;
    }
    .stNumberInput > div > input {
        background-color: #F0F0F0;
        color: #333333;
        border: 1px solid #FF00FF;
    }
    /* Updated table styling for light theme */
    [data-testid="stTable"] {
        background-color: #F0F0F0 !important;
        color: #333333 !important;
        border: 1px solid #A0A0A0 !important;
    }
    [data-testid="stTable"] table {
        background-color: #F0F0F0 !important;
        color: #333333 !important;
        border-collapse: collapse !important;
    }
    [data-testid="stTable"] th {
        background-color: #E0E0E0 !important;
        color: #FF00FF !important;
        border: 1px solid #A0A0A0 !important;
        font-weight: bold;
    }
    [data-testid="stTable"] td {
        background-color: #F0F0F0 !important;
        color: #333333 !important;
        border: 1px solid #A0A0A0 !important;
    }
    </style>
    """
# Apply the selected theme
st.markdown(css, unsafe_allow_html=True)

st.title("PPF Investment Tracker")

# Sidebar for inputs
st.sidebar.header("Options")
data_option = st.sidebar.radio("Choose Data", ("Upload File", "Use Sample"))

# Download data template
template = pd.DataFrame([{"date": "2023-04-01", "amount": 10000}])
st.sidebar.download_button("Download Template", template.to_csv(index=False), "ppf_template.csv", "text/csv")

if data_option == "Upload File":
    uploaded_file = st.sidebar.file_uploader("Upload Excel/CSV", type=["csv", "xlsx"])
    if uploaded_file:
        investments = pd.read_csv(uploaded_file) if uploaded_file.name.endswith(".csv") else pd.read_excel(uploaded_file)
        if "date" in investments.columns and "amount" in investments.columns:
            investments["date"] = pd.to_datetime(investments["date"], errors='coerce')
        else:
            st.error("File must have 'date' and 'amount' columns.")
else:
    sample_choice = st.sidebar.selectbox("Select Sample", (
        "Investor since 2010 (Incremental)",
        "Investor since 2015 (Incremental)",
        "Investor since 2020 (Incremental)",
        "Max Investor since 2015 (₹1,50,000)",
        "Max Investor since 2018 (₹1,50,000)",
        "Max Investor since 2021 (₹1,50,000)",
        "Max Investor since 2006 (Variable Limits)"
    ))
    investments = {
        "Investor since 2010 (Incremental)": sample1,
        "Investor since 2015 (Incremental)": sample2,
        "Investor since 2020 (Incremental)": sample3,
        "Max Investor since 2015 (₹1,50,000)": sample4,
        "Max Investor since 2018 (₹1,50,000)": sample5,
        "Max Investor since 2021 (₹1,50,000)": sample6,
        "Max Investor since 2006 (Variable Limits)": sample7
    }[sample_choice]

# Projection settings
st.sidebar.header("Projection Settings")
projection_years = st.sidebar.slider("Years to Project", 1, 15, 5)
assumed_rate = st.sidebar.number_input("Assumed Interest Rate (%)", 0.0, 15.0, 7.1)
future_investment = st.sidebar.number_input("Annual Future Investment (₹)", 0, 150000, 0)

# Process data
if "investments" in locals():
    # Convert 'date' column to datetime
    investments['date'] = pd.to_datetime(investments['date'], errors='coerce')
    start_year = investments["date"].dt.year.min()
    end_year = date.today().year
    yearly_data = calculate_ppf_balance(investments, ppf_data, start_year, end_year)
    full_data = project_ppf_balance(yearly_data, projection_years, assumed_rate, future_investment)

    # Display table
    st.subheader("Yearly Investment Details")
    st.dataframe(full_data)

    # Create line graph with theme-adjusted colors
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=full_data["year"], y=full_data["invested"], mode="lines", name="Invested Value", line=dict(color="#FF00FF" )))
    fig.add_trace(go.Scatter(x=full_data["year"], y=full_data["balance"], mode="lines", name="Current Value", line=dict(color="#00FFFF" )))


    fig.update_layout(
        title="PPF Investment Growth",
        xaxis_title="Year",
        yaxis_title="Amount (₹)",
        plot_bgcolor="#1E1E1E" if theme == "Dark" else "#FFFFFF",
        paper_bgcolor="#1E1E1E" if theme == "Dark" else "#FFFFFF",
        font=dict(color="#D3D3D3" if theme == "Dark" else "#333333"),
        title_font_color="#D3D3D3" if theme == "Dark" else "#333333",
        legend_font_color="#D3D3D3" if theme == "Dark" else "#333333",
        xaxis=dict(
            gridcolor="#4A4A4A" if theme == "Dark" else "#A0A0A0",
        ),
        yaxis=dict(
            gridcolor="#4A4A4A" if theme == "Dark" else "#A0A0A0",
            showgrid=True
        )
    )
    st.plotly_chart(fig)

    # Download chart
    st.sidebar.download_button("Download Chart", fig.to_image(format="png"), "ppf_chart.png", "image/png")


