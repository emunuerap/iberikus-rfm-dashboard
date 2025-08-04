import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
import os

# Initialize the Dash app with Bootstrap theme and page support
app = dash.Dash(
    __name__,
    use_pages=True,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    suppress_callback_exceptions=True
)

server = app.server  # Required for deployment

# Main layout
app.layout = dbc.Container([
    dbc.NavbarSimple(
        brand="Iberikus Analytics Dashboard",
        brand_href="/",
        color="dark",
        dark=True,
        children=[
            dbc.NavItem(dbc.NavLink("Home", href="/")),
            dbc.NavItem(dbc.NavLink("RFM Dashboard", href="/rfm-dashboard")),
        ]
    ),
    html.Br(),
    dash.page_container  # This renders the content of each page
], fluid=True)

print(dash.page_registry)

if __name__ == '__main__':
    app.run(debug=True)
