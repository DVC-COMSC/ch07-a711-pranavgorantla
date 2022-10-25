import numpy as np
import matplotlib.pyplot as plt

width = 0.15
x = np.arange(2)
Math = [100,90]
English = [90,80]
Physics = [80,80]
Computer = [90,90]

fig,ax = plt.subplots()
math = ax.bar(x-width*1.5,Math,width)
eng = ax.bar(x-width*.5,English,width)
phy = ax.bar(x+width*1.5,Physics,width)
com = ax.bar(x+width*.5,Computer,width)

ax.legend(["Math","English","Physics","Computer"],loc = "lower center")

ax.set_title("Grouped graph for scores")

ax.bar_label(math,Math)
ax.bar_label(eng,English)
ax.bar_label(phy,Physics)
ax.bar_label(com,Computer)

#ax.set_xticks()
ax.set_xticks(ticks = [0,1])
ax.set_xticklabels(["Billy","Mary"])
fig.savefig('A11.png')
