from mecode import G
import numpy as np

g=G(print_lines=False)


g.meander(x=5, y=5, spacing=0.1)  # trace a rectangle meander with 1mm spacing between the passes


g.view()

g.teardown()