from mecode import G
import numpy as np
#from aerotech_automator import AerotechAutomator
#
#outfile = r"/Volumes/jlewis/User Files/Valentine/AFRL/my_print.pgm"
#
##List of axes used for printing - comment out the axes not being used
#AXES_USED = ['A',
#            'B',
#            'C', 
#            #'D'
#            ]
#
##Defining positions of axes
#AXES_DATA = {
#    'A': {
#        'number': 4,
#        'alignment_location': (586.075, 367.82),
#    },
#    'B': {
#        'number': 5,
#        'alignment_location': (482.075, 367.82),
#    },
#    'C': {
#        'number': 6,
#        'alignment_location': (378.075, 367.82),
#    },
#    'D': {
#        'number': 7,
#        'alignment_location': (299.075, 367.82),
#    },
#}
#
##Defining substrate location and profilometry mesh size
#SUBSTRATES = {
#    'slide1': {
#        'origin': (199.57,118),
#        'size': 'auto',
#        'profile': True,
#        'profile-spacing': (5, 5),
#    },
#}
##Defining profilometry parameters
#automator = AerotechAutomator(
#    calfile_path='C:\Users\Lewis Group\Desktop\Calibration\CAL_output.cal',
#    axes=AXES_USED,
#    axes_data = AXES_DATA,
#    substrates = SUBSTRATES,
#)



g=G(
    direct_write=False,
    #outfile=outfile,
    #header=header,
    #footer=footer,
    print_lines=False,
)



###INSERT GCODE FROM SLIC3R HERE#####


g.view()

g.teardown()