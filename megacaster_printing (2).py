from mecode import G
import numpy as np

outfile = r"/Volumes/group0/jlewis/User Files/Valentine/AFRL/my_print.pgm"

#myz = 2.82357
g=G(
    direct_write=False,
    outfile=r'C:\Users\Aerosol Jet\Documents\myprint.pgm',
    header=r'C:\Users\Aerosol Jet\Documents\GitHub\MEGACASTER_PRINTING\mymegacasterheader.txt',
    footer=r'C:\Users\Aerosol Jet\Documents\GitHub\MEGACASTER_PRINTING\mymegacasterfooter.txt',
    print_lines=False,
    aerotech_include=False,
)

pad_positions=((0.1,0.38+0.28*0),(.1,0.38+0.28*1),(.1,0.38+0.28*2),(.1,0.38+0.28*3),(.1,0.38+0.28*4),(.1,0.38+0.28*5),
(0.38+0.28*0,2.06),(0.38+0.28*1,2.06),(0.38+0.28*2,2.06),(0.38+0.28*3,2.06),(0.38+0.28*4,2.06),(0.38+0.28*5,2.06),
(2.06,0.38+0.28*5),(2.06,0.38+0.28*4),(2.06,0.38+0.28*3),(2.06,0.38+0.28*2),(2.06,0.38+0.28*1),(2.06,0.38+0.28*0),
(0.38+0.28*5,0.1),(0.38+0.28*4,0.1),(0.38+0.28*3,0.1),(0.38+0.28*2,0.1),(0.38+0.28*1,0.1),(0.38+0.28*0,0.1))

well_position = ((10.5, 25.245), (24, 25.245), (37.5, 25.245), (51, 25.245), 
                       (10.5, 24.245), (24, 24.245), (37.5, 24.245), (51, 24.245))


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
    zero=0.0
    g.abs_move(z=zero)
    g.set_home(x=0,y=0,z=0)
    g.move(z=2)
    g.abs_move(x=2,y=2)
    g.abs_move(z=height)
    g.toggle_pressure(pressure_box)
    g.feed(speed)
    g.dwell(dwell)
    
    #first wire
    g.move(y=33)
    g.move(x=5)
    g.move(y=-2.6)
    g.dwell(dwell)
    g.move(y=-0.8,z=1)
    g.move(y=-0.8,z=-1)
    g.move(y=-3.2)
    g.dwell(dwell)
    g.move(y=-0.8,z=1)
    g.move(y=-0.8,z=-1)
    g.move(y=-3.2)
    g.dwell(dwell)
    g.move(y=-0.8,z=1)
    g.move(y=-0.8,z=-1)
    g.move(y=-3.2)
    g.dwell(dwell)
    g.move(y=-0.8,z=1)
    g.move(y=-0.8,z=-1)
    g.move(y=-0.6)
    g.move(x=0.9)
    g.move(y=8.5)
    g.move(x=8.5)
    g.move(y=-10.)
    g.move(x=7)
    g.move(y=-5.8)
    g.dwell(dwell)
    g.move(y=-1.3,z=1)
    g.move(y=-1.3,z=-1)
    g.abs_move(y=2)
    g.toggle_pressure(pressure_box)
    g.feed(10)
    g.clip(height=2, direction='+x')
    #
    ##second wire
    g.abs_move(x=2,y=2)
    g.abs_move(z=height)
    g.feed(speed)
    g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.move(y=3)
    g.move(x=5)
    g.move(y=6.2)
    g.dwell(dwell)
    g.move(y=0.8,z=1)
    g.move(y=0.8,z=-1)
    g.move(y=1.2)
    g.move(x=1.6)
    g.move(y=8)
    g.move(x=1.25)
    g.dwell(dwell)
    g.move(x=0.8,z=1)
    g.move(x=0.8,z=-1)
    g.move(x=1.4)
    g.dwell(dwell)
    g.move(x=0.8,z=1)
    g.move(x=0.8,z=-1)
    g.move(x=1.25)
    g.move(y=-8.5)
    g.move(x=1.4)
    g.move(y=-0.6)
    g.dwell(dwell)
    g.move(y=-0.8,z=1)
    g.move(y=-0.8,z=-1)
    g.move(y=-0.6)
    g.move(x=3)
    g.move(y=-2)
    g.dwell(dwell)
    g.move(y=-1.3,z=1)
    g.move(y=-1.3,z=-1)
    g.abs_move(y=2)
    g.move(x=3)
    g.toggle_pressure(pressure_box)
    g.feed(10)
    g.clip(height=2, direction='+x')


    ##third wire
    g.abs_move(x=2,y=2)
    g.abs_move(z=height)
    g.feed(speed)
    g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.move(y=33)
    g.move(x=15.4)
    g.move(y=-2.6)
    g.dwell(dwell)
    g.move(y=-0.8,z=1)
    g.move(y=-0.8,z=-1)
    g.move(y=-3.2)
    g.dwell(dwell)
    g.move(y=-0.8,z=1)
    g.move(y=-0.8,z=-1)
    g.move(y=-3.2)
    g.dwell(dwell)
    g.move(y=-0.8,z=1)
    g.move(y=-0.8,z=-1)
    g.move(y=-3.2)
    g.dwell(dwell)
    g.move(y=-0.8,z=1)
    g.move(y=-0.8,z=-1)
    g.move(y=-0.8)
    g.move(x=9)
    g.move(y=-7)
    g.dwell(dwell)
    g.move(y=-1.3,z=1)
    g.move(y=-1.3,z=-1)
    g.abs_move(y=2)
    #g.toggle_pressure(pressure_box)
    #g.feed(10)
    #g.clip(height=2, direction='+x')

    #anode/cathode
    g.feed(speed*0.4)
    g.move(x=-1.5)  
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

    g.abs_move(x=2,y=2)
    g.abs_move(z=height)
    g.feed(speed*0.4)
    g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.move(x=1.4)
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


def LED_line(speed,dwell,pressure,height):
    g.set_pressure(pressure_box, pressure)   
    g.feed(10)
    zero=0.0
    g.abs_move(z=zero)
    g.set_home(x=0,y=0,z=0)
    g.move(z=5)
    g.dwell(5)
    

    #wire
    g.abs_move(x=2,y=2)
    g.abs_move(z=height)
    g.feed(speed)
    g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.move(y=-5)
    #g.move(y=-2)
    g.move(y=-0.5,z=1.5)
    g.move(y=-0.5,z=-1.5)
    g.move(y=-2)
    g.dwell(0.1)
    g.move(y=-0.5,z=1.5)
    g.move(y=-0.5,z=-1.5)
    g.move(y=-2)
    g.dwell(0.1)
    g.move(y=-0.5,z=1.5)
    g.move(y=-0.5,z=-1.5)
    g.move(y=-2)
    g.dwell(0.1)
    g.move(y=-0.5,z=1.5)
    g.move(y=-0.5,z=-1.5)
    g.move(y=-5)
    
    #g.move(x=2)
    #g.move(y=-1)
    #g.dwell(0.7)
    #g.move(y=-1.3,z=0.5)
    #g.move(y=-1.3,z=-0.5)
    #g.move(y=-1)
    #g.move(x=-2)
    #g.move(y=-2)
    g.move(x=-2)
    g.feed(speed*0.4)
    g.abs_move(z=height+0.05)
    g.move(x=1.4)  
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
    
    g.move(y=20)
    
    g.abs_move(z=height+0.05)
    g.feed(speed)
    g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.feed(speed*0.4)
    g.move(x=1.4)  
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

def stacked_rectangle(x, y, layer_height, layers, nozzle = 'Z'):
    
    for i in range(layers):
        g.move(x=x)
        g.move(y=-y)
        g.move(x=-x)
        g.move(y=y)
        g.move(**{nozzle:layer_height})

def print_single_well(x, y, layer_height, layers, speed, pressure, filament = 1, nozzle = 'Z'):
    g.feed(speed)
    g.set_pressure(pressure_box, pressure)   
    g.toggle_pressure(pressure_box)
    g.dwell(0.25)
    stacked_rectangle(x=x, y=y, layer_height = layer_height, layers = layers, nozzle = nozzle)
    g.toggle_pressure(pressure_box)

def print_all_single_wells(layer_height, layer_increments, total_increments, pressure, speed, nozzle):
    #
    for i in range(0,2):      
        g.feed(15)
        g.abs_move(*well_position[i])
        g.abs_move(**{nozzle:0.05})
        print_single_well(x = 12.5, y = -14, layer_height = layer_height ,  layers = layer_increments, speed = speed, pressure = pressure, filament = 1, nozzle = nozzle)
        g.clip(axis=nozzle, direction='+y', height=3)
    
    #for i in range(4,8):      
    #    g.feed(15)
    #    g.abs_move(*well_position[i])
    #    g.abs_move(**{nozzle:0.05})
    #    print_single_well(x = 12.5, y = 14, layer_height = layer_height ,  layers = layer_increments, speed = speed, pressure = pressure, filament = 1, nozzle = nozzle)
    #    g.clip(axis=nozzle, direction='-y', height=3)
     
    count = 0
    repeats = (total_increments)-1     
    
    
    for i in range(repeats-1):
        
        count = count + layer_increments
        for i in range(0,2):
           
            g.feed(15)
            g.abs_move(*well_position[i])
            g.abs_move(**{nozzle:(15*count*layer_height)/(repeats)})
            print_single_well(x = 12.5, y = -14, layer_height = layer_height ,  layers = layer_increments, speed = speed, pressure = pressure, filament = 1, nozzle = nozzle)
            g.clip(axis=nozzle, direction='+y', height=3)

        print count 
        print count*layer_height
        print (15*count*layer_height)/(repeats)
       
        #for i in range(4,8):      
        #    g.feed(15)
        #    g.abs_move(*well_position[i])
        #    g.abs_move(**{nozzle:count*layer_height})
        #    print_single_well(x = 12.5, y = 14, layer_height = layer_height ,  layers = layer_increments, speed = speed, pressure = pressure, filament = 1, nozzle = nozzle)
        #    g.clip(axis=nozzle, direction='-y', height=3)





#print_die(speed=1.4,dwell=0.1)
#print_die_wiring(speed=0.25,dwell=0.1)
#LED_Harvard(speed=2,dwell=0.1,pressure=36,height=0.06)
#LED_line(speed=4,dwell=1.5,pressure=15,height=0.04)

g.set_home(x=0,y=0,z=0)
print_all_single_wells(layer_height = 0.04, layer_increments=5, total_increments=20, pressure=32, speed=5, nozzle = 'Z')


#g.view(backend='matplotlib')

g.teardown() 