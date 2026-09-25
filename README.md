Customer Risk Analysis Dashboard

Project Overview

This project analyzes customer churn using the IBM Telco Customer Churn dataset. The data is cleaned and analyzed using Python, and the results are prepared for visualization in Power BI. The objective is to identify customer behavior, churn patterns, and business insights that can help improve customer retention.

Features

- Data cleaning and preprocessing
- Customer churn analysis
- KPI calculation (Total Customers, Churn Rate, Average Monthly Charges, Average Tenure)
- Charts for Contract Type, Internet Service, Payment Method, and Churn Distribution
- Power BI dashboard (in progress)

Dataset

- Dataset: IBM Telco Customer Churn Dataset
- Source: Kaggle
- Records: 7,043 customers
- Target Column: "Churn"

Tools & Technologies

- Python
- Pandas
- Matplotlib
- Power BI
- IBM watsonx

Project Structure

<escape>Customer-Risk-Analysis/
├── churn_analysis.py
├── requirements.txt
├── README.md
├── Customer_Churn_Report.docx
└── dashboard_data.csv</escape>

How to Run

1. Download the project files.

2. Install the required libraries:
   
   <escape>pip install -r requirements.txt</escape>

3. Run the Python file:
   
   <escape>python churn_analysis.py</escape>

Key Insights

- Churn Rate: 26.58%
- Month-to-month customers have higher churn.
- Long-term contracts improve customer retention.
- Internet service type influences customer churn.

Future Improvements

- Complete the Power BI dashboard.
- Add interactive filters and advanced visualizations.
- Improve customer churn prediction using machine learning.
