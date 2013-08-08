# Define time parameters
t=0 #starting time
deltat = 0.01  #time step units are s


### CALCULATION LOOP; perform physics updates and drawing
# ------------------------------------------------------------------------------------
print car1.pos.x
while  car1.pos.x < 1.5:  #while the car1 x-position is between -1.5 and 1.5
 
    # Required to make animation visible / refresh smoothly (keeps program from running faster than 1000 frames/s)
    rate(100)    

    # Compute Net Force 
    Fnet = vector(0,0,0) 

    # Newton's 2nd Law
