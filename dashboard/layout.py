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
                    zoom=11,
                    center=[52.479893, 4.748747],
                    children=[
                    dl.TileLayer()
                ],
                style={
                "width": "90%",
                "height": "70vh",
                "margin": "2rem",
                "padding": "1rem",
                "border": "2px solid black",
            },)


left_panel_tabs = dbc.Tabs(
    [
        dbc.Tab(
            [
                dbc.Label(
                    "Aggregatieniveau",
                    style={"fontStyle": "italic"},
                ),
                dcc.Dropdown(
                    options=[
                        {"label": "Subconditie", "value": 1},
                        {"label": "Hoofdconditie", "value": 2},
                        {"label": "Keten", "value": 3},
                    ],
                    id="aggregatie-niveau",
                    value=1,
                    clearable=False,
                    searchable=False,
                ),
                html.Br(),
                dbc.Container(
                    [
                        dcc.Checklist(
                            ["Maatregel pakket"],
                            inputStyle={"margin": "1rem"},
                            id="maatregel-check",
                        ),
                    ],
                    style={
                        "backgroundColor": "#eeeeee",
                        "padding": "1rem",
                    },
                ),
                html.Br(),
                dbc.Label("Grafiek configuratie", style={"fontWeight": "bold"}),
                html.Hr(),
                dbc.Label("Kleur op basis van: "),
                dcc.Dropdown(
                    options=[
                        {"label": "Subconditie", "value": "subconditie"},
                        {"label": "Hoofdconditie", "value": "hoofdconditie"},
                        {"label": "Keten", "value": "keten"},
                        {"label": "Categorie", "value": "categorie"},
                    ],
                    value="keten",
                    id="grafiek-kleur-groep",
                ),
            ],
            label="Configuratie",
        ),
        dbc.Tab(
            [
                dbc.Container(
                    [
                        dbc.Label(
                            "Versnellers en vertragers",
                            style={"fontWeight": "bold"},
                        ),
                        html.Br(),
                        dbc.Label("Subconditie", style={"fontStyle": "italic"}),
                        
                        html.Br(),
                        dbc.Label(
                            "calamiteit",
                            style={"fontStyle": "italic"},
                        ),
                        dcc.Slider(
                            -10,
                            10,
                            1,
                            value=0,
                            included=False,
                            id="calamiteit-slider",
                            marks={
                                10: {"label": "Vertragen"},
                                -10: {"label": "Versnellen"},
                            },
                            tooltip={
                                "placement": "bottom",
                                "always_visible": False,
                            },
                            disabled=True,
                        ),
                        dbc.Label(
                            "belangen",
                            style={"fontStyle": "italic"},
                        ),
                        dcc.Slider(
                            -10,
                            10,
                            1,
                            value=0,
                            included=False,
                            id="belangen-slider",
                            marks={
                                10: {"label": "Vertragen"},
                                -10: {"label": "Versnellen"},
                            },
                            disabled=True,
                            tooltip={
                                "placement": "bottom",
                                "always_visible": False,
                            },
                        ),
                        dbc.Label("trends", style={"fontStyle": "italic"}),
                        dcc.Slider(
                            -10,
                            10,
                            1,
                            value=0,
                            included=False,
                            id="trends-slider",
                            marks={
                                10: {"label": "Vertragen"},
                                -10: {"label": "Versnellen"},
                            },
                            tooltip={
                                "placement": "bottom",
                                "always_visible": False,
                            },
                            disabled=True,
                        ),
                        dbc.Label(
                            "middelen",
                            style={"fontStyle": "italic"},
                        ),
                        dcc.Slider(
                            -10,
                            10,
                            1,
                            value=0,
                            included=False,
                            id="middelen-slider",
                            marks={
                                10: {"label": "Vertragen"},
                                -10: {"label": "Versnellen"},
                            },
                            tooltip={
                                "placement": "bottom",
                                "always_visible": False,
                            },
                            disabled=True,
                        ),
                    ],
                    style={
                        "backgroundColor": "#eeeeee",
                        "padding": "1rem",
                    },
                ),
                dbc.Button(
                    "Reset",
                    id="reset-button",
                    style={
                        "margin": "1rem",
                        "backgroundColor": "#080C80",
                        "borderColor": "#080C80",
                    },
                ),
            ],
            label="Maatregelen",
        ),
    ]
)


content = html.Div(
    [
        nav_bar,
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Container(
                            [
                                html.H5("Conditionele ketens in Transformatiepaden"),
                                html.Hr(),
                                left_panel_tabs,
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
