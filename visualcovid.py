tex =open(".\9036.txt", "r").read()
tex = tex.replace('\n','')
n=3
#freq =[int(tex[i:i+n]) for i in range(0, len(tex), n)]
#for f in freq:
#     if f > 37:
#             winsound.Beep(f, 60)

colr =[tex[i:i+n] for i in range(0, len(tex), n)]
rgbarr = [[int(j) for j in i] for i in colr]
rgbarr.pop()
import numpy as np
import matplotlib.pyplot as plt
c=int(144)
r = int(len(rgbarr)/c)
flag = np.empty((r,c,3), dtype=np.uint8)
for row in range(r):
 for col in range(c):
  	flag[row,col,:] = np.array(rgbarr[c*row + col]*27).astype(float) 

plt.imshow(flag.astype(np.uint8))
plt.show()