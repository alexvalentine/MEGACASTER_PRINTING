from mecode import G
import numpy as np

#outfile = r"/Volumes/group0/jlewis/User Files/Valentine/AFRL/my_print.pgm"
outfile = r'C:\Users\Wyss User\myprint.pgm'

#myz = 2.82357
g=G(
    direct_write=False,
    outfile=outfile,
    #header=r"/Users/alex/alexvalentine/AFRL-printing/mymegacasterheader.txt",
    #footer=r"/Users/alex/alexvalentine/AFRL-printing/mymegacasterfooter.txt",
    print_lines=False,
    aerotech_include=False,
)

pad_positions=((0.1,0.38+0.28*0),(.1,0.38+0.28*1),(.1,0.38+0.28*2),(.1,0.38+0.28*3),(.1,0.38+0.28*4),(.1,0.38+0.28*5),
(0.38+0.28*0,2.06),(0.38+0.28*1,2.06),(0.38+0.28*2,2.06),(0.38+0.28*3,2.06),(0.38+0.28*4,2.06),(0.38+0.28*5,2.06),
(2.06,0.38+0.28*5),(2.06,0.38+0.28*4),(2.06,0.38+0.28*3),(2.06,0.38+0.28*2),(2.06,0.38+0.28*1),(2.06,0.38+0.28*0),
(0.38+0.28*5,0.1),(0.38+0.28*4,0.1),(0.38+0.28*3,0.1),(0.38+0.28*2,0.1),(0.38+0.28*1,0.1),(0.38+0.28*0,0.1))

pressure_box = 12
pdms_pressure = 13

def print_die(speed,dwell):
    g.set_home(x=0,y=0)
    g.set_pressure(pressure_box, pdms_pressure)   
    g.feed(5)
    g.move(z=2)
    for i in np.arange(2):
        for j in np.arange(6):
            if i==0:
                g.abs_move(x=pad_positions[23-j][0],y=pad_positions[23-j][1])
                g.move(z=-2)
                g.feed(speed)
                g.toggle_pressure(pressure_box)
                g.dwell(dwell)
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
                    g.toggle_pressure(pressure_box)
                    g.feed(10)
                    g.clip(height=2, direction='-x')
                else:
                    g.move(y=pad_positions[12+j][1]-pad_positions[23-j][1])
                    g.move(x=-(pad_positions[23-j][0]-pad_positions[12+j][0]))
                    g.move(x=0.025,y=0.025)
                    g.rect(x=0.05,y=0.05,start='UR')
                    g.move(x=0.05,y=0.05)
                    g.rect(x=0.15,y=0.15,start='UR')
                    g.move(x=-0.075,y=-0.075)
                    g.toggle_pressure(pressure_box)
                    g.feed(10)
                    g.clip(height=2, direction='-x')
            else:
                g.abs_move(x=pad_positions[6+j][0],y=pad_positions[6+j][1])
                g.move(z=-2)
                g.feed(speed)
                g.toggle_pressure(pressure_box)
                g.dwell(dwell)
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
                    g.toggle_pressure(pressure_box)
                    g.feed(10)
                    g.clip(height=2, direction='-x')
                else:
                    g.move(y=-(pad_positions[12+j][1]-pad_positions[23-j][1]))
                    g.move(x=-(pad_positions[23-j][0]-pad_positions[12+j][0]))
                    g.move(x=0.025,y=0.025)
                    g.rect(x=0.05,y=0.05,start='UR')
                    g.move(x=0.05,y=0.05)
                    g.rect(x=0.15,y=0.15,start='UR')
                    g.move(x=-0.075,y=-0.075)
                    g.toggle_pressure(pressure_box)
                    g.feed(10)
                    g.clip(height=2, direction='-x')
   # g.move(z=0.5)

def print_die_wiring(speed,dwell):
    #g.set_pressure(pressure_box, pdms_pressure)   
    g.feed(5)
    for i in np.arange(2):        
        for j in np.arange(6):
                if i==0:
                    g.abs_move(x=pad_positions[23-j][0],y=pad_positions[23-j][1])
                    g.move(z=-2)
                    g.feed(speed)
                    #g.toggle_pressure(pressure_box)
                    g.dwell(dwell)
                    g.move(y=-3)
                    if j<3:
                        g.move(x=-3/(j+1),y=-3)
                        #g.toggle_pressure(pressure_box)
                        g.feed(10)
                        g.clip(height=2, direction='-x')
                    else:
                        g.move(x=(j+1)-3,y=-3)
                        #g.toggle_pressure(pressure_box)
                        g.feed(10)
                        g.clip(height=2, direction='-x')
                else:
                    g.abs_move(x=pad_positions[6+j][0],y=pad_positions[6+j][1])
                    g.move(z=-2)
                    g.feed(speed)
                    #g.toggle_pressure(pressure_box)
                    g.dwell(dwell)
                    g.move(y=3)
                    if j<3:
                        g.move(x=-3/(j+1),y=3)
                        #g.toggle_pressure(pressure_box)
                        g.feed(10)
                        g.clip(height=2, direction='-x')
                    else:
                        g.move(x=(j+1)-3,y=3)
                        #g.toggle_pressure(pressure_box)
                        g.feed(10)
                        g.clip(height=2, direction='-x')
                        
    for i in np.arange(2):        
        for j in np.arange(6):
                if i==0:
                    g.abs_move(x=pad_positions[j][0],y=pad_positions[j][1])
                    g.move(z=-2)
                    g.feed(speed)
                    #g.toggle_pressure(pressure_box)
                    g.dwell(dwell)                    
                    g.move(x=-3)
                    if j<3:
                        g.move(x=-3,y=-3/(j+1))
                        #g.toggle_pressure(pressure_box)
                        g.feed(10)
                        g.clip(height=2, direction='-x')
                    else:
                        g.move(x=-3,y=(j+1)-3)
                        #g.toggle_pressure(pressure_box)
                        g.feed(10)
                        g.clip(height=2, direction='-x')
                else:
                    g.abs_move(x=pad_positions[17-j][0],y=pad_positions[17-j][1])
                    g.move(z=-2)
                    g.feed(speed)
                    #g.toggle_pressure(pressure_box)
                    g.dwell(dwell) 
                    g.move(x=3)
                    if j<3:
                        g.move(x=3,y=-3/(j+1))
                        #g.toggle_pressure(pressure_box)
                        g.feed(10)
                        g.clip(height=2, direction='-x')
                    else:
                        g.move(x=3,y=(j+1)-3)
                        #g.toggle_pressure(pressure_box)
                        g.feed(10)
                        g.clip(height=2, direction='-x')
def LONG_serpentine_encaps_pdms(nozzle,valve,pressure,speed,height):
    g.feed(25)
    g.set_pressure(pressure_box, pressure)
    g.abs_move(x=5,y=5)
    g.abs_move(**{nozzle:height})  
    if valve is not None:
        g.set_valve(num = valve, value = 1)
    g.feed(speed)
    g.dwell(0.8)
    g.meander(x=10,y=12,spacing=0.26,start='LL',orientation='y')
    g.move(y=6)
    g.feed(speed/1.6)
    g.move(x=2)
    g.feed(speed/2)
    for i in np.arange(13):
        if i%2==0:
            direc='CW'
        else:
            direc='CCW'
        g.arc(y=0,x=2.5,radius=-1.7,direction=direc)
    for i in np.arange(4):
        if i%2==0:
            direc='CCW'
        else:
            direc='CW'
        g.arc(y=0.8,x=2.5,radius=-1.7,direction=direc)
    for i in np.arange(2):
        if i%2==0:
            direc='CCW'
        else:
            direc='CW'
        g.arc(y=2.5,x=1.5,radius=-1.7,direction=direc)
    for i in np.arange(2):
        if i%2==0:
            direc='CCW'
        else:
            direc='CW'
        g.arc(y=2.5,x=0.8,radius=-1.7,direction=direc)
    for i in np.arange(2):
        if i%2==0:
            direc='CCW'
        else:
            direc='CW'
        g.arc(y=2.5,x=0,radius=-1.7,direction=direc)
    for i in np.arange(2):
        if i%2==0:
            direc='CCW'
        else:
            direc='CW'
        g.arc(y=2.5,x=-0.8,radius=-1.7,direction=direc)
    for i in np.arange(2):
        if i%2==0:
            direc='CCW'
        else:
            direc='CW'
        g.arc(y=2.5,x=-1.5,radius=-1.7,direction=direc)
    for i in np.arange(4):
        if i%2==0:
            direc='CCW'
        else:
            direc='CW'
        g.arc(y=0.8,x=-2.5,radius=-1.7,direction=direc)
    for i in np.arange(13):
        if i%2==0:
            direc='CCW'
        else:
            direc='CW'
        g.arc(y=0,x=-2.5,radius=-1.7,direction=direc)
    g.move(x=-2)
    g.feed(speed)
    g.move(y=6)
    g.meander(x=10,y=-12,spacing=0.25,start='LR',orientation='y')
    g.set_valve(num = valve, value = 0)
    g.clip(axis=nozzle, direction='-y', height=20)
      
def SHORT_serpentine_encaps_wire(nozzle,valve,pressure,speed,height):    
    g.feed(25)
    g.set_pressure(pressure_box, pressure)
    g.abs_move(x=10,y=10)
    g.abs_move(**{nozzle:height})  
    if valve is not None:
        g.set_valve(num = valve, value = 1)
    g.feed(speed)
    g.dwell(1.3)
    g.meander(x=2,y=2,spacing=0.08,start='LL',orientation='y')
    g.move(y=1)
    g.move(x=5)
    for i in np.arange(10):
        if i%2==0:
            direc='CW'
        else:
            direc='CCW'
        g.arc(x=2.5,y=0,radius=-1.7,direction=direc)
    g.move(x=5)
    g.move(y=-1)
    g.meander(x=2,y=2,spacing=0.08,start='LL',orientation='y')
    g.set_valve(num = valve, value = 0)
    g.clip(axis=nozzle, direction='-y', height=20)

def LONG_serpentine_encaps_wire(nozzle,valve,pressure,speed,height):    
    g.feed(25)
    g.set_pressure(pressure_box, pressure)
    g.abs_move(x=10,y=10)
    g.abs_move(**{nozzle:height})  
    if valve is not None:
        g.set_valve(num = valve, value = 1)
    g.feed(speed)
    g.dwell(1.7)
    g.meander(x=2,y=2,spacing=0.08,start='LL',orientation='y')
    g.move(y=1)
    g.move(x=5)
    g.abs_move(**{nozzle:height-0.04})  
    for i in np.arange(13):
        if i%2==0:
            direc='CW'
        else:
            direc='CCW'
        g.arc(y=0,x=2.5,radius=-1.7,direction=direc)
    for i in np.arange(4):
        if i%2==0:
            direc='CCW'
        else:
            direc='CW'
        g.arc(y=0.8,x=2.5,radius=-1.7,direction=direc)
    for i in np.arange(2):
        if i%2==0:
            direc='CCW'
        else:
            direc='CW'
        g.arc(y=2.5,x=1.5,radius=-1.7,direction=direc)
    for i in np.arange(2):
        if i%2==0:
            direc='CCW'
        else:
            direc='CW'
        g.arc(y=2.5,x=0.8,radius=-1.7,direction=direc)
    for i in np.arange(2):
        if i%2==0:
            direc='CCW'
        else:
            direc='CW'
        g.arc(y=2.5,x=0,radius=-1.7,direction=direc)
    for i in np.arange(2):
        if i%2==0:
            direc='CCW'
        else:
            direc='CW'
        g.arc(y=2.5,x=-0.8,radius=-1.7,direction=direc)
    for i in np.arange(2):
        if i%2==0:
            direc='CCW'
        else:
            direc='CW'
        g.arc(y=2.5,x=-1.5,radius=-1.7,direction=direc)
    for i in np.arange(4):
        if i%2==0:
            direc='CCW'
        else:
            direc='CW'
        g.arc(y=0.8,x=-2.5,radius=-1.7,direction=direc)
    for i in np.arange(13):
        if i%2==0:
            direc='CCW'
        else:
            direc='CW'
        g.arc(y=0,x=-2.5,radius=-1.7,direction=direc)
    g.abs_move(**{nozzle:height+0.04})  
    g.move(x=-5)
    g.move(y=-1)
    g.meander(x=2,y=2,spacing=0.08,start='LR',orientation='y')
    g.set_valve(num = valve, value = 0)
    g.clip(axis=nozzle, direction='-y', height=20)

#print_die(speed=1.4,dwell=0.1)
#print_die_wiring(speed=0.25,dwell=0.1)

LONG_serpentine_encaps_pdms(nozzle='B',valve='2',pressure=22,speed=9,height=0.15+.24+.28)
LONG_serpentine_encaps_wire(nozzle='A',valve='1',pressure=30,speed=0.7,height=0.4-0.15+0.1)


g.view(backend='matplotlib')

g.teardown() 