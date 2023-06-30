from dash import dcc, html, Dash, Output, Input, State, callback
import dash_bootstrap_components as dbc


def div_shadow(**kwargs):
    style_dict = {
        "margin": "auto",
        "width": "95%",
        "textAlign": "center",
        "display": "block",
        "padding": "0.5rem",
        "horizontalAlign": "center",
        "boxShadow": "0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgb(0 0 0 / 19%)",
    }
    if kwargs:
        style_dict.update(kwargs)
    return style_dict
