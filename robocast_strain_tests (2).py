from mecode import G
import numpy as np

outfile = r"C:\Users\Aerosol Jet\Desktop\Valentine\my_print.pgm"


g=G(
    direct_write=False,
    outfile=outfile,
    header=r"C:\Users\Aerosol Jet\Documents\GitHub\AFRL-printing\mymegacasterheader.txt",
    footer=r"C:\Users\Aerosol Jet\Documents\GitHub\AFRL-printing\mymegacasterfooter.txt",
    print_lines=False,
    aerotech_include=False,
)

L=24 #length at strain = 0%

def slow_test(strain,initdwell, enddwell,speed = 0.1):
    dist=L*strain
    g.feed(speed)
    g.dwell(initdwell)
    g.move(x=-dist)
    g.move(x=dist)
    g.dwell(enddwell)

def cyclic_test(strain, freq,mydwell ,cycles=100):
    dist=L*strain
    speed=freq*dist*2
    g.feed(speed)
    g.dwell(mydwell)
    for i in range(cycles):
        g.move(-dist)
        g.move(dist)
    g.dwell(mydwell)
    
g.set_home(x=0, y=0, z=0)

slow_test(strain=0.5,initdwell=10,enddwell=60)
#cyclic_test(strain=0.5, freq=0.1, cycles = 20, mydwell=120)
#cyclic_test(strain=0.6, freq=0.1, cycles = 20, mydwell=120)
#cyclic_test(strain=0.7, freq=0.1, cycles = 20, mydwell=120)
#cyclic_test(strain=0.8, freq=0.1, cycles = 20, mydwell=120)
#cyclic_test(strain=0.9, freq=0.1, cycles = 20, mydwell=120)
#cyclic_test(strain=1.0, freq=0.1, cycles = 20, mydwell=120)

#cyclic_test(strain=0.3, freq=0.1)

#g.view(backend='matplotlib')


g.teardown()