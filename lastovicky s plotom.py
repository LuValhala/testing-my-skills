#malo by to byt cyklus v cykle - ten najnizsi bude if o tom ze ci je jednotka tak nahodne zvysi nahodnym smerom maticu o +1

import random
import matplotlib.pyplot as plt
x=0
y=0

for i in range(1,11):
  o = random.randrange(1,100)
  if o > 20:
    x=x
    y=y+32
    plt.scatter(x, y, c="blue")
  if (20<=o<=50): 
    z = random.randrange(1,32)
    x = x +(32 - z)
    y = y + z
    plt.scatter(x, y, c="blue")
  if (50<o<70):
    x=x+32
    y=y
    plt.scatter(x, y, c="blue")
  if (70<=o<=100):
    x=x
    y=y-32
    plt.scatter(x, y, c="blue")  
  plt.savefig("tura%i.png" %i)
  
if x >= 98 and y >= 98:
  print "jo"
else:
  print "nie"
print plt
