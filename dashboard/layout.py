from dash import dcc, html, Dash, Output, Input, State, callback
import dash
import dash_leaflet as dl
import dash_leaflet.express as dlx
import dash_bootstrap_components as dbc
import pandas as pd
from dash_extensions.javascript import arrow_function, assign

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



classes = [
 44892,
 65221,
 85550,
 105879,
 126207,
 146536,
 166865,
 187195]

colorscale = ['#FFEDA0', '#FED976', '#FEB24C', '#FD8D3C', '#FC4E2A', '#E31A1C']
style = dict(weight=2, opacity=1, color='white', dashArray='3', fillOpacity=0.7)
# Create colorbar.
ctg = ["{}+".format(cls, classes[i + 1]) for i, cls in enumerate(classes[:-1])] + ["{}+".format(classes[-1])]
colorbar = dlx.categorical_colorbar(categories=ctg, colorscale=colorscale, width=400, height=30, position="bottomleft")
# Geojson rendering logic, must be JavaScript as it is executed in clientside.
style_handle = assign("""function(feature, context){
    const {classes, colorscale, style, colorProp} = context.props.hideout;  // get props from hideout
    const value = feature.properties[colorProp];  // get value the determines the color
    for (let i = 0; i < classes.length; ++i) {
        if (value > classes[i]) {
            style.fillColor = colorscale[i];  // set the fill color according to the class
        }
    }
    return style;
}""")


kaart = dl.Map(
                    zoom=10,
                    center=[52.356789, 4.773006],
                    children=[
                    dl.TileLayer(),
                    colorbar,
                    dl.GeoJSON(url="/assets/buurten_od_emissies.geojson",
                    id="buurten",
                    options=dict(style=style_handle),  # how to style each polygon
                    zoomToBounds=True,  # when true, zooms to bounds when data changes (e.g. on load)
                    zoomToBoundsOnClick=True,  # when true, zooms to bounds of feature (e.g. polygon) on click
                    hoverStyle=arrow_function(dict(weight=5, color='#666', dashArray='')),  # style applied on hover
                    hideout=dict(colorscale=colorscale, classes=classes, style=style, colorProp="fijnstof_afstand"),
                    format="geojson"
                    )
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
