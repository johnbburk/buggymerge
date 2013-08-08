
# Define axis (with a specified length) that marks the track with a specified number of tick marks
axis = PhysAxis(track, 16, length=3) #units are in m

# Set up graph
positiongraph = PhysGraph(%count)


# Set timer in top right of screen
timerDisplay = PhysTimer(1,1)


### SETUP PARAMETERS AND INITIAL CONDITIONS
# ----------------------------------------------------------------------------------------

# Define parameters