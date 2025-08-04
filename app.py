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

import os

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8050))  # Render te asigna un puerto
    app.run(host='0.0.0.0', port=port, debug=True)

