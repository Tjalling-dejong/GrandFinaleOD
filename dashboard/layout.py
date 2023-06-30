from dash import dcc, html, Dash, Output, Input, State, callback
import dash
import dash_leaflet as dl
import dash_bootstrap_components as dbc
import pandas as pd

from styling import div_shadow


nav_bar = dbc.Navbar(
    [
        dbc.Row(
            [
                dbc.Col(
                    dbc.NavbarBrand(
                        "OD emissie dashboard",
                        style={"paddingLeft": "1rem", "fontWeight": "bold"},
                    ),
                    width=4,
                )
            ],
            justify="between",
            style={"width": "100%"},
        ),
    ],
    color="#080C80",
    # links_left=True,
    dark=True,
    style={
        "boxShadow": "0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgb(0 0 0 / 19%)",
        "padding": "1rem",
        # "width": "100%",
        "maxWidth": "100%",
    },
)


kaart = dl.Map(
                    zoom=10,
                    center=[52.356789, 4.773006],
                    children=[
                    dl.TileLayer(),
                    dl.GeoJSON(url="/assets/buurten_od.geojson" ,id="buurten")
                ],
                style={
                "width": "90%",
                "height": "70vh",
                "margin": "2rem",
                "padding": "1rem",
                "border": "2px solid black",
            },)




content = html.Div(
    [
        nav_bar,
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Container(
                            [
                                html.H5("Emissie informatie buurten"),
                                html.Hr(),
                                html.Div(id="buurt-info-div"),
                            ],
                            style=div_shadow(height="85vh"),
                        )
                    ],
                    width=4,
                    style={"padding": "1rem"},
                ),
                dbc.Col(
                    [
                        dbc.Container(
                            [
                                dbc.Container(
                                    [kaart
                                    ],
                                    style={"height": "80vh", "padding": "1rem"},
                                )
                            ],
                            style=div_shadow(height="85vh", marginTop="1rem"),
                        )
                    ],
                    width=8,
                ),
            ],
            justify="evenly",
            style={"margin": "auto"},
        ),
        
    ],
    # style=
    # div_shadow(
    #     height="95vh",
    #     margin="1rem",
    #     marginLeft="auto",
    #     marginRight="auto",
    #     display="block",
    # ),
    style={"maxHeight": "100vh", "maxWidth": "100%"},
)
