from .plot import *

# Capture the original matplotlib rcParams
import matplotlib as mpl
_orig_rc_params = mpl.rcParams.copy()

# Define the EleganPlot version
__version__ = "0.1.0.dev0"