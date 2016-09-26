'''
Created on Jun 29, 2016

@author: Paulina
'''
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
s=5.0
n = 50
a= s/(2*n-1)
for i in range(n):
#    c.fill(path.rect(i,i,2*(n-i)-1,2*(n-i)-1), [color.rgb(random(),random(),random())])
    c.fill(path.rect(a*i,a*i,a*(2*(n-i)-1),a*(2*(n-i)-1)), [color.rgb(random(),random(),random())])
    


#c.stroke(path.line(1, 1, 2, 0))
    



       
#c.writeEPSfile()
c.writePDFfile()
#c.writeSVGfile()

