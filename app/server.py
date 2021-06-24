from dash import Dash
from dash_bootstrap_components.themes import BOOTSTRAP
from os.path import dirname, join, realpath

# Get file directory
dir_path = join(dirname(realpath(__file__)), "..")

# Create app and set title to show on browser tab
app = Dash(
    __name__, external_stylesheets=[BOOTSTRAP], assets_folder=join(dir_path, "assets"),
)
