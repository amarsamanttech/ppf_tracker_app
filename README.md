# PPF Tracker App

The **PPF Tracker App** is a user-friendly tool designed to help individuals track their Public Provident Fund (PPF) investments. Built with [Streamlit](https://streamlit.io/) and Python, this app offers a range of features to simplify managing your PPF portfolio while providing insightful visualizations and projections.

## Features

- **Historical PPF Data**: Access interest rates and investment limits from 2006 to 2023.
- **Data Upload/Download**: Upload your investment data in Excel or CSV formats and download results.
- **Sample Data**: Explore preloaded investment scenarios for three different age groups.
- **Visualizations**: View interactive line graphs comparing invested amounts to current values.
- **Projections**: Estimate future PPF balances based on customizable settings.
- **Downloadable Charts**: Export visualizations as PNG images for easy sharing.

## Installation and Setup

To run the PPF Tracker App, ensure you have [Python](https://www.python.org/) installed on your machine. Follow these steps:

1. Clone this repository or download the project files:
   ```bash
   git clone https://github.com/yourusername/ppf-tracker-app.git
   ```
2. Navigate to the project directory:
   ```bash
   cd ppf-tracker-app
   ```
3. Install the required dependencies listed in `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```
4. Launch the app:
   ```bash
   streamlit run app.py
   ```
5. The app will automatically open in your default web browser.

## How to Use

1. **Choose Data Source**:
   - In the sidebar, decide whether to upload your own data or use a sample:
     - **Upload File**: Provide an Excel or CSV file with columns `date` (in `YYYY-MM-DD` format) and `amount` (e.g., `5000`).
     - **Use Sample**: Select from three preloaded scenarios representing different investment profiles.

2. **Projection Settings**:
   - Adjust the following parameters in the sidebar:
     - **Years to Project**: Number of years to forecast (e.g., 10).
     - **Assumed Interest Rate**: Estimated future interest rate (e.g., 7.1%).
     - **Annual Future Investment**: Yearly contribution amount (e.g., ₹1,50,000).

3. **View Results**:
   - A table will display yearly investment details.
   - An interactive line graph will show the growth of your PPF investment over time.

4. **Download Charts**:
   - Click the sidebar button to save the chart as a PNG, or use Plotly’s built-in tools for more export options.

## Project Structure

Here’s an overview of the key files in the project:

- **`app.py`**:  
  The main Streamlit app file containing the user interface and core logic. This file handles user inputs, data uploads, and displays results such as tables and interactive charts.

- **`ppf_data.py`**:  
  Stores historical PPF interest rates and investment limits from 2006 to 2024. The data is structured as a dictionary for easy access and updates.

- **`data_processing.py`**:  
  Contains the core calculations for the app, including:
  - Functions to compute PPF balances based on historical data.
  - Logic for projecting future PPF values.
  - Generation of sample investment data for different age groups.

- **`requirements.txt`**:  
  Lists all Python dependencies needed to run the app. Use `pip install -r requirements.txt` to install them.

This structure ensures the app is modular, maintainable, and easy to extend.

## App URL deployed on streamlit cloud
- **`App url`**: https://ppf-tracker-app.streamlit.app/

## Future Enhancements

The app is already packed with useful features, but here are some planned upgrades:

- **Interest Rate Prediction**:  
  Leverage AI and time series models (e.g., ARIMA) to forecast future interest rates based on historical trends.

- **Investment Optimization**:  
  Provide personalized contribution suggestions using regression or reinforcement learning to help users meet their financial goals.

These enhancements will make the app even more powerful, offering users smarter insights and recommendations.