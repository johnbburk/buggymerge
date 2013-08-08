### INITIALIZE VPYTHON
# -----------------------------------------------------------------------

from __future__ import division
from visual import *
from physutil import *
from visual.graph import *

### SETUP ELEMENTS FOR GRAPHING, SIMULATION, VISUALIZATION, TIMING
# ------------------------------------------------------------------------

# Set window title
scene.title = "My Buggy Model"

# Make scene background black
scene.background=color.black


# Define scene objects
track = box(pos =vector(0,-.1,0),size=(3,.1,2),color = color.green) #units are m
