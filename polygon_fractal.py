'''
Created on Jun 29, 2016

@author: elphel
'''
import math 
from pyx import *
from random import *
c = canvas.canvas()
"""
c.text(0, 0, "Hello, world!")
c.stroke(path.line(0, 0, 2, 0))
c.fill(path.rect(0, -3, 4, 1), [color.rgb.blue])
c.fill(path.circle(2.5, 1.5, 0.5), [color.rgb.red])
c.fill(path.circle(2.5, 1.5, 0.1), [color.rgb.green])
c.fill(path.circle(3.5, 2.5, 0.1), [color.rgb.green])
#c.fill(path.rect(1,2,3,1), [color.rgb.red])
for a in range(10):
    c.fill(path.circle(0.2*a, 0.2*a, 0.1), [color.rgb.green])
for _ in range(100):
    x = 3*random()
    y = 3*random()
    c.fill(path.circle(x, y, random()), [color.rgb(random(),random(),random())])
c.stroke(path.line(0, 0, 2, 0))
"""
m = 15
r = 5.0
n = 2000
k = 0.51


point_list = []


for i in range(m):
    a = (2*math.pi)/m*i
    x = r*math.cos(a)
    y = r*math.sin(a)
    point_list.append((x,y))
#point_list = [(0.0,0.0),(5.0,0.0),(6.0,4.0),(3.0,6.0),(0.0,4.0),(-1.0,2.0)]
#num = len(point_list)
for i in range(n):
    point_list.append((point_list[i][0]*(1-k)+point_list[i+1][0]*k,
                       point_list[i][1]*(1-k)+point_list[i+1][1]*k))
    
for i in range(len(point_list)-1):
    c.stroke(path.line(point_list[i][0],
                       point_list[i][1],
                       point_list[i+1][0],
                       point_list[i+1][1])
             , [color.rgb(random(),random(),random())])      
#c.writeEPSfile()
c.writePDFfile()
#c.writeSVGfile()

