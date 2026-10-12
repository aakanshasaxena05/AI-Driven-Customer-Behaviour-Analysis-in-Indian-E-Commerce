# 🛒 Indian E-Commerce Customer Behavior Analysis

An end-to-end data analytics project that analyzes customer browsing and purchasing behavior on an Indian e-commerce platform using **Python, SQL, and Power BI**.

The project follows a complete analytics workflow:

**Data Cleaning → SQL Analysis → Exploratory Data Analysis (EDA) → Interactive Power BI Dashboard**

## 📌 Project Overview

E-commerce businesses can lose potential revenue when visitors fail to purchase products or abandon their shopping carts before checkout.

This project analyzes **3,000 customer browsing sessions** to understand customer purchasing patterns, evaluate business performance, and identify opportunities to improve conversions and revenue.

### 🎯 Business Objectives

- Analyze revenue trends and overall business KPIs.
- Identify the highest-performing product categories and states.
- Evaluate device and marketing channel performance.
- Understand customer payment preferences.
- Analyze cart abandonment and conversion behavior.
- Generate actionable business insights using interactive dashboards.

## ❓ Business Questions

1. What are the total revenue, total orders, average order value (AOV), conversion rate, and cart abandonment rate?
2. Which product categories generate the highest revenue?
3. Which Indian states contribute the most to sales?
4. How does revenue change over time?
5. Which devices and marketing channels perform best?
6. Which payment methods are most popular?
7. What percentage of sessions result in purchases, cart abandonment, or no action?

## 📂 Dataset Information

| Metric | Description |
|---|---|
| Total Rows | 3,000 |
| Total Columns | 20 |
| Data Grain | One row per browsing session |
| Period | January 2024 – December 2025 |
| Missing Values | Reported in the rating column |
| Duplicate Records | None reported |

**Dataset includes:**
- Customer demographics
- Device and browsing information
- Marketing channels
- Product categories
- Discounts and pricing
- Purchase and revenue information
- Payment methods
- Session engagement metrics

> Note: The dataset statistics above are based on the project's current analysis and should be verified against the final cleaned dataset.

## 🛠️ Tech Stack

| Category | Tools |
|---|---|
| Programming | Python |
| Data Manipulation | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn |
| Statistical Analysis | SciPy |
| Database | MySQL, SQLite |
| Business Intelligence | Power BI Desktop |
| Development Environment | Jupyter Notebook |

## 🔄 Project Workflow

```text
Raw CSV Dataset
       |
       v
01_data_cleaning.ipynb
       |
       v
02_sql_analysis.ipynb
       |
       v
03_eda.ipynb
       |
       v
Power BI Dashboard
       |
       v
Business Insights & Recommendations
```

### Key Deliverables

- Cleaned and treated datasets
- SQL queries for business analysis
- KPI calculations and reports
- Exploratory data analysis visualizations
- Interactive Power BI dashboard

## 🧹 Data Cleaning

The data preparation process includes:

- Standardizing column names.
- Converting date columns into appropriate data types.
- Checking for duplicate records.
- Handling missing ratings.
- Performing data validity checks.
- Creating additional date-based features.
- Detecting potential outliers using the IQR method.
- Generating cleaned and treated datasets for analysis.

## 📊 SQL Analysis

SQL was used to answer business questions and calculate key performance indicators.

**Key analyses include:**

- Total Revenue
- Total Orders
- Average Order Value (AOV)
- Conversion Rate
- Cart Abandonment Rate
- Monthly Revenue Trends
- Revenue by Product Category
- Revenue by State
- Payment Method Analysis
- Device Performance Analysis

## 📈 Key Insights

### KPI Summary

| KPI | Value |
|---|---:|
| Sessions Analyzed | 3,000 |
| Total Revenue | ₹22.68 Lakh |
| Total Orders | 2,380 |
| Average Order Value | ₹953 |
| Conversion Rate | 79.33% |
| Cart Abandonment Rate | 24.77% |

### Business Findings

- **Top Category:** Fashion generated the highest revenue.
- **Top State:** Maharashtra contributed the highest revenue.
- **Device Performance:** Mobile devices accounted for the majority of traffic.
- **Payment Preference:** UPI was the most preferred payment method.
- **Marketing Performance:** Paid Search recorded the highest conversion rate.
- **Cart Abandonment:** Approximately one in four sessions resulted in cart abandonment.
- **Revenue Distribution:** Revenue was heavily right-skewed, indicating that a relatively small number of high-value purchases contributed significantly to total revenue.

*These findings should be validated against the final dataset and KPI definitions before publication.*

## 📊 Power BI Dashboard

<img width="1132" height="752" alt="Ecommerce dashboard" src="https://github.com/user-attachments/assets/6a4e47bf-903c-4f6e-a70d-bc99523701a8" />


### Recommended Dashboard Components

- KPI cards for revenue, orders, AOV, conversion, and cart abandonment
- Monthly revenue trend
- Revenue by product category
- State-wise revenue analysis
- Payment method distribution
- Device and marketing channel analysis
- Customer segmentation
- Interactive slicers for dates, categories, states, and devices

### Dashboard Preview

Add your Power BI screenshots here after uploading them to your GitHub repository.

Example:

```markdown
![E-Commerce Dashboard](images/ecommerce_dashboard.png)
```

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/aakanshasaxena05/AI-Driven-Customer-Behaviour-Analysis-in-Indian-E-Commerce.git
```

```bash
cd AI-Driven-Customer-Behaviour-Analysis-in-Indian-E-Commerce
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Environment

**Windows PowerShell:**

```powershell
.\venv\Scripts\Activate.ps1
```

**Windows Command Prompt:**

```cmd
venv\Scripts\activate.bat
```

**macOS/Linux:**

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### 5. Run the Project

Open Jupyter Notebook and execute the notebooks in the following order:

1. `01_data_cleaning.ipynb`
2. `02_sql_analysis.ipynb`
3. `03_eda.ipynb`

Configure your database credentials in `config.py` before running the MySQL analysis notebook.

Finally, open `ecommerce_dashboard.pbix` using Power BI Desktop to explore the dashboard.

## 🔮 Future Improvements

- Customer segmentation using RFM analysis
- Statistical significance testing
- Conversion prediction models
- Cart abandonment prediction
- Cohort and customer retention analysis
- Advanced SQL using CTEs and window functions
- Dashboard publishing through Power BI Service

## 👤 Author

**Aakansha Saxena**

- **GitHub:** [aakanshasaxena05](https://github.com/aakanshasaxena05)
- **LinkedIn:** [Aakansha Saxena](https://www.linkedin.com/in/aakansha-saxena-23a370317/)


⭐ If you find this project useful, consider giving the repository a star.

*Built to demonstrate practical skills in data cleaning, SQL analytics, exploratory data analysis, and business intelligence.*
