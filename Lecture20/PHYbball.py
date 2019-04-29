# Shoot a basketball! 
# balle - Program to compute the trajectory of a baseball
#         using the Euler method.
# Adapted from Garcia, Numerical Methods for Physics, 2nd Edition

#* Set initial position and velocity of the baseball
from math import *
import numpy as np
import matplotlib
matplotlib.rcParams['legend.fancybox'] = True
import matplotlib.pyplot as plt
from matplotlib import legend
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation
basket = 0.0
y1 = 0.0
speed = 0.0
theta = 0.0
r1 = [0.0] * 2
v1 = [0.0] * 2
r =  [0.0] * 2
v =  [0.0] * 2
accel = [0.0] * 2
shot = 0.0
pts = 0.0
euler = 0
print 'Welcome to Physics Basketball!'
print'             ____|'
print'       o     \%/ |~~'
print'  o//              |'
print'  8                |'
print' / >               |'
print'~ ~             ~~~~~~'
inp = input("Enter number of attempts: ")
basket = input ( "Enter distance to basket (meters): " )
if (basket > 6.70):
	shot = 3
	print 'Attempting 3 point shot'
else:
	shot = 2	
	print 'Attempting 2 point shot'
y1 = input( "Enter initial height (meters): ")
r1[0] = 0
r1[1] = y1     # Initial vector position
for number in range(inp) :
	
#FOR LOOP 10 TIMES SHOW SUCCESSES
	speed = input( "Enter initial speed (m/s): ")
	theta = input("Enter initial angle (degrees): ")

	v1[0] = speed*cos(theta*pi/180.)   # Initial velocity (x)
	v1[1] = speed*sin(theta*pi/180.)   # Initial velocity (y)
	r[0] = r1[0]
	r[1] = r1[1]  # Set initial position and velocity
	v[0] = v1[0]
	v[1] = v1[1]             

	#* Set physical parameters (mass, Cd, etc.)
	Cd = 0.47      # Drag coefficient (dimensionless)
	area = 0.0457  # Cross-sectional area of projectile (m^2)
	grav = 9.81    # Gravitational acceleration (m/s^2)
	mass = 0.625   # Mass of projectile (kg)
	airFlag = 0
	rho = 0.0
	airFlag = input( "Outdoors or inside [a vaccuum ;)]? (Outside:1, Inside :0): ")
	if airFlag == 0 :
	    rho = 0      # No air resistance
	else :
	    rho = 1.2    # Density of air (kg/m^3)
	air_const = -0.5*Cd*rho*area/mass  # Air resistance constant
	
	euler = 2
	print "Using Midpoint approximation method"
	
	#* Loop until ball hits ground or max steps completed
	tau = 0.0
	tau = input("Enter timestep at 0.05 or smaller, tau (sec): ")
	iStep = 0
	maxStep = 1000   # Maximum number of steps
	xplot = []
	yplot = []
	xNoAir = []
	yNoAir = []
	for iStep in xrange(maxStep) :
	
	    print iStep
	    print str(r[1]) + ',' +str(r[0])
	    #* Record position (computed and theoretical) for plotting
	    xplot.append( r[0] )   # Record trajectory for plot
	    yplot.append( r[1] )
	    t = (iStep)*tau     # Current time
	    xNoAir.append( r1[0] + v1[0]*t )
	    yNoAir.append( r1[1] + v1[1]*t - 0.5*grav*t*t )
	
	    #* Calculate the acceleration of the ball 
	    normV = sqrt( v[0]*v[0] + v[1]*v[1] )
	    accel[0] = air_const*normV*v[0]   # Air resistance
	    accel[1] = air_const*normV*v[1]   # Air resistance
	    accel[1] -= grav                  # Gravity
	
	    #* Calculate the new position and velocity using Euler method
	    #if ( euler == 0 ) :        # Euler step
	     #   r[0] += tau*v[0]                 
	      # v[0] += tau*accel[0]     
	      #  v[1] += tau*accel[1]     
	    #elif ( euler == 1 ) : # Euler-Cromer step
	    #    v[0] += tau*accel[0]     
	    #    v[1] += tau*accel[1]     
	    #    r[0] += tau*v[0]                 
	    #    r[1] += tau*v[1]                 
	    #else :                   # Midpoint step
	    vx_last = v[0]
    	    vy_last = v[1]
    	    v[0] += tau*accel[0]     
    	    v[1] += tau*accel[1]     
    	    r[0] += tau*0.5*(v[0] + vx_last)                 
    	    r[1] += tau*0.5*(v[1] + vy_last)
	
	
	    #* If ball reaches ground (y<0), or if the basket is made break out of the loop
	    if (2.8 < r[1] < 3.2)  & ((basket - 0.2) < r[0] < (basket + 0.2)):
		pts = pts + shot
	        xplot.append( r[0] )  # Record last values computed
	        yplot.append( r[1] )
		print 'BASKET MADE'
		print 'Total points: ' + str(pts)	        
		break                  # Break out of the for loop
	    elif r[1] < 0 :
		xplot.append( r[0] )  # Record last values computed
	        yplot.append( r[1] )
		print 'MISS'
		print 'Total points: ' + str(pts)
		break
	fig , ax1 = plt.subplots()
	line, = ax1.plot(xplot, yplot)
	p2 = ax1.plot(basket, 3.0,marker='o', markersize=15, color="orange")
	def update(num, xplot, yplot, line):
		line.set_data(xplot[:num], yplot[:num])
		line.axes.axis([0,10,0,10])
		return line,
	ani = animation.FuncAnimation(fig, update, len(xplot), fargs = [xplot,yplot,line], interval = 200, blit =True)

	#* Print maximum range and time of flight
#	print "Maximum range is " + str( r[0] ) + " meters"
#	print "Time of flight is " +str( iStep*tau ) + " seconds"
#	p1, = ax1.plot(xplot,yplot)
#	p2, = ax1.plot(xNoAir,yNoAir)

	
	plt.show()
