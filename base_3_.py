from mecode import G
import numpy as np

outfile = r"C:\Users\avalentine\Documents\GitHub\AFRL-printing\my_print.pgm"


g=G(
    #direct_write=False,
    #outfile=outfile,
    #header=None,
    #footer=None,
    print_lines=False,
)
#hey


def first_print():

    #11 layers - 1 base + 10 notched
    
    #base layer (1)
    g.meander(4.4,4.4,0.1)
    
    #next layer (2)
    g.move(-0.1,-0.1,0.1)
    
    #second layer fill (2)
    g.meander(4.2,4.1,0.1,start="UR")
    
    
    #first line of notches (2)
    g.move(y=-0.1)
    g.move(-1.4)
    g.move(y=0.1)
    g.move(-0.2)
    g.move(y=-0.1)
    g.move(-1.0)
    g.move(y=0.1)
    g.move(-0.2)
    g.move(y=-0.1)
    g.move(-1.4)
    
    #next layer (3)
    g.move(0.1,0.1,0.1)
    
    #second line of notches (3)
    g.move(1.3)
    g.move(y=0.1)
    g.move(0.2)
    g.move(y=-0.1)
    g.move(1.0)
    g.move(y=0.1)
    g.move(0.2)
    g.move(y=-0.1)
    g.move(1.3)
    g.move(y=0.1)
    
    #third layer fill (3)
    g.meander(4,3.9,0.1,start="LR")
    
    #next layer (4)
    g.move(-0.1,-0.1,0.1)
    
    #fourth layer fill (4)
    g.meander(3.8,3.7,0.1,start="UR")
    
    #third line notches (4)
    g.move(y=-0.1)
    g.move(-1.2)
    g.move(y=0.1)
    g.move(-0.2)
    g.move(y=-0.1)
    g.move(-1.0)
    g.move(y=0.1)
    g.move(-0.2)
    g.move(y=-0.1)
    g.move(-1.2)
    
    #next layer (5)
    g.move(0.1,0.1,0.1)
    
    #fourth line notches (5)
    
    g.move(1.1)
    g.move(y=0.1)
    g.move(0.2)
    g.move(y=-0.1)
    g.move(1.0)
    g.move(y=0.1)
    g.move(0.2)
    g.move(y=-0.1)
    g.move(1.1)
    g.move(y=0.1)
    
    #fifth layer fill (5)
    g.meander(3.6,3.5,0.1,start="LR")
    
    #next layer (6)
    g.move(-0.1,-0.1,0.1)
    
    #sixth layer fill (6)
    g.meander(3.4,3.3,0.1,start="UR")
    
    #fifth line notches (6)
    g.move(y=-0.1)
    g.move(-1)
    g.move(y=0.1)
    g.move(-0.2)
    g.move(y=-0.1)
    g.move(-1.0)
    g.move(y=0.1)
    g.move(-0.2)
    g.move(y=-0.1)
    g.move(-1)
    
    #next layer (7)
    g.move(0.1,0.1,0.1)
    
    #sixth line notches (7)
    g.move(0.9)
    g.move(y=0.1)
    g.move(0.2)
    g.move(y=-0.1)
    g.move(1.0)
    g.move(y=0.1)
    g.move(0.2)
    g.move(y=-0.1)
    g.move(0.9)
    g.move(y=0.1)
    
    #seventh layer fill
    g.meander(3.2,3.1,0.1,start="LR")
    
    #next layer (8)
    g.move(-0.1,-0.1,0.1)
    
    #eigth layer fill
    g.meander(3,2.9,0.1,start="UR")
    
    #seventh line notches
    g.move(y=-0.1)
    g.move(-0.8)
    g.move(y=0.1)
    g.move(-0.2)
    g.move(y=-0.1)
    g.move(-1.0)
    g.move(y=0.1)
    g.move(-0.2)
    g.move(y=-0.1)
    g.move(-0.8)
    
    #next line (9)
    g.move(0.1,0.1,0.1)
    
    #eigth line notches (9)
    g.move(0.7)
    g.move(y=0.1)
    g.move(0.2)
    g.move(y=-0.1)
    g.move(1.0)
    g.move(y=0.1)
    g.move(0.2)
    g.move(y=-0.1)
    g.move(0.7)
    g.move(y=0.1)
    
    #ninth layer fill (9)
    g.meander(2.8,2.7,0.1,start="LR")
    
    #next line (10)
    g.move(-0.1,-0.1,0.1)
    
    #tenth layer fill (10)
    g.meander(2.6,2.5,0.1,start="UR")
    
    #ninth line notches (10)
    g.move(y=-0.1)
    g.move(-0.6)
    g.move(y=0.1)
    g.move(-0.2)
    g.move(y=-0.1)
    g.move(-1.0)
    g.move(y=0.1)
    g.move(-0.2)
    g.move(y=-0.1)
    g.move(-0.6)
    
    #next line (11)
    g.move(0.1,0.1,0.1)
    
    #tenth line notches(11)
    g.move(0.5)
    g.move(y=0.1)
    g.move(0.2)
    g.move(y=-0.1)
    g.move(1.0)
    g.move(y=0.1)
    g.move(0.2)
    g.move(y=-0.1)
    g.move(0.5)
    g.move(y=0.1)
    
    #eleventh layer fill
    g.meander(2.4,2.3,0.1,start="LR")


##third line of notches
#g.move(0.1,0.1,0.1)
#g.move(1)
#g.move(y=0.1)
#g.move(0.2)
#g.move(y=-0.1)
#g.move(1.0)
#g.move(y=0.1)
#g.move(0.2)
#g.move(y=-0.1)
#g.move(1)
#g.move(y=0.1)
#
##third layer of fill
#g.meander(4.,3.9,0.1,start="LR")
#
#g.move(-0.1,-0.1,0.1)
#
##fourth layer of fill
#g.meander(3.8,3.7,0.1,start="UR")
#



#g.move(-0.1,-0.1,0.1)
#g.meander(4.2,4.2,0.1,start='UR')
#g.move(0.1,0.1,0.1)
#g.meander(4,4,0.1)
#g.move(-0.1,-0.1,0.1)
#g.meander(3.8,3.8,0.1,start='UR')
#g.move(0.1,0.1,0.1)
#g.meander(3.6,3.6,0.1)
#g.move(-0.1,-0.1,0.1)
#g.meander(3.4,3.4,0.1,start='UR')
#g.move(0.1,0.1,0.1)
#g.meander(3.2,3.2,0.1)
#g.move(-0.1,-0.1,0.1)
#g.meander(3.,3.,0.1,start='UR')
#g.move(0.1,0.1,0.1)
#g.meander(2.8,2.8,0.1)
#g.move(-0.1,-0.1,0.1)
#g.meander(2.6,2.6,0.1,start='UR')
#g.move(0.1,0.1,0.1)

#g.move(-1.1,-1.1,1)
#g.meander(2.4,2.4,0.1,start='UR')

first_print()
g.view()

g.teardown()

