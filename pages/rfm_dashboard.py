import dash
from dash import dcc, html, Input, Output, callback, dash_table
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

# Register this page with Dash Pages
dash.register_page(__name__, path="/rfm", name="RFM Dashboard")

# Load the dataset (update path as needed)
rfm = pd.read_csv("data/rfm_clustered_customers.csv")

# Branding colors
PRIMARY = "#8E2DE2"  # Purple
SECONDARY = "#4A00E0"  # Indigo

# App layout
def layout():
    return dbc.Container([
        html.H2("RFM Segmentation Dashboard", className="text-center my-4 text-primary"),

        # Filters
        dbc.Row([
            dbc.Col([
                html.Label("Select Cluster:"),
                dcc.Dropdown(
                    id="cluster-filter",
                    options=[{"label": str(c), "value": c} for c in sorted(rfm["Cluster"].unique())],
                    value=None,
                    placeholder="All Clusters",
                    clearable=True
                ),
            ], md=4),

            dbc.Col([
                html.Label("Select Frequency Range:"),
                dcc.RangeSlider(
                    id="frequency-slider",
                    min=rfm["Frequency"].min(),
                    max=rfm["Frequency"].max(),
                    value=[rfm["Frequency"].min(), rfm["Frequency"].max()],
                    marks=None,
                    tooltip={"always_visible": False, "placement": "bottom"},
                    step=1
                )
            ], md=8)
        ], className="mb-4"),

        # KPI Cards
        dbc.Row([
            dbc.Col(dbc.Card([
                dbc.CardBody([
                    html.H5("Total Customers", className="card-title text-white"),
                    html.H2(id="total-customers", className="card-text")
                ])
            ], color="primary", inverse=True), md=4),

            dbc.Col(dbc.Card([
                dbc.CardBody([
                    html.H5("Avg. Monetary Value", className="card-title text-white"),
                    html.H2(id="avg-monetary", className="card-text")
                ])
            ], color="secondary", inverse=True), md=4),

            dbc.Col(dbc.Card([
                dbc.CardBody([
                    html.H5("Avg. Frequency", className="card-title text-white"),
                    html.H2(id="avg-frequency", className="card-text")
                ])
            ], color="info", inverse=True), md=4)
        ], className="mb-5"),

        # Visualizations
        dbc.Row([
            dbc.Col(dcc.Graph(id="bar-segments"), md=6),
            dbc.Col(dcc.Graph(id="scatter-recency-monetary"), md=6)
        ]),

        html.Hr(),

        # RFM Table
        html.H4("Segmented Customers Table", className="my-3 text-primary"),
        dash_table.DataTable(
            id="rfm-table",
            columns=[{"name": i, "id": i} for i in rfm.columns],
            style_table={"overflowX": "auto"},
            style_cell={"textAlign": "left", "padding": "5px"},
            style_header={"backgroundColor": PRIMARY, "color": "white", "fontWeight": "bold"},
            page_size=10,
            filter_action="native",
            sort_action="native"
        )
    ], fluid=True)

# Callback for interactivity
@callback(
    [Output("bar-segments", "figure"),
     Output("scatter-recency-monetary", "figure"),
     Output("rfm-table", "data"),
     Output("total-customers", "children"),
     Output("avg-monetary", "children"),
     Output("avg-frequency", "children")],
    [Input("cluster-filter", "value"),
     Input("frequency-slider", "value")]
)
def update_dashboard(cluster, freq_range):
    filtered = rfm.copy()

    # Filter by cluster
    if cluster is not None:
        filtered = filtered[filtered["Cluster"] == cluster]

    # Filter by frequency
    filtered = filtered[(filtered["Frequency"] >= freq_range[0]) & (filtered["Frequency"] <= freq_range[1])]

    # KPI calculations
    total_customers = f"{filtered.shape[0]:,}"
    avg_monetary = f"€{filtered['Monetary'].mean():,.2f}"
    avg_frequency = f"{filtered['Frequency'].mean():.2f}"

    # Bar chart by segment
    fig_bar = px.histogram(
        filtered,
        x="Cluster",
        color="Cluster",
        title="Customer Distribution by Cluster",
        color_discrete_sequence=px.colors.qualitative.Set2
    )
    fig_bar.update_layout(margin=dict(t=40, b=0, l=0, r=0))

    # Scatter plot Recency vs Monetary
    fig_scatter = px.scatter(
        filtered,
        x="Recency",
        y="Monetary",
        color="Cluster",
        title="Recency vs Monetary Value",
        color_discrete_sequence=px.colors.qualitative.Set2,
        hover_data=["customer_id", "Frequency"]
    )
    fig_scatter.update_layout(margin=dict(t=40, b=0, l=0, r=0))

    return fig_bar, fig_scatter, filtered.to_dict("records"), total_customers, avg_monetary, avg_frequency
