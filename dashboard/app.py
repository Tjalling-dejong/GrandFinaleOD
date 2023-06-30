from dash import dcc, html, Dash, Output, Input, State, callback
import dash
import dash_bootstrap_components as dbc

from layout import content
    

app = Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    assets_folder="../assets",
    title="OD Emissies Dashboard"

)

app.config.suppress_callback_exceptions = True

app.layout = content
app.title = "OD emissie dashboard"

if __name__ == "__main__":
    app.run_server(debug=True)


