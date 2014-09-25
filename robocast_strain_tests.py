from mecode import G
import numpy as np

outfile = r"/Volumes/jlewis/User Files/Valentine/AFRL/my_print.pgm"


g=G(
    direct_write=False,
    outfile=outfile,
    header=r"/Users/alex/alexvalentine/AFRL-printing/mymegacasterheader.txt",
    footer=r"/Users/alex/alexvalentine/AFRL-printing/mymegacasterfooter.txt",
    print_lines=False,
    aerotech_include=False,
)

L=50 #length at strain = 0%

def slow_test(strain,speed = 0.1, mydwell=60):
    dist=L*strain
    g.feed(speed)
    g.dwell(mydwell)
    g.move(-dist)
    g.move(dist)
    g.dwell(mydwell)

def cyclic_test(strain, freq, cycles=100, mydwell=60):
    dist=L*strain
    speed=freq*dist*2
    g.feed(speed)
    g.dwell(mydwell)
    for i in range(cycles):
        g.move(-dist)
        g.move(dist)
    #g.dwell(mydwell)
    
g.set_home(x=0, y=0, z=0)

#slow_test(strain=0.3)
cyclic_test(strain=0.5, freq=0.1, cycles = 20, mydwell=120)
cyclic_test(strain=0.6, freq=0.1, cycles = 20, mydwell=120)
cyclic_test(strain=0.7, freq=0.1, cycles = 20, mydwell=120)
cyclic_test(strain=0.8, freq=0.1, cycles = 20, mydwell=120)
cyclic_test(strain=0.9, freq=0.1, cycles = 20, mydwell=120)
cyclic_test(strain=1.0, freq=0.1, cycles = 20, mydwell=120)

#cyclic_test(strain=0.3, freq=0.1)



g.teardown()