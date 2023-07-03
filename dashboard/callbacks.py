from dash import Output, Input, State, callback, ALL, callback_context, html
import dash_leaflet as dl
from dash.exceptions import PreventUpdate

import dash_bootstrap_components as dbc


@callback(Output("buurt-info-div", "children"), Input("buurten", "click_feature"))
def get_clicked_buurt(clicked_feature):
    if clicked_feature:
        props = clicked_feature["properties"]
        children =[
            dbc.Row([dbc.Col("Buurt naam: "), dbc.Col(props["buurtnaam"])]),
            dbc.Row([dbc.Col("Buurt code: "), dbc.Col(props["buurtcode"])]),
            dbc.Row([dbc.Col("Gemeente naam: "), dbc.Col(props["gemeentenaam"])]),
            dbc.Row([dbc.Col("Fijnstof afstand: "), dbc.Col(props["fijnstof_afstand"])]),
            dbc.Row([dbc.Col("Aantal inwoners: "), dbc.Col(props["Aantal inwoners"])]),
            dbc.Row([dbc.Col("Gemiddeld gestandaardiseerd inkomen van huishoudens: "), dbc.Col(props["Gem gestandaardiseerd inkomen van huish"], align="end")]),
            dbc.Row([dbc.Col("Aantal laag opgeleiden: "), dbc.Col(props["Aantal laag opgeleiden"])]),
            dbc.Row([dbc.Col("Aantal middelbaar opgeleiden: "), dbc.Col(props["Aantal middelbaar opgeleiden"])]),
            dbc.Row([dbc.Col("Aantal hoog opgeleiden: "), dbc.Col(props["Aantal hoog opgeleiden"])]),
            html.Br(),
            html.H6("Ervaren gezondheidsscore"),
            dbc.Row([dbc.Col("Leeftijdscatagorie 18+"), dbc.Col(props["18 jaar of ouder"])]),
            dbc.Row([dbc.Col("Leeftijdscatagorie 18-65"), dbc.Col(props["18 - 65 jaar"])]),
            dbc.Row([dbc.Col("Leeftijdscatagorie 65+"), dbc.Col(props["65 jaar of ouder"])])
            

        ]
        return children
    raise PreventUpdate


@callback(Output("bedrijf-info-div", "children"), Input("bedrijven", "click_feature"))
def get_clicked_bedrijf(feature):
    if feature:
        props = feature["properties"]
        return [html.Hr(),dbc.Row(dbc.Label(props["bedrijf"]))]

