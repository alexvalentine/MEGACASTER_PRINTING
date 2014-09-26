from mecode import G
import numpy as np

outfile = r"/Volumes/jlewis/User Files/Valentine/AFRL/my_print.pgm"


g=G(
    direct_write=False,
    #outfile=outfile,
    #header=r"/Users/alex/alexvalentine/AFRL-printing/mymegacasterheader.txt",
    #footer=r"/Users/alex/alexvalentine/AFRL-printing/mymegacasterfooter.txt",
    print_lines=True,
    aerotech_include=False,
)


pressure_box = 16  #megacaster pressure box com port

pressure = 55    #pressure needed for AG-TPU ink with 100um nozzle + high pressure adapter

#def square_base(length, height, connections, layer_height, theta = 45):
#    base_extra = height/np.tan(theta)  # x component of slope
#
#    base_length = length + 2*base_extra
#    
#    layers = height/layer_height
#    layers = int(round(layers))
#    
#    for i in range(layers):
#        if i==0:
#            g.meader(base_length, base_length, spacing=0.1,start='UL')
#            g.move(x = , y = , z = height)
#        elif i%2==1:
#            
#        else:
            

pad_positions=((0.1,0.38+0.28*0),(.1,0.38+0.28*1),(.1,0.38+0.28*2),(.1,0.38+0.28*3),(.1,0.38+0.28*4),(.1,0.38+0.28*5),
(0.38+0.28*0,2.06),(0.38+0.28*1,2.06),(0.38+0.28*2,2.06),(0.38+0.28*3,2.06),(0.38+0.28*4,2.06),(0.38+0.28*5,2.06),
(2.06,0.38+0.28*5),(2.06,0.38+0.28*4),(2.06,0.38+0.28*3),(2.06,0.38+0.28*2),(2.06,0.38+0.28*1),(2.06,0.38+0.28*0),
(0.38+0.28*5,0.1),(0.38+0.28*4,0.1),(0.38+0.28*3,0.1),(0.38+0.28*2,0.1),(0.38+0.28*1,0.1),(0.38+0.28*0,0.1))

#coordinates of the center of all contact pads, starting in LL corner and going clockwise
#24 pads, 6 on each side

pyramid_positions=((0,0),(0,19.4-6),(0,38.8-12),(-19.4+6,19.4-6),(19.4-6,19.4-6))

#coordinates of the center of all contact pads, starting in LL corner and going clockwise
#24 pads, 6 on each side

def pyramids():

    for i in np.arange(10):
        if i%2==0:
            start1='LL'
            num=-1            
        else:
            start1='UR'
            num=1
        g.meander(4.4-(i*0.2),4.4-(i*0.2),0.1,start=start1)
        g.move(x=0.1*num,y=0.1*num,z=0.1)

    g.move(x=-3.6,y=3.4,z=2)
    g.abs_move(x=pyramid_positions[1][0],y=pyramid_positions[1][1])
    g.move(z=-3)
    
    for i in np.arange(10):
        if i%2==0:
            start1='LL'
            num=-1            
        else:
            start1='UR'
            num=1
        g.meander(4.4-(i*0.2),4.4-(i*0.2),0.1,start=start1)
        g.move(x=0.1*num,y=0.1*num,z=0.1)
    
    g.move(x=-3.6,y=3.4,z=2)
    g.abs_move(x=pyramid_positions[2][0],y=pyramid_positions[2][1])
    g.move(z=-3)
    
    for i in np.arange(10):
        if i%2==0:
            start1='LL'
            num=-1            
        else:
            start1='UR'
            num=1
        g.meander(4.4-(i*0.2),4.4-(i*0.2),0.1,start=start1)
        g.move(x=0.1*num,y=0.1*num,z=0.1)
    
    g.move(x=-3.6,y=3.4,z=2)
    g.abs_move(x=pyramid_positions[3][0],y=pyramid_positions[3][1])
    g.move(z=-3)

    for i in np.arange(10):
        if i%2==0:
            start1='LL'
            num=-1            
        else:
            start1='UR'
            num=1
        g.meander(4.4-(i*0.2),4.4-(i*0.2),0.1,start=start1)
        g.move(x=0.1*num,y=0.1*num,z=0.1)

    g.move(x=-3.6,y=3.4,z=2)
    g.abs_move(x=pyramid_positions[4][0],y=pyramid_positions[4][1])
    g.move(z=-3)

    for i in np.arange(10):
        if i%2==0:
            start1='LL'
            num=-1            
        else:
            start1='UR'
            num=1
        g.meander(4.4-(i*0.2),4.4-(i*0.2),0.1,start=start1)
        g.move(x=0.1*num,y=0.1*num,z=0.1)

    g.move(x=-3.6,y=3.4,z=2)

def serp_wires_pyramids():
    g.abs_move(x=1.55,y=3.2)
    g.move(z=-2.05)
    g.move(y=0.3)
    g.move(y=0.95,z=-0.95)
    
    g.move(y=0.45)
    
    for i in np.arange(20):
        if i%2==0:
            dir='CW'
        else:
            dir='CCW'
        g.arc(x=0,y=0.4,radius=-0.3,direction=dir)
    g.move(y=0.45)
    g.move(y=0.95,z=0.95)
    g.move(y=0.3)
    g.move(z=2.05)
   
    g.move(x=1.3)
    g.move(z=-2.05)
    g.move(y=-0.3)
    g.move(y=-0.95,z=-0.95)
    
    g.move(y=-0.45)
    
    for i in np.arange(20):
        if i%2==0:
            dir='CW'
        else:
            dir='CCW'
        g.arc(x=0,y=-0.4,radius=-0.3,direction=dir)
    g.move(y=-0.45)
    g.move(y=-0.95,z=0.95)
    g.move(y=-0.3)
    g.move(z=2.05)

    g.abs_move(x=pyramid_positions[3][0],y=pyramid_positions[3][1])
    g.move(x=3.2,y=1.55)
    g.move(z=-2.05)

    g.move(x=0.3)
    g.move(x=0.95,z=-0.95)

    g.move(x=0.45)
    
    for i in np.arange(20):
        if i%2==0:
            dir='CW'
        else:
            dir='CCW'
        g.arc(x=0.4,y=0,radius=-0.3,direction=dir)
    g.move(x=0.45)
    g.move(x=0.95,z=0.95)
    g.move(x=0.3)
    g.move(z=2.05)
   
    g.move(y=1.3)
    g.move(z=-2.05)
    g.move(x=-0.3)
    g.move(x=-0.95,z=-0.95)
    
    g.move(x=-0.45)
    
    for i in np.arange(20):
        if i%2==0:
            dir='CW'
        else:
            dir='CCW'
        g.arc(x=-0.4,y=0,radius=-0.3,direction=dir)
    g.move(x=-0.45)
    g.move(x=-0.95,z=0.95)
    g.move(x=-0.3)
    g.move(z=2.05)

    g.abs_move(x=pyramid_positions[1][0],y=pyramid_positions[1][1])
    g.move(x=1.55,y=3.2)
    g.move(z=-2.05)
    g.move(y=0.3)
    g.move(y=0.95,z=-0.95)
    
    g.move(y=0.45)
    
    for i in np.arange(20):
        if i%2==0:
            dir='CW'
        else:
            dir='CCW'
        g.arc(x=0,y=0.4,radius=-0.3,direction=dir)
    g.move(y=0.45)
    g.move(y=0.95,z=0.95)
    g.move(y=0.3)
    g.move(z=2.05)
   
    g.move(x=1.3)
    g.move(z=-2.05)
    g.move(y=-0.3)
    g.move(y=-0.95,z=-0.95)
    
    g.move(y=-0.45)
    
    for i in np.arange(20):
        if i%2==0:
            dir='CW'
        else:
            dir='CCW'
        g.arc(x=0,y=-0.4,radius=-0.3,direction=dir)
    g.move(y=-0.45)
    g.move(y=-0.95,z=0.95)
    g.move(y=-0.3)
    g.move(z=2.05)


    g.abs_move(x=pyramid_positions[1][0],y=pyramid_positions[1][1])
    g.move(x=3.2,y=1.55)
    g.move(z=-2.05)

    g.move(x=0.3)
    g.move(x=0.95,z=-0.95)

    g.move(x=0.45)
    
    for i in np.arange(20):
        if i%2==0:
            dir='CW'
        else:
            dir='CCW'
        g.arc(x=0.4,y=0,radius=-0.3,direction=dir)
    g.move(x=0.45)
    g.move(x=0.95,z=0.95)
    g.move(x=0.3)
    g.move(z=2.05)
   
    g.move(y=1.3)
    g.move(z=-2.05)
    g.move(x=-0.3)
    g.move(x=-0.95,z=-0.95)
    
    g.move(x=-0.45)
    
    for i in np.arange(20):
        if i%2==0:
            dir='CW'
        else:
            dir='CCW'
        g.arc(x=-0.4,y=0,radius=-0.3,direction=dir)
    g.move(x=-0.45)
    g.move(x=-0.95,z=0.95)
    g.move(x=-0.3)
    g.move(z=2.05)



    g.move(x=20,y=20)


    



def first_print():

    #11 layers - 1 base + 10 notched
    #g.move(5)
    
    
    g.feed(3)
    
    #base layer (1)
    g.meander(4.4,4.4,0.1)
    
    #next layer (2)
    g.move(-0.1,-0.1,0.08)
    
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
    g.move(0.1,0.1,0.08)
    
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
    g.move(-0.1,-0.1,0.08)
    
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
    g.move(0.1,0.1,0.08)
    
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
    g.move(-0.1,-0.1,0.08)
    
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
    g.move(0.1,0.1,0.08)
    
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
    g.move(-0.1,-0.1,0.08)
    
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
    g.move(0.1,0.1,0.08)
    
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
    g.move(-0.1,-0.1,0.08)
    
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
    g.move(0.1,0.1,0.08)
    
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

    #g.move(3,3,3)

   
      
         
def MGH_print():
    #----print 4 electrodes 
    #g.set_home(x=0,y=0)
    #g.abs_move(x=3,y=24)
    #g.move(z=-5)
    #g.meander(x=3,y=3,spacing=0.3,start='UL')
    #g.move(z=5)
    #g.abs_move(x=3,y=18)
    #g.move(z=-5)
    #g.meander(x=3,y=3,spacing=0.3,start='UL')
    #g.move(z=5)
    #g.abs_move(x=3,y=12)
    #g.move(z=-5)
    #g.meander(x=3,y=3,spacing=0.3,start='UL')
    #g.move(z=5)
    #g.abs_move(x=3,y=6)
    #g.move(z=-5)
    #g.meander(x=3,y=3,spacing=0.3,start='UL')
    #g.move(z=5)
    #g.abs_move(x=0,y=0)

    #----print TPU around electrodes
    #g.move(z=-5)
    #g.meander(x=30,y=3,spacing=0.3,start='LL')
    #g.move(y=0.3)
    #g.meander(x=24,y=3,spacing=0.3,start='LR')
    #g.move(x=-3)
    #g.move(y=0.3)
    #g.meander(x=27,y=2.1,spacing=0.3,start='LL')
    #g.move(y=0.3)
    #g.meander(x=24,y=3,spacing=0.3,start='LR')
    #g.move(z=5)
    #g.abs_move(x=30,y=12.3)
    #g.move(z=-5)
    #g.meander(x=27,y=2.4,spacing=0.3,start='LR')
    #g.move(z=5)
    #g.abs_move(x=30,y=15.)
    #g.move(z=-5)
    #g.meander(x=24,y=3,spacing=0.3,start='LR')
    #g.move(z=5)
    #g.abs_move(x=30,y=18.3)
    #g.move(z=-5)
    #g.meander(x=27,y=2.4,spacing=0.3,start='LR')
    #g.move(z=5)
    #g.abs_move(x=30,y=21.)
    #g.move(z=-5)
    #g.meander(x=24,y=3,spacing=0.3,start='LR')
    #g.move(z=5)
    #g.abs_move(x=30,y=24.3)
    #g.move(z=-5)
    #g.meander(x=27,y=3,spacing=0.3,start='LR')
    #g.move(x=-0.3)
    #g.meander(x=2.7,y=24,spacing=0.3,start='UR',orientation='y')
    #g.move(z=5)

    #----print leads
#    g.abs_move(x=4.5,y=22.5)
#    g.move(z=-4.7)
#    g.move(x=6)
#    g.move(x=3,y=-5.5)
#    g.move(y=0.5)
#    g.meander(x=2,y=1,spacing=0.3,start='UL')
#    g.move(z=4.7)
#    
#    g.abs_move(x=4.5,y=16.5)
#    g.move(z=-4.7)
#    g.move(x=6)
#    g.move(x=3,y=-1.75)
#    g.move(y=0.5)
#    g.meander(x=2,y=1,spacing=0.3,start='UL')
#    g.move(z=4.7)
#
#    g.abs_move(x=4.5,y=10.5)
#    g.move(z=-4.7)
#    g.move(x=6)
#    g.move(x=3,y=1.75)
#    g.move(y=0.5)
#    g.meander(x=2,y=1,spacing=0.3,start='UL')
#    g.move(z=4.7)
#
#    g.abs_move(x=4.5,y=4.5)
#    g.move(z=-4.7)
#    g.move(x=6)
#    g.move(x=3,y=5.5)
#    g.move(y=0.5)
#    g.meander(x=2,y=1,spacing=0.3,start='UL')
#    g.move(z=4.7)


    #----print TPU cover
    g.abs_move(x=0,y=0)
    g.move(z=-4.4)
    g.meander(x=30,y=9.2,spacing=0.3,start='LL')
    g.move(y=0.3)
    g.meander(x=13.4,y=1,spacing=0.3,start='LL')
    g.move(z=4.4)
    g.move(x=-13.4,y=0.3)
    g.move(z=-4.4)
    g.meander(x=15.5,y=0.8,spacing=0.3,start='LL')
    g.move(y=0.3)
    g.meander(x=13.4,y=1,spacing=0.3,start='LL')
    g.move(x=2.1)
    g.move(y=0.3)
    g.meander(x=15.5,y=0.8,spacing=0.3,start='LR')
    g.move(z=4.4)
    g.move(x=-15.5,y=0.3)
    g.move(z=-4.4)
    g.meander(x=13.4,y=1,spacing=0.3,start='LL')
    g.move(z=4.4)
    g.move(x=-13.4,y=0.2)
    g.move(z=-4.4)
    g.meander(x=15.5,y=0.8,spacing=0.3,start='LL')
    g.move(y=0.3)
    g.meander(x=13.4,y=1,spacing=0.3,start='LL')
    g.move(x=-13.4)
    g.meander(x=30,y=10,spacing=0.3,start='LL')
    g.move(z=4.4)
    g.move(y=-10.3)
    g.move(z=-4.4)
    g.meander(x=14.5,y=8,spacing=0.3,start='UR')
    

    g.move(z=3)

def print_die():
    #g.abs_move(x=0,y=0)
    #g.abs_move(x=0.38,y=0.1)
    #g.move(x=0.1,y=0.1)
    #g.rect(x=0.2,y=0.2)
    #g.meander(x=0.2,y=0.2,spacing=0.05,start='LL',orientation='y')
    #g.move(x=-0.1) #x=380,y=200
    #
    #g.move(y=0.18) 
    #g.move(x=-0.18)
    #
    #g.move(y=0.1)
    #g.meander(x=0.2,y=0.2,spacing=0.05,start='UR',orientation='y')
    #g.clip(axis='z',direction='-x',height=1 )

    for i in np.arange(2):
        for j in np.arange(6):
            if i==0:
                g.move(z=0.5)
                g.abs_move(x=pad_positions[23-j][0],y=pad_positions[23-j][1])
                g.move(z=-0.5)
                g.move(x=0.075,y=0.075)
                g.rect(x=0.15,y=0.15,start='UR')
                g.move(x=-0.05,y=-0.05)
                g.rect(x=0.05,y=0.05,start='UR')
                g.move(x=-0.025,y=-0.025)
                if j<3:
                    g.move(y=pad_positions[j][1]-pad_positions[23-j][1])
                    g.move(x=-(pad_positions[23-j][0]-pad_positions[j][0]))
                    g.move(x=0.025,y=0.025)
                    g.rect(x=0.05,y=0.05,start='UR')
                    g.move(x=0.05,y=0.05)
                    g.rect(x=0.15,y=0.15,start='UR')
                    g.move(x=-0.075,y=-0.075)
                else:
                    g.move(y=pad_positions[12+j][1]-pad_positions[23-j][1])
                    g.move(x=-(pad_positions[23-j][0]-pad_positions[12+j][0]))
                    g.move(x=0.025,y=0.025)
                    g.rect(x=0.05,y=0.05,start='UR')
                    g.move(x=0.05,y=0.05)
                    g.rect(x=0.15,y=0.15,start='UR')
                    g.move(x=-0.075,y=-0.075)
            else:
                g.move(z=0.5)
                g.abs_move(x=pad_positions[6+j][0],y=pad_positions[6+j][1])
                g.move(z=-0.5)
                g.move(x=0.075,y=0.075)
                g.rect(x=0.15,y=0.15,start='UR')
                g.move(x=-0.05,y=-0.05)
                g.rect(x=0.05,y=0.05,start='UR')
                g.move(x=-0.025,y=-0.025)
                if j<3:
                    g.move(y=-(pad_positions[j][1]-pad_positions[23-j][1]))
                    g.move(x=-(pad_positions[23-j][0]-pad_positions[j][0]))
                    g.move(x=0.025,y=0.025)
                    g.rect(x=0.05,y=0.05,start='UR')
                    g.move(x=0.05,y=0.05)
                    g.rect(x=0.15,y=0.15,start='UR')
                    g.move(x=-0.075,y=-0.075)
                else:
                    g.move(y=-(pad_positions[12+j][1]-pad_positions[23-j][1]))
                    g.move(x=-(pad_positions[23-j][0]-pad_positions[12+j][0]))
                    g.move(x=0.025,y=0.025)
                    g.rect(x=0.05,y=0.05,start='UR')
                    g.move(x=0.05,y=0.05)
                    g.rect(x=0.15,y=0.15,start='UR')
                    g.move(x=-0.075,y=-0.075)
    g.move(z=0.5)
    
    
def print_die_wiring():
    g.move(z=-0.5)
    for i in np.arange(2):        
        for j in np.arange(6):
                if i==0:
                    g.move(z=0.5)
                    g.abs_move(x=pad_positions[23-j][0],y=pad_positions[23-j][1])
                    g.move(z=-0.5)
                    g.move(y=-3)
                    if j<3:
                        g.move(x=-3/(j+1),y=-3)
                    else:
                        g.move(x=(j+1)-3,y=-3)
                else:
                    g.move(z=0.5)
                    g.abs_move(x=pad_positions[6+j][0],y=pad_positions[6+j][1])
                    g.move(z=-0.5)
                    g.move(y=3)
                    if j<3:
                        g.move(x=-3/(j+1),y=3)
                    else:
                        g.move(x=(j+1)-3,y=3)
    for i in np.arange(2):        
        for j in np.arange(6):
                if i==0:
                    g.move(z=0.5)
                    g.abs_move(x=pad_positions[j][0],y=pad_positions[j][1])
                    g.move(z=-0.5)
                    g.move(x=-3)
                    if j<3:
                        g.move(x=-3,y=-3/(j+1))
                    else:
                        g.move(x=-3,y=(j+1)-3)
                else:
                    g.move(z=0.5)
                    g.abs_move(x=pad_positions[17-j][0],y=pad_positions[17-j][1])
                    g.move(z=-0.5)
                    g.move(x=3)
                    if j<3:
                        g.move(x=3,y=-3/(j+1))
                    else:
                        g.move(x=3,y=(j+1)-3)
    g.move(z=0.5)    

   
      
 
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


#
#g.set_home(x=0, y=0, z=0)
##
#g.set_pressure(pressure_box, pressure)
#g.toggle_pressure(pressure_box)
#first_print()
#MGH_print()
#g.toggle_pressure(pressure_box)

#print_die()
#print_die_wiring()
serp_wires_pyramids()
g.view()

g.view(backend='matplotlib')

g.teardown()

