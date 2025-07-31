
import pandas as pd
import dash
from dash import dcc, html
import plotly.express as px

# Cargar datos RFM segmentados
rfm = pd.read_csv('rfm_clustered_customers.csv')

app = dash.Dash(__name__)
app.title = "Iberikus RFM Dashboard"

fig_rfm_scatter = px.scatter_3d(
    rfm, x='Recency', y='Frequency', z='Monetary',
    color='Cluster', title="Segmentos de Clientes (RFM en 3D)",
    color_discrete_sequence=px.colors.qualitative.Set2
)

fig_cluster_dist = px.histogram(
    rfm, x='Cluster', color='Cluster', title='Distribución de Clientes por Cluster',
    color_discrete_sequence=px.colors.qualitative.Set2
)

app.layout = html.Div([
    html.H1("Iberikus · RFM Customer Segmentation Dashboard", style={'textAlign': 'center'}),
    html.Div([
        html.Div([dcc.Graph(figure=fig_rfm_scatter)], className="six columns"),
        html.Div([dcc.Graph(figure=fig_cluster_dist)], className="six columns"),
    ], className="row"),
])

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=8080)
