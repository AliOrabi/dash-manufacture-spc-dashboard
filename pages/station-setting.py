import os
import pathlib
import datetime
import dash
from dash import dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from dash import dash_table
import plotly.graph_objs as go
import dash_daq as daq

import pandas as pd



dash.register_page(__name__)