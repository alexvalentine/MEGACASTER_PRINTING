from mecode import G
import numpy as np

outfile = r"/Volumes/group0/jlewis/User Files/Valentine/AFRL/my_print.pgm"

#myz = 2.82357
g=G(
    direct_write=False,
    outfile=r'C:\Users\Aerosol Jet\Documents\myprint.pgm',
    header=r'C:\Users\Aerosol Jet\Documents\GitHub\AFRL-printing\mymegacasterheader.txt',
    footer=r'C:\Users\Aerosol Jet\Documents\GitHub\AFRL-printing\mymegacasterfooter.txt',
    print_lines=False,
    aerotech_include=False,
)

pad_positions=((0.1,0.38+0.28*0),(.1,0.38+0.28*1),(.1,0.38+0.28*2),(.1,0.38+0.28*3),(.1,0.38+0.28*4),(.1,0.38+0.28*5),
(0.38+0.28*0,2.06),(0.38+0.28*1,2.06),(0.38+0.28*2,2.06),(0.38+0.28*3,2.06),(0.38+0.28*4,2.06),(0.38+0.28*5,2.06),
(2.06,0.38+0.28*5),(2.06,0.38+0.28*4),(2.06,0.38+0.28*3),(2.06,0.38+0.28*2),(2.06,0.38+0.28*1),(2.06,0.38+0.28*0),
(0.38+0.28*5,0.1),(0.38+0.28*4,0.1),(0.38+0.28*3,0.1),(0.38+0.28*2,0.1),(0.38+0.28*1,0.1),(0.38+0.28*0,0.1))

pressure_box = 16
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
    g.set_pressure(pressure_box, pdms_pressure)   
    g.feed(5)
    for i in np.arange(2):        
        for j in np.arange(6):
                if i==0:
                    g.abs_move(x=pad_positions[23-j][0],y=pad_positions[23-j][1])
                    g.move(z=-2)
                    g.feed(speed)
                    g.toggle_pressure(pressure_box)
                    g.dwell(dwell)
                    g.move(y=-3)
                    if j<3:
                        g.move(x=-3/(j+1),y=-3)
                        g.toggle_pressure(pressure_box)
                        g.feed(10)
                        g.clip(height=2, direction='-x')
                    else:
                        g.move(x=(j+1)-3,y=-3)
                        g.toggle_pressure(pressure_box)
                        g.feed(10)
                        g.clip(height=2, direction='-x')
                else:
                    g.abs_move(x=pad_positions[6+j][0],y=pad_positions[6+j][1])
                    g.move(z=-2)
                    g.feed(speed)
                    g.toggle_pressure(pressure_box)
                    g.dwell(dwell)
                    g.move(y=3)
                    if j<3:
                        g.move(x=-3/(j+1),y=3)
                        g.toggle_pressure(pressure_box)
                        g.feed(10)
                        g.clip(height=2, direction='-x')
                    else:
                        g.move(x=(j+1)-3,y=3)
                        g.toggle_pressure(pressure_box)
                        g.feed(10)
                        g.clip(height=2, direction='-x')
                        
    for i in np.arange(2):        
        for j in np.arange(6):
                if i==0:
                    g.abs_move(x=pad_positions[j][0],y=pad_positions[j][1])
                    g.move(z=-2)
                    g.feed(speed)
                    g.toggle_pressure(pressure_box)
                    g.dwell(dwell)                    
                    g.move(x=-3)
                    if j<3:
                        g.move(x=-3,y=-3/(j+1))
                        g.toggle_pressure(pressure_box)
                        g.feed(10)
                        g.clip(height=2, direction='-x')
                    else:
                        g.move(x=-3,y=(j+1)-3)
                        g.toggle_pressure(pressure_box)
                        g.feed(10)
                        g.clip(height=2, direction='-x')
                else:
                    g.abs_move(x=pad_positions[17-j][0],y=pad_positions[17-j][1])
                    g.move(z=-2)
                    g.feed(speed)
                    g.toggle_pressure(pressure_box)
                    g.dwell(dwell) 
                    g.move(x=3)
                    if j<3:
                        g.move(x=3,y=-3/(j+1))
                        g.toggle_pressure(pressure_box)
                        g.feed(10)
                        g.clip(height=2, direction='-x')
                    else:
                        g.move(x=3,y=(j+1)-3)
                        g.toggle_pressure(pressure_box)
                        g.feed(10)
                        g.clip(height=2, direction='-x')

def LED_Harvard(speed,dwell,pressure,height):
    g.set_pressure(pressure_box, pressure)   
    g.feed(10)
    zero=0.4067
    g.abs_move(z=zero)
    g.set_home(z=0)
    g.move(z=2)
    g.abs_move(x=2,y=2)
    #g.abs_move(z=height)
    #g.toggle_pressure(pressure_box)
    #g.feed(speed)
    #g.dwell(dwell)
    
    ##first wire
    #g.move(y=33)
    #g.move(x=5)
    #g.move(y=-3)
    #g.dwell(0.7)
    #g.move(y=-0.5,z=0.5)
    #g.move(y=-0.5,z=-0.5)
    #g.move(y=-4)
    #g.dwell(0.7)
    #g.move(y=-0.5,z=0.5)
    #g.move(y=-0.5,z=-0.5)
    #g.move(y=-4)
    #g.dwell(0.7)
    #g.move(y=-0.5,z=0.5)
    #g.move(y=-0.5,z=-0.5)
    #g.move(y=-4)
    #g.dwell(0.7)
    #g.move(y=-0.5,z=0.5)
    #g.move(y=-0.5,z=-0.5)
    #g.move(y=-1)
    #g.move(x=1)
    #g.move(y=8.5)
    #g.move(x=8.5)
    #g.move(y=-9.5)
    #g.move(x=7)
    #g.move(y=-6)
    #g.dwell(0.7)
    #g.move(y=-1.3,z=0.5)
    #g.move(y=-1.3,z=-0.5)
    #g.abs_move(y=2)
    #g.toggle_pressure(pressure_box)
    #g.feed(10)
    #g.clip(height=2, direction='+x')
    #
    ##second wire
    #g.abs_move(x=2,y=2)
    #g.abs_move(z=height)
    #g.feed(speed)
    #g.toggle_pressure(pressure_box)
    #g.dwell(dwell)
    #g.move(y=3)
    #g.move(x=5)
    #g.move(y=6)
    #g.dwell(0.7)
    #g.move(y=0.5,z=0.5)
    #g.move(y=0.5,z=-0.5)
    #g.move(y=1)
    #g.move(x=1.4)
    #g.move(y=8.5)
    #g.move(x=1.5)
    #g.dwell(0.7)
    #g.move(x=0.5,z=0.5)
    #g.move(x=0.5,z=-0.5)
    #g.move(x=2.6)
    #g.dwell(0.7)
    #g.move(x=0.5,z=0.5)
    #g.move(x=0.5,z=-0.5)
    #g.move(x=1.4)
    #g.move(y=-8.5)
    #g.move(x=1.4)
    #g.move(y=-1)
    #g.dwell(0.7)
    #g.move(y=-0.5,z=0.5)
    #g.move(y=-0.5,z=-0.5)
    #g.move(y=-1)
    #g.move(x=3)
    #g.move(y=-2)
    #g.dwell(0.7)
    #g.move(y=-1.3,z=0.5)
    #g.move(y=-1.3,z=-0.5)
    #g.abs_move(y=2)
    #g.toggle_pressure(pressure_box)
    #g.feed(10)
    #g.clip(height=2, direction='+x')


    ##third wire
    #g.abs_move(x=2,y=2)
    #g.abs_move(z=height)
    #g.feed(speed)
    #g.toggle_pressure(pressure_box)
    #g.dwell(dwell)
    #g.move(y=33)
    #g.move(x=15.4)
    #g.move(y=-3)
    #g.dwell(0.7)
    #g.move(y=-0.5,z=0.5)
    #g.move(y=-0.5,z=-0.5)
    #g.move(y=-4)
    #g.dwell(0.7)
    #g.move(y=-0.5,z=0.5)
    #g.move(y=-0.5,z=-0.5)
    #g.move(y=-4)
    #g.dwell(0.7)
    #g.move(y=-0.5,z=0.5)
    #g.move(y=-0.5,z=-0.5)
    #g.move(y=-4)
    #g.dwell(0.7)
    #g.move(y=-0.5,z=0.5)
    #g.move(y=-0.5,z=-0.5)
    #g.move(y=-1)
    #g.move(x=9)
    #g.move(y=-7)
    #g.dwell(0.7)
    #g.move(y=-1.3,z=0.5)
    #g.move(y=-1.3,z=-0.5)
    #g.abs_move(y=2)
    #g.toggle_pressure(pressure_box)
    #g.feed(10)
    #g.clip(height=2, direction='+x')

    #anode/cathode
    g.abs_move(z=height)
    g.feed(speed)
    g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.move(x=2)
    g.arc(x=-4,y=0,radius=2)
    g.arc(x=4,y=0,radius=2)
    g.move(x=-0.2)
    g.arc(x=-3.6,y=0,radius=1.8)
    g.arc(x=3.6,y=0,radius=1.8)
    g.move(x=-0.2)
    g.arc(x=-3.2,y=0,radius=1.6)
    g.arc(x=3.2,y=0,radius=1.6)
    g.move(x=-0.2)
    g.arc(x=-2.8,y=0,radius=1.4)
    g.arc(x=2.8,y=0,radius=1.4)
    g.move(x=-0.2)
    g.arc(x=-2.4,y=0,radius=1.2)
    g.arc(x=2.4,y=0,radius=1.2)
    g.move(x=-0.2)
    g.arc(x=-2.0,y=0,radius=1)
    g.arc(x=2.0,y=0,radius=1)
    g.move(x=-0.2)
    g.arc(x=-1.6,y=0,radius=0.8)
    g.arc(x=1.6,y=0,radius=0.8)
    g.move(x=-0.2)
    g.arc(x=-1.2,y=0,radius=0.6)
    g.arc(x=1.2,y=0,radius=0.6)
    g.move(x=-0.2)
    g.arc(x=-0.8,y=0,radius=0.4)
    g.arc(x=0.8,y=0,radius=0.4)
    g.move(x=-0.2)
    g.arc(x=-0.4,y=0,radius=0.2)
    g.arc(x=0.4,y=0,radius=0.2)
    g.move(x=-0.2)
    g.move(x=2,z=0.03)
    g.arc(x=-4,y=0,radius=2)
    g.arc(x=4,y=0,radius=2)
    g.move(x=-0.2)
    g.arc(x=-3.6,y=0,radius=1.8)
    g.arc(x=3.6,y=0,radius=1.8)
    g.move(x=-0.2)
    g.arc(x=-3.2,y=0,radius=1.6)
    g.arc(x=3.2,y=0,radius=1.6)
    g.move(x=-0.2)
    g.arc(x=-2.8,y=0,radius=1.4)
    g.arc(x=2.8,y=0,radius=1.4)
    g.move(x=-0.2)
    g.arc(x=-2.4,y=0,radius=1.2)
    g.arc(x=2.4,y=0,radius=1.2)
    g.move(x=-0.2)
    g.arc(x=-2.0,y=0,radius=1)
    g.arc(x=2.0,y=0,radius=1)
    g.move(x=-0.2)
    g.arc(x=-1.6,y=0,radius=0.8)
    g.arc(x=1.6,y=0,radius=0.8)
    g.move(x=-0.2)
    g.arc(x=-1.2,y=0,radius=0.6)
    g.arc(x=1.2,y=0,radius=0.6)
    g.move(x=-0.2)
    g.arc(x=-0.8,y=0,radius=0.4)
    g.arc(x=0.8,y=0,radius=0.4)
    g.move(x=-0.2)
    g.arc(x=-0.4,y=0,radius=0.2)
    g.arc(x=0.4,y=0,radius=0.2)
    g.move(x=-0.2)
    
    g.toggle_pressure(pressure_box)
    g.feed(10)
    g.clip(height=2, direction='+x')
    


#print_die(speed=1.4,dwell=0.1)
#print_die_wiring(speed=0.25,dwell=0.1)
LED_Harvard(speed=0.3,dwell=1.5,pressure=80,height=0.08)

g.view(backend='matplotlib')

g.teardown() 