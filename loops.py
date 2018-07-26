platforms=["x86-64_linux", "ppc64le_linux", "s390x_linux", "x86-64_windows", "x86-32_windows", "x86-64_macos", "ppc64_aix", "arm32_linux"]

versions=["openjdk8", "openjdk8_openj9", "openjdk9", "openjdk9_openj9", "openjdk10", "openjdk10_openj9", "openjdk11", "openjdk11_openj9", ]

#import unicornhat as uh
from sense_hat import SenseHat
sense = SenseHat()
import time
#uh.rotation(180)
#uh.set_layout(uh.AUTO)
#uh.brightness(0.5)
#uh.show()

#uhcolor = { 'red':'(255,0,0)', 'blue':'(0,255,0)', 'green':'(0,255,255)', 'off':"(10,10,10)" }
#uhcolor = { 'red':(200,0,0), 'blue':(0,100,200), 'green':(0,255,0), 'off':(10,10,10) }
uhcolor = { 'red':[150,0,0], 'blue':[0,0,150], 'off':[0,0,0], "aborted_anime":[200,200,0], "blue_anime":[0,255,0], "red_anime":[210,0,210], "aborted":[50,50,50], "disabled": [8,8,4], "broken": [70,30,30]}
data = {}
with open("ao.txt") as f:
  d = dict(a.rstrip().split(None, 1) for a in f)
x = 0
y = 0
pixels = [ [0,0,0], [0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],
           [0,0,0], [0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],
           [0,0,0], [0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],
           [0,0,0], [0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],
           [0,0,0], [0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],
           [0,0,0], [0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],
           [0,0,0], [0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],
           [0,0,0], [0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]
        ]

def set_pixel(x, y, rgb):
  print (x)
  print (y)
  #print "Setting pixel ("+ x + "," + y + ") = " + (x*8+y)5C + " to " + rgb
  pixels[x*8+y] = rgb

for platform in platforms:
  x = 7 
  for version in versions:
    searchstring=version + "_build_" + platform
    if searchstring in d:
      print (searchstring + "\t" + d.get(searchstring, "off"))
      if d.get(searchstring) in uhcolor:
        set_pixel(x, y, uhcolor.get(d.get(searchstring)))
      else:
        set_pixel(x, y, uhcolor.get('broken'))
    else:
      print (searchstring + "\t" + d.get(searchstring, "No Job"))
      set_pixel(x, y, [0, 0, 0])
    x -=1
  y += 1
sense.set_pixels(pixels)
time.sleep(180)
