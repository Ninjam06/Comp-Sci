# Ishaan Jhanji
# Geometry.py 

'''
Begin Required variables section:
=================================
Do not change the names of these variables at all.
You may change the values on the right side of the equals (=) sign if you
would like. For instance if you would like to have raw_input to be able to test
different user information, that's fine.
'''
radiusList = [1, 10,  123.456]
'''
End Required variables:
=======================
You may have any additional variables that you might need to complete
the program below this line.
'''

# Create a constant for PI

import math

PI = math.pi
SA = 0
V = 0

#--#

spot = 0

while spot < len(radiusList):
    SA = 4*PI*(radiusList[spot]**2)
    V = (4.0/3)*PI*(radiusList[spot]**3)
    print "SA = %.3f : V = %.3f"%(SA, V)
    spot = spot + 1
