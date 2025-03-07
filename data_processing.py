# data_processing.py
import pandas as pd
from datetime import date
from ppf_data import ppf_data


def calculate_ppf_balance(investments, ppf_data, start_year, end_year):
    balance = 0
    cumulative_invested = 0
    yearly_data = []

    for year in range(start_year, end_year + 1):
        year_investments = investments[investments["date"].dt.year == year]["amount"].sum()
        if year_investments > ppf_data[year]["limit"]:
            year_investments = ppf_data[year]["limit"]  # Cap at annual limit
        balance += year_investments
        cumulative_invested += year_investments
        interest_rate = ppf_data[year]["interest_rate"]  # Fetch interest rate for the year
        interest = balance * (interest_rate / 100)
        balance += interest
        yearly_data.append({
            "year": year,
            "invested": cumulative_invested,
            "interest_rate": interest_rate,  # Add interest rate to data
            "balance": balance
        })
    return pd.DataFrame(yearly_data)


def project_ppf_balance(yearly_data, projection_years, assumed_rate, annual_investment):
    last_year = yearly_data["year"].max()
    last_balance = yearly_data["balance"].iloc[-1]
    last_invested = yearly_data["invested"].iloc[-1]

    for year in range(last_year + 1, last_year + projection_years + 1):
        balance = last_balance + annual_investment
        invested = last_invested + annual_investment
        interest = balance * (assumed_rate / 100)
        balance += interest
        yearly_data = pd.concat([yearly_data, pd.DataFrame([{
            "year": year,
            "invested": invested,
            "interest_rate": assumed_rate,  # Use assumed rate for projections
            "balance": balance
        }])], ignore_index=True)
        last_balance = balance
        last_invested = invested
    return yearly_data


def generate_sample(start_year, initial_amount, growth_rate, end_year, fixed_amount=False, max_limit=False):
    investments = []
    amount = initial_amount
    for year in range(start_year, end_year + 1):
        if max_limit:
            # Use the maximum allowed limit for each year from ppf_data
            investments.append({"date": date(year, 4, 1), "amount": ppf_data[year]["limit"]})
        elif fixed_amount:
            investments.append({"date": date(year, 4, 1), "amount": initial_amount})
        else:
            investments.append({"date": date(year, 4, 1), "amount": amount})
            amount *= (1 + growth_rate)
    return pd.DataFrame(investments)


current_year = date.today().year

# Existing incremental samples
sample1 = generate_sample(2010, 5000, 0.10, current_year)
sample2 = generate_sample(2015, 10000, 0.05, current_year)
sample3 = generate_sample(2020, 15000, 0.03, current_year)

# New full-amount samples
sample4 = generate_sample(2015, 150000, 0, current_year, fixed_amount=True)
sample5 = generate_sample(2018, 150000, 0, current_year, fixed_amount=True)
sample6 = generate_sample(2021, 150000, 0, current_year, fixed_amount=True)

# New max-limit sample from 2006
sample7 = generate_sample(2006, 0, 0, current_year, max_limit=True)  # Max investor since 2006