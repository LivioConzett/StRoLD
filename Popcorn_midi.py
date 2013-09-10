#Popcorn midi

import pygame
import pygame.midi
from time import sleep

#midi notes
c0 = 36
cis0 =37
d0 = 38
dis0 =39 
e0 =40
f0 = 41
fis0 =42
g0 = 43
gis0 =44 
a0 =45
b0 =46
h0 = 47

c1 = 48
cis1 = 49
d1 = 50
dis1 = 51
e1 =52
f1 = 53
fis1 =54
g1 = 55
gis1 = 56
a1 =57
b1 =58
h1 = 59

c2 = 60
cis2 = 61
d2 = 62
dis2 = 63
e2 =64
f2 = 65
fis2 =66
g2 = 67
gis2 = 68
a2 =69
b2 =70
h2 = 71

c3 = 72
cis3 = 73
d3 = 74
dis3 = 75
e3 =76
f3 = 77
fis3 =78
g3 = 79
gis3 = 80
a3 =81
b3 =82
h3 =83

c4 = 84
cis4 = 85
d4 = 86
dis4 = 87
e4 =88
f4 = 89
fis4 =90
g4 = 91
gis4 = 92
a4 =93
b4 =94
h4 =95

c5 = 96
cis5 = 97
d5 = 98
dis5 = 99
e5 =100
f5 = 101
fis5 =102
g5 = 103
gis5 = 104
a5 =105
b5 =106
h5 =107

#instruments
GRAND_PIANO = 0
COOL_ORGAN = 4
BELLS = 8
BRIGHT_BELLS = 9
XYLOPHONE = 12
CHURCH_ORGAN = 19
EL_XYLOPHONE = 24
EL_BELLS = 46
EL_ORGAN = 71


pygame.init()
pygame.midi.init()
port = pygame.midi.get_default_output_id()
midi_out = pygame.midi.Output(port, 0)
midi_out.set_instrument(GRAND_PIANO)

#===================================1
midi_out.note_on(h0,100)
sleep(.25)
midi_out.note_off(h0,100)

midi_out.note_on(h1,100)
sleep(.125)
midi_out.note_off(h1,100)

midi_out.note_on(fis1,100)
sleep(.125)
midi_out.note_off(fis1,100)

midi_out.note_on(h0,100)
sleep(.25)
midi_out.note_off(h0,100)

midi_out.note_on(h1,100)
sleep(.125)
midi_out.note_off(h1,100)

midi_out.note_on(fis1,100)
sleep(.125)
midi_out.note_off(fis1,100)

midi_out.note_on(h0,100)
sleep(.25)
midi_out.note_off(h0,100)

midi_out.note_on(h1,100)
sleep(.125)
midi_out.note_off(h1,100)

midi_out.note_on(fis1,100)
sleep(.125)
midi_out.note_off(fis1,100)

midi_out.note_on(h0,100)
sleep(.125)
midi_out.note_off(h0,100)

midi_out.note_on(d1,100)
sleep(.125)
midi_out.note_off(d1,100)

midi_out.note_on(fis1,100)
sleep(.125)
midi_out.note_off(fis1,100)

midi_out.note_on(a1,100)
sleep(.125)
midi_out.note_off(a1,100)

#=============================2
midi_out.note_on(h0,100)
sleep(.25)
midi_out.note_off(h0,100)

midi_out.note_on(h1,100)
sleep(.125)
midi_out.note_off(h1,100)

midi_out.note_on(fis1,100)
sleep(.125)
midi_out.note_off(fis1,100)

midi_out.note_on(h0,100)
sleep(.25)
midi_out.note_off(h0,100)

midi_out.note_on(h1,100)
sleep(.125)
midi_out.note_off(h1,100)

midi_out.note_on(fis1,100)
sleep(.125)
midi_out.note_off(fis1,100)

midi_out.note_on(h0,100)
sleep(.25)
midi_out.note_off(h0,100)

midi_out.note_on(h1,100)
sleep(.125)
midi_out.note_off(h1,100)

midi_out.note_on(fis1,100)
sleep(.125)
midi_out.note_off(fis1,100)

midi_out.note_on(h0,100)
sleep(.125)
midi_out.note_off(h0,100)

midi_out.note_on(d1,100)
sleep(.125)
midi_out.note_off(d1,100)

midi_out.note_on(fis1,100)
sleep(.125)
midi_out.note_off(fis1,100)

midi_out.note_on(a1,100)
sleep(.125)
midi_out.note_off(a1,100)

#=============================3
midi_out.note_on(h0,100)
sleep(.25)
midi_out.note_off(h0,100)

midi_out.note_on(h1,100)
sleep(.125)
midi_out.note_off(h1,100)

midi_out.note_on(fis1,100)
sleep(.125)
midi_out.note_off(fis1,100)

midi_out.note_on(h0,100)
sleep(.25)
midi_out.note_off(h0,100)

midi_out.note_on(h1,100)
sleep(.125)
midi_out.note_off(h1,100)

midi_out.note_on(fis1,100)
sleep(.125)
midi_out.note_off(fis1,100)

midi_out.note_on(h0,100)
sleep(.25)
midi_out.note_off(h0,100)

midi_out.note_on(h1,100)
sleep(.125)
midi_out.note_off(h1,100)

midi_out.note_on(fis1,100)
sleep(.125)
midi_out.note_off(fis1,100)

midi_out.note_on(h0,100)
sleep(.125)
midi_out.note_off(h0,100)

midi_out.note_on(d1,100)
sleep(.125)
midi_out.note_off(d1,100)

midi_out.note_on(fis1,100)
sleep(.125)
midi_out.note_off(fis1,100)

midi_out.note_on(a1,100)
sleep(.125)
midi_out.note_off(a1,100)

#=============================4
midi_out.note_on(h0,100)
sleep(.25)
midi_out.note_off(h0,100)

midi_out.note_on(h1,100)
sleep(.125)
midi_out.note_off(h1,100)

midi_out.note_on(fis1,100)
sleep(.125)
midi_out.note_off(fis1,100)

midi_out.note_on(h0,100)
sleep(.25)
midi_out.note_off(h0,100)

midi_out.note_on(h1,100)
sleep(.125)
midi_out.note_off(h1,100)

midi_out.note_on(fis1,100)
sleep(.125)
midi_out.note_off(fis1,100)

midi_out.note_on(h0,100)
sleep(.25)
midi_out.note_off(h0,100)

midi_out.note_on(h1,100)
sleep(.125)
midi_out.note_off(h1,100)

midi_out.note_on(fis1,100)
sleep(.125)
midi_out.note_off(fis1,100)

midi_out.note_on(h0,100)
midi_out.note_on(h3,127)
sleep(.125)
midi_out.note_off(h0,100)

midi_out.note_on(d1,100)
sleep(.125)
midi_out.note_off(d1,100)
midi_out.note_off(h3,127)

midi_out.note_on(fis1,100)
midi_out.note_on(a3,127)
sleep(.125)
midi_out.note_off(fis1,100)

midi_out.note_on(a1,100)
sleep(.125)
midi_out.note_off(a3,127)
midi_out.note_off(a1,100)

#=============================5

midi_out.note_on(h0,100)
midi_out.note_on(h3,127)
sleep(.25)
midi_out.note_off(h0,100)
midi_out.note_off(h3,127)

midi_out.note_on(h1,100)
midi_out.note_on(fis3,127)
sleep(.125)
midi_out.note_off(h1,100)

midi_out.note_on(fis1,100)
sleep(.125)
midi_out.note_off(fis1,100)
midi_out.note_off(fis3,127)

midi_out.note_on(h0,100)
midi_out.note_on(d3,127)
sleep(.25)
midi_out.note_off(h0,100)
midi_out.note_off(d3,127)

midi_out.note_on(h1,100)
midi_out.note_on(fis3,127)
sleep(.125)
midi_out.note_off(h1,100)

midi_out.note_on(fis1,100)
sleep(.125)
midi_out.note_off(fis1,100)
midi_out.note_off(fis3,127)

midi_out.note_on(h0,100)
midi_out.note_on(h2,127)
sleep(.25)
midi_out.note_off(h0,100)

midi_out.note_on(h1,100)
sleep(.125)
midi_out.note_off(h1,100)

midi_out.note_on(fis1,100)
sleep(.125)
midi_out.note_off(fis1,100)
midi_out.note_off(h2,127)

midi_out.note_on(h0,100)
midi_out.note_on(h3,127)
sleep(.125)
midi_out.note_off(h0,100)

midi_out.note_on(d1,100)
sleep(.125)
midi_out.note_off(d1,100)
midi_out.note_off(h3,127)

midi_out.note_on(fis1,100)
midi_out.note_on(a3,127)
sleep(.125)
midi_out.note_off(fis1,100)

midi_out.note_on(a1,100)
sleep(.125)
midi_out.note_off(a1,100)
midi_out.note_off(a3,127)

#===================================6
midi_out.note_on(h0,100)
midi_out.note_on(h3,127)
sleep(.25)
midi_out.note_off(h0,100)
midi_out.note_off(h3,127)

midi_out.note_on(h1,100)
midi_out.note_on(fis3,127)
sleep(.125)
midi_out.note_off(h1,100)

midi_out.note_on(fis1,100)
sleep(.125)
midi_out.note_off(fis1,100)
midi_out.note_off(fis3,127)

midi_out.note_on(h0,100)
midi_out.note_on(d3,127)
sleep(.25)
midi_out.note_off(h0,100)
midi_out.note_off(d3,127)

midi_out.note_on(h1,100)
midi_out.note_on(fis3,127)
sleep(.125)
midi_out.note_off(h1,100)

midi_out.note_on(fis1,100)
sleep(.125)
midi_out.note_off(fis1,100)
midi_out.note_off(fis3,127)

midi_out.note_on(h0,100)
midi_out.note_on(h2,127)
sleep(.25)
midi_out.note_off(h0,100)

midi_out.note_on(h1,100)
sleep(.125)
midi_out.note_off(h1,100)

midi_out.note_on(fis1,100)
sleep(.125)
midi_out.note_off(fis1,100)
midi_out.note_off(h2,127)

midi_out.note_on(h0,100)
midi_out.note_on(h3,127)
sleep(.125)
midi_out.note_off(h0,100)

midi_out.note_on(d1,100)
sleep(.125)
midi_out.note_off(d1,100)
midi_out.note_off(h3,127)

midi_out.note_on(fis1,100)
midi_out.note_on(cis4,127)
sleep(.125)
midi_out.note_off(fis1,100)

midi_out.note_on(a1,100)
sleep(.125)
midi_out.note_off(a1,100)
midi_out.note_off(cis3,127)

#===================================7
midi_out.note_on(h0,100)
midi_out.note_on(d4,127)
sleep(.25)
midi_out.note_off(h0,100)
midi_out.note_off(d4,127)

midi_out.note_on(h1,100)
midi_out.note_on(cis4,127)
sleep(.125)
midi_out.note_off(h1,100)

midi_out.note_on(fis1,100)
sleep(.125)
midi_out.note_off(fis1,100)
midi_out.note_off(cis4,127)

midi_out.note_on(h0,100)
midi_out.note_on(d4,127)
sleep(.125)
midi_out.note_off(h0,100)

midi_out.note_on(d1,100)
sleep(.125)
midi_out.note_off(d1,100)
midi_out.note_off(d4,127)

midi_out.note_on(fis1,100)
midi_out.note_on(h3,127)
sleep(.125)
midi_out.note_off(fis1,100)

midi_out.note_on(a1,100)
sleep(.125)
midi_out.note_off(a1,100)
midi_out.note_off(h3,127)

midi_out.note_on(a0,100)
midi_out.note_on(cis4,127)
sleep(.25)
midi_out.note_off(a0,100)
midi_out.note_off(cis4,127)

midi_out.note_on(c1,100)
midi_out.note_on(h3,127)
sleep(.125)
midi_out.note_off(c1,100)

midi_out.note_on(e1,100)
sleep(.125)
midi_out.note_off(e1,100)
midi_out.note_off(h3,127)

midi_out.note_on(a0,100)
midi_out.note_on(cis4,127)
sleep(.125)
midi_out.note_off(a0,100)

midi_out.note_on(c1,100)
sleep(.125)
midi_out.note_off(c1,100)
midi_out.note_off(cis4,127)

midi_out.note_on(e1,100)
midi_out.note_on(a3,127)
sleep(.125)
midi_out.note_off(e1,100)

midi_out.note_on(a1,100)
sleep(.125)
midi_out.note_off(a1,100)
midi_out.note_off(a3,127)

#===================================8
midi_out.note_on(g0,100)
midi_out.note_on(h3,127)
sleep(.25)
midi_out.note_off(g0,100)
midi_out.note_off(h3,127)

midi_out.note_on(g1,100)
midi_out.note_on(a3,127)
sleep(.125)
midi_out.note_off(g1,100)

midi_out.note_on(d1,100)
sleep(.125)
midi_out.note_off(d1,100)
midi_out.note_off(a3,127)

midi_out.note_on(g0,100)
midi_out.note_on(h3,127)
sleep(.125)
midi_out.note_off(g0,100)

midi_out.note_on(h1,100)
sleep(.125)
midi_out.note_off(h1,100)
midi_out.note_off(h3,127)

midi_out.note_on(d1,100)
midi_out.note_on(g3,127)
sleep(.125)
midi_out.note_off(d1,100)

midi_out.note_on(g1,100)
sleep(.125)
midi_out.note_off(g1,100)
midi_out.note_off(g3,127)

midi_out.note_on(h0,100)
midi_out.note_on(h3,127)
sleep(.25)
midi_out.note_off(h0,100)

midi_out.note_on(h1,100)
sleep(.125)
midi_out.note_off(h1,100)

midi_out.note_on(fis1,100)
sleep(.125)
midi_out.note_off(fis1,100)
midi_out.note_off(h3,127)

midi_out.note_on(h0,100)
midi_out.note_on(h3,127)
sleep(.125)
midi_out.note_off(h0,100)

midi_out.note_on(d1,100)
sleep(.125)
midi_out.note_off(d1,100)
midi_out.note_off(h3,127)

midi_out.note_on(fis1,100)
midi_out.note_on(a3,127)
sleep(.125)
midi_out.note_off(fis1,100)

midi_out.note_on(a1,100)
sleep(.125)
midi_out.note_off(a3,127)
midi_out.note_off(a1,100)

#===============================5

midi_out.note_on(h0,100)
midi_out.note_on(h3,127)
sleep(.25)
midi_out.note_off(h0,100)
midi_out.note_off(h3,127)

midi_out.note_on(h1,100)
midi_out.note_on(fis3,127)
sleep(.125)
midi_out.note_off(h1,100)

midi_out.note_on(fis1,100)
sleep(.125)
midi_out.note_off(fis1,100)
midi_out.note_off(fis3,127)

midi_out.note_on(h0,100)
midi_out.note_on(d3,127)
sleep(.25)
midi_out.note_off(h0,100)
midi_out.note_off(d3,127)

midi_out.note_on(h1,100)
midi_out.note_on(fis3,127)
sleep(.125)
midi_out.note_off(h1,100)

midi_out.note_on(fis1,100)
sleep(.125)
midi_out.note_off(fis1,100)
midi_out.note_off(fis3,127)

midi_out.note_on(h0,100)
midi_out.note_on(h2,127)
sleep(.25)
midi_out.note_off(h0,100)

midi_out.note_on(h1,100)
sleep(.125)
midi_out.note_off(h1,100)

midi_out.note_on(fis1,100)
sleep(.125)
midi_out.note_off(fis1,100)
midi_out.note_off(h2,127)

midi_out.note_on(h0,100)
midi_out.note_on(h3,127)
sleep(.125)
midi_out.note_off(h0,100)

midi_out.note_on(d1,100)
sleep(.125)
midi_out.note_off(d1,100)
midi_out.note_off(h3,127)

midi_out.note_on(fis1,100)
midi_out.note_on(a3,127)
sleep(.125)
midi_out.note_off(fis1,100)

midi_out.note_on(a1,100)
sleep(.125)
midi_out.note_off(a1,100)
midi_out.note_off(a3,127)

#===================================6
midi_out.note_on(h0,100)
midi_out.note_on(h3,127)
sleep(.25)
midi_out.note_off(h0,100)
midi_out.note_off(h3,127)

midi_out.note_on(h1,100)
midi_out.note_on(fis3,127)
sleep(.125)
midi_out.note_off(h1,100)

midi_out.note_on(fis1,100)
sleep(.125)
midi_out.note_off(fis1,100)
midi_out.note_off(fis3,127)

midi_out.note_on(h0,100)
midi_out.note_on(d3,127)
sleep(.25)
midi_out.note_off(h0,100)
midi_out.note_off(d3,127)

midi_out.note_on(h1,100)
midi_out.note_on(fis3,127)
sleep(.125)
midi_out.note_off(h1,100)

midi_out.note_on(fis1,100)
sleep(.125)
midi_out.note_off(fis1,100)
midi_out.note_off(fis3,127)

midi_out.note_on(h0,100)
midi_out.note_on(h2,127)
sleep(.25)
midi_out.note_off(h0,100)

midi_out.note_on(h1,100)
sleep(.125)
midi_out.note_off(h1,100)

midi_out.note_on(fis1,100)
sleep(.125)
midi_out.note_off(fis1,100)
midi_out.note_off(h2,127)

midi_out.note_on(h0,100)
midi_out.note_on(h3,127)
sleep(.125)
midi_out.note_off(h0,100)

midi_out.note_on(d1,100)
sleep(.125)
midi_out.note_off(d1,100)
midi_out.note_off(h3,127)

midi_out.note_on(fis1,100)
midi_out.note_on(cis4,127)
sleep(.125)
midi_out.note_off(fis1,100)

midi_out.note_on(a1,100)
sleep(.125)
midi_out.note_off(a1,100)
midi_out.note_off(cis3,127)

#===================================7
midi_out.note_on(h0,100)
midi_out.note_on(d4,127)
sleep(.25)
midi_out.note_off(h0,100)
midi_out.note_off(d4,127)

midi_out.note_on(h1,100)
midi_out.note_on(cis4,127)
sleep(.125)
midi_out.note_off(h1,100)

midi_out.note_on(fis1,100)
sleep(.125)
midi_out.note_off(fis1,100)
midi_out.note_off(cis4,127)

midi_out.note_on(h0,100)
midi_out.note_on(d4,127)
sleep(.125)
midi_out.note_off(h0,100)

midi_out.note_on(d1,100)
sleep(.125)
midi_out.note_off(d1,100)
midi_out.note_off(d4,127)

midi_out.note_on(fis1,100)
midi_out.note_on(h3,127)
sleep(.125)
midi_out.note_off(fis1,100)

midi_out.note_on(a1,100)
sleep(.125)
midi_out.note_off(a1,100)
midi_out.note_off(h3,127)

midi_out.note_on(a0,100)
midi_out.note_on(cis4,127)
sleep(.25)
midi_out.note_off(a0,100)
midi_out.note_off(cis4,127)

midi_out.note_on(c1,100)
midi_out.note_on(h3,127)
sleep(.125)
midi_out.note_off(c1,100)

midi_out.note_on(e1,100)
sleep(.125)
midi_out.note_off(e1,100)
midi_out.note_off(h3,127)

midi_out.note_on(a0,100)
midi_out.note_on(cis4,127)
sleep(.125)
midi_out.note_off(a0,100)

midi_out.note_on(c1,100)
sleep(.125)
midi_out.note_off(c1,100)
midi_out.note_off(cis4,127)

midi_out.note_on(e1,100)
midi_out.note_on(a3,127)
sleep(.125)
midi_out.note_off(e1,100)

midi_out.note_on(a1,100)
sleep(.125)
midi_out.note_off(a1,100)
midi_out.note_off(a3,127)

#=============================9
midi_out.note_on(g0,100)
midi_out.note_on(h3,127)
sleep(.25)
midi_out.note_off(g0,100)
midi_out.note_off(h3,127)

midi_out.note_on(g1,100)
midi_out.note_on(a3,127)
sleep(.125)
midi_out.note_off(g1,100)

midi_out.note_on(d1,100)
sleep(.125)
midi_out.note_off(d1,100)
midi_out.note_off(a3,127)

midi_out.note_on(g0,100)
midi_out.note_on(h3,127)
sleep(.125)
midi_out.note_off(g0,100)

midi_out.note_on(h1,100)
sleep(.125)
midi_out.note_off(h1,100)
midi_out.note_off(h3,127)

midi_out.note_on(d1,100)
midi_out.note_on(cis4,127)
sleep(.125)
midi_out.note_off(d1,100)

midi_out.note_on(g1,100)
sleep(.125)
midi_out.note_off(g1,100)
midi_out.note_off(cis4,127)

midi_out.note_on(g0,100)
midi_out.note_on(d4,127)
sleep(.25)
midi_out.note_off(g0,100)

midi_out.note_on(g1,100)
sleep(.125)
midi_out.note_off(g1,100)

midi_out.note_on(d1,100)
sleep(.125)
midi_out.note_off(d1,100)
midi_out.note_off(d4,127)

midi_out.note_on(g0,100)
midi_out.note_on(fis4,127)
sleep(.125)
midi_out.note_off(g0,100)

midi_out.note_on(h1,100)
sleep(.125)
midi_out.note_off(h1,100)
midi_out.note_off(fis4,127)

midi_out.note_on(d1,100)
midi_out.note_on(e4,127)
sleep(.125)
midi_out.note_off(d1,100)

midi_out.note_on(g1,100)
sleep(.125)
midi_out.note_off(g1,100)
midi_out.note_off(e4,127)

#=================================10
midi_out.note_on(d1,100)
midi_out.note_on(fis4,127)
sleep(.25)
midi_out.note_off(d1,100)
midi_out.note_off(fis4,127)

midi_out.note_on(d2,100)
midi_out.note_on(d4,127)
sleep(.125)
midi_out.note_off(d2,100)

midi_out.note_on(a1,100)
sleep(.125)
midi_out.note_off(a1,100)
midi_out.note_off(d4,127)

midi_out.note_on(d1,100)
midi_out.note_on(a3,127)
sleep(.25)
midi_out.note_off(d1,100)
midi_out.note_off(a3,127)

midi_out.note_on(d2,100)
midi_out.note_on(d4,127)
sleep(.125)
midi_out.note_off(d2,100)

midi_out.note_on(a1,100)
sleep(.125)
midi_out.note_off(a1,100)
midi_out.note_off(d4,127)

midi_out.note_on(d1,100)
midi_out.note_on(fis3,127)
sleep(.25)
midi_out.note_off(d1,100)

midi_out.note_on(d2,100)
sleep(.125)
midi_out.note_off(d2,100)

midi_out.note_on(a1,100)
sleep(.125)
midi_out.note_off(a1,100)
midi_out.note_off(fis3,127)

midi_out.note_on(d1,100)
midi_out.note_on(fis4,127)
sleep(.125)
midi_out.note_off(d1,100)

midi_out.note_on(fis1,100)
sleep(.125)
midi_out.note_off(fis1,100)
midi_out.note_off(fis4,127)

midi_out.note_on(a1,100)
midi_out.note_on(e4,127)
sleep(.125)
midi_out.note_off(a1,100)

midi_out.note_on(d2,100)
sleep(.125)
midi_out.note_off(d2,100)
midi_out.note_off(e4,127)

#=============================11

midi_out.note_on(d1,100)
midi_out.note_on(fis4,127)
sleep(.25)
midi_out.note_off(d1,100)
midi_out.note_off(fis4,127)

midi_out.note_on(d2,100)
midi_out.note_on(d4,127)
sleep(.125)
midi_out.note_off(d2,100)

midi_out.note_on(a1,100)
sleep(.125)
midi_out.note_off(a1,100)
midi_out.note_off(d4,127)

midi_out.note_on(d1,100)
midi_out.note_on(a3,127)
sleep(.25)
midi_out.note_off(d1,100)
midi_out.note_off(a3,127)

midi_out.note_on(d2,100)
midi_out.note_on(d4,127)
sleep(.125)
midi_out.note_off(d2,100)

midi_out.note_on(a1,100)
sleep(.125)
midi_out.note_off(a1,100)
midi_out.note_off(d4,127)

midi_out.note_on(d1,100)
midi_out.note_on(fis3,127)
sleep(.25)
midi_out.note_off(d1,100)

midi_out.note_on(d2,100)
sleep(.125)
midi_out.note_off(d2,100)

midi_out.note_on(a1,100)
sleep(.125)
midi_out.note_off(a1,100)
midi_out.note_off(fis3,127)

midi_out.note_on(d1,100)
midi_out.note_on(fis4,127)
sleep(.125)
midi_out.note_off(d1,100)

midi_out.note_on(fis1,100)
sleep(.125)
midi_out.note_off(fis1,100)
midi_out.note_off(fis4,127)

midi_out.note_on(a1,100)
midi_out.note_on(gis4,127)
sleep(.125)
midi_out.note_off(a1,100)

midi_out.note_on(d2,100)
sleep(.125)
midi_out.note_off(d2,100)
midi_out.note_off(gis4,127)

#=============================12

sleep(1)
