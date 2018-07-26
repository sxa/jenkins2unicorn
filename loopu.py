platforms=["x86-64_linux", "ppc64le_linux", "s390x_linux", "x86-64_windows", "x86-32_windows", "x86-64_macos", "ppc64_aix", "arm32_linux", "arm32_linux"]

versions=["openjdk8", "openjdk8_openj9", "openjdk9", "openjdk9_openj9", "openjdk10", "openjdk10_openj9", "openjdk11", "openjdk11_openj9", ]

import unicornhat as uh
import time
uh.rotation(180)
uh.set_layout(uh.AUTO)
uh.brightness(0.5)
uh.show()

#uhcolor = { 'red':'(255,0,0)', 'blue':'(0,255,0)', 'green':'(0,255,255)', 'off':"(10,10,10)" }
#uhcolor = { 'red':(200,0,0), 'blue':(0,100,200), 'green':(0,255,0), 'off':(10,10,10) }
uhcolor = { 'red':(150,0,0), 'blue':(0,0,150), 'off':(0,0,0), "aborted_anime":(200,200,0), "blue_anime":(0,255,0), "red_anime":(210,0,210), "aborted":(50,50,50), "disabled": (8,8,4), "broken": (70,30,30)}
data = {}
with open("ao.txt") as f:
  d = dict(a.rstrip().split(None, 1) for a in f)
x = 0
y = 0
for platform in platforms:
  x = 0 
  for version in versions:
    searchstring=version + "_build_" + platform
    if searchstring in d:
      print (searchstring + "\t" + d.get(searchstring, "off"))
      if d.get(searchstring) in uhcolor:
        uh.set_pixel(x, y, uhcolor.get(d.get(searchstring)))
      else:
        uh.set_pixel(x, y, uhcolor.get('broken'))
    else:
      print (searchstring + "\t" + d.get(searchstring, "No Job"))
      uh.set_pixel(x, y, 0, 0, 0)
    x +=1
  y += 1
uh.show()
time.sleep(180)
