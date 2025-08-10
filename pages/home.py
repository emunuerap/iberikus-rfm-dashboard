import dash
from dash import html
import dash_bootstrap_components as dbc
import pandas as pd
import os

# Load RFM data
rfm = pd.read_csv("data/rfm_clustered_customers_enhanced.csv")
# Calculate KPIs dynamically
TOTAL_CUSTOMERS = f"{rfm.shape[0]:,}"
AVG_MONETARY = f"€{rfm['Monetary'].mean():,.2f}"
TOP_CLUSTER= str(rfm.groupby('Cluster')['Monetary'].sum().idxmax())

# Color palette
PRIMARY_COLOR = "#3D5A40"
SECONDARY_COLOR = "#D8B08C"
BACKGROUND = "#F9F9F9"

dash.register_page(__name__, path="/")

layout = dbc.Container([

    # Header Section
    dbc.Row([
        dbc.Col([
            html.H1("Welcome to the Iberikus Data Insights Platform",
                    className="display-4",
                    style={"color": PRIMARY_COLOR, "fontWeight": "bold"}),
            html.P("Gain insights, discover trends, and understand your customers better.",
                   className="lead", style={"fontSize": "1.2rem"}),
            html.Hr(style={"borderTop": f"2px solid {PRIMARY_COLOR}", "width": "100px", "marginLeft": "0"}),
            dbc.Button("Go to RFM Dashboard", href="/rfm", color="success", size="lg", style={"marginTop": "1.5rem"})
        ], md=6, style={"paddingTop": "4rem"}),

        dbc.Col([
            html.Img(src="/assets/iberikus_logo.png", style={
                "width": "80%", "maxWidth": "300px", "marginTop": "3rem"
            })
        ], md=6, className="text-center")
    ], align="center"),

    html.Br(),

    # KPI Section
    dbc.Row([
        dbc.Col(dbc.Card([
            dbc.CardBody([
                html.H5("Total Customers", className="card-title"),
                html.H2(TOTAL_CUSTOMERS, className="card-text")
            ])
        ], color="primary", inverse=True), md=4),

        dbc.Col(dbc.Card([
            dbc.CardBody([
                html.H5("Avg. Monetary Value", className="card-title"),
                html.H2(AVG_MONETARY, className="card-text")
            ])
        ], color="secondary", inverse=True), md=4),

        dbc.Col(dbc.Card([
            dbc.CardBody([
                html.H5("Top Cluster", className="card-title"),
                html.H2(TOP_CLUSTER, className="card-text")
            ])
        ], color="info", inverse=True), md=4)
    ], style={"marginTop": "3rem"}),

    html.Br(),

    # Insights Section
    dbc.Row([
        dbc.Col([
            html.H4("Key Insights", style={"color": PRIMARY_COLOR}),
            html.Ul([
                html.Li("🔍 40% of revenue comes from 20% of high-value customers."),
                html.Li("📉 Cluster 3 shows signs of inactivity – consider re-engagement."),
                html.Li("🛒 Frequent buyers spend 3x more than occasional visitors."),
                html.Li("📍 Top spending regions: Madrid, Valencia, and Barcelona.")
            ], style={"fontSize": "1rem"})
        ])
    ], style={"marginTop": "2rem", "marginBottom": "4rem"})

], fluid=True, style={"backgroundColor": BACKGROUND, "paddingBottom": "4rem"})
