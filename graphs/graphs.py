import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np
from itertools import groupby
import re

plt.figure(1)

data = []
with open('data.txt', 'r') as f:
    for line in f:
        mgrp = re.match(r'(.*?)\t(.*?)\t(.*?)\t(.*?)\t(.*?)\t(.*?)$', line)
        if mgrp:
            data.append({"vid"      : int(mgrp.group(1)),
                         "vname"    : mgrp.group(2),
                         "type"     : mgrp.group(3).lower(),
                         "vgroup"   : int(mgrp.group(4)),
                         "ok"       : bool(mgrp.group(5) == "Ok"),
                         "yescount" : int(mgrp.group(6))})

x = np.arange(8)

dense = sorted([v.get("yescount") for v in data if v.get("type") != "normal" and v.get("ok") and "dense" in v.get("vname")], key = lambda x: -x)
dense = {k: len(list(g)) for k, g in groupby(dense)}
dense = [dense.get(i, 0) for i in x]
plt.bar(x - 0.35 / 2, dense, 0.35, color = "gray", edgecolor = "black")



sparse = sorted([v.get("yescount") for v in data if v.get("type") != "normal" and v.get("ok") and "sparse" in v.get("vname")], key = lambda x: -x)
sparse = {k: len(list(g)) for k, g in groupby(sparse)}
sparse = [sparse.get(i, 0) for i in x]
plt.bar(x + 0.35 / 2, sparse,  0.35, color = "brown", edgecolor = "black")


#  Extra labels
plt.ylabel("Number of videos")
plt.xlabel("Number of 'Yes' responses")
patches = [mpatches.Patch(color='gray', label='Low density videos')]
patches.append(mpatches.Patch(color='brown', label='High density videos'))
plt.legend(handles=patches)

plt.title("Videos per amount of subjects that saw an anomaly, anomaly videos only")
plt.tight_layout()
plt.show()

plt.figure(2)

data2yes = {1 : 0, 2 : 0, 3 : 0, 4 : 0, 5 : 0}
data2no = {1 : 0, 2 : 0, 3 : 0, 4 : 0, 5 : 0}
with open("data2.txt", 'r') as f:
    for line in f:
        if line == "\n":
            continue
        line = line.split("\t")
        items = [(line[i], line[i+1]) for i in range(0, len(line), 2)]
        for rating, yesno in items:
            if yesno == "Yes":
                data2yes[int(rating)] += 1
            else:
                data2no[int(rating)] += 1

x = np.arange(5)
plt.bar(x - 0.2 / 2, [data2no.get(i, 0) for i in range(1, 6)], 0.2, color = "gray", edgecolor = "black")
plt.bar(x + 0.2 / 2, [data2yes.get(i, 0) for i in range(1, 6)], 0.2, color = "brown", edgecolor = "black")

plt.ylabel("Number of responses")
patches = [mpatches.Patch(color='gray', label='Saw no anomaly')]
patches.append(mpatches.Patch(color='brown', label='Saw anomaly'))
plt.xticks(x + 0.2 / 2, ('Strongly Disagree', 'Disagree', 'Neutral', 'Agree', 'Strongly Agree'))

plt.legend(handles=patches)
plt.title("Amount of yes/no responses per realism rating, all videos")
plt.tight_layout()
plt.show()


plt.figure(3)

anomyes = {1 : 0, 2 : 0, 3 : 0, 4 : 0, 5 : 0}
anomno = {1 : 0, 2 : 0, 3 : 0, 4 : 0, 5 : 0}
normalyes = {1 : 0, 2 : 0, 3 : 0, 4 : 0, 5 : 0}
normalno = {1 : 0, 2 : 0, 3 : 0, 4 : 0, 5 : 0}
with open("data2.txt", 'r') as f:
    for i, line in enumerate(f):
        if line == "\n":
            continue
        line = line.split("\t")
        items = [(line[j], line[j+1]) for j in range(0, len(line), 2)]
        for rating, yesno in items:
            dictyes = normalyes if data[i].get("type") == "normal" else anomyes
            dictno = normalno if data[i].get("type") == "normal" else anomno
            if yesno == "Yes":
                dictyes[int(rating)] += 1
            else:
                dictno[int(rating)] += 1

x = np.arange(5)
plt.subplot(211)
plt.title("Amount of yes/no responses per realism rating, anomaly videos only")
plt.tight_layout()
axes = plt.gca()
ymax = max([v for _, v in anomyes.items()]   + 
           [v for _, v in anomno.items()] + 
           [v for _, v in normalyes.items()] + 
           [v for _, v in normalno.items()])
axes.set_ylim([0, ymax])
plt.bar(x - 0.2 / 2, [anomno.get(i, 0) for i in range(1, 6)], 0.2, color = "gray", edgecolor = "black")
plt.bar(x + 0.2 / 2, [anomyes.get(i, 0) for i in range(1, 6)], 0.2, color = "brown", edgecolor = "black")

plt.ylabel("Number of responses")
patches = [mpatches.Patch(color='gray', label='Saw no anomaly')]
patches.append(mpatches.Patch(color='brown', label='Saw anomaly'))
plt.xticks(x + 0.2 / 2, ('Strongly Disagree', 'Disagree', 'Neutral', 'Agree', 'Strongly Agree'))

plt.legend(handles=patches)
plt.tight_layout()

plt.subplot(212)
plt.title("Amount of yes/no responses per realism rating, non-anomaly videos only")
axes = plt.gca()
axes.set_ylim([0, ymax])
plt.bar(x - 0.2 / 2, [normalno.get(i, 0) for i in range(1, 6)], 0.2, color = "gray", edgecolor = "black")
plt.bar(x + 0.2 / 2, [normalyes.get(i, 0) for i in range(1, 6)], 0.2, color = "brown", edgecolor = "black")

plt.ylabel("Number of responses")
plt.xticks(x + 0.2 / 2, ('Strongly Disagree', 'Disagree', 'Neutral', 'Agree', 'Strongly Agree'))
plt.legend(handles=patches)
plt.tight_layout()
plt.show()

plt.figure(4)
anomtotal = sum([v for _, v in anomno.items()])
normaltotal = sum([v for _, v in normalno.items()])
anompercent = [100 * anomno[i] / anomtotal for i in range(1, 6)]
normalpercent = [100 * normalno[i] / normaltotal for i in range(1, 6)]

plt.subplot(211)
plt.title("Amount of no responses in percent per realism rating, anomaly videos only")
axes = plt.gca()
axes.set_ylim([0, 100])
plt.bar(x, anompercent, 0.2, color = "gray", edgecolor = "black")

plt.ylabel("Number of responses, %")
patches = [mpatches.Patch(color='gray', label='Saw no anomaly')]
plt.xticks(x, ('Strongly Disagree', 'Disagree', 'Neutral', 'Agree', 'Strongly Agree'))

plt.legend(handles=patches)
plt.tight_layout()

plt.subplot(212)
plt.title("Amount of no responses in percent per realism rating, non-anomaly videos only")
axes = plt.gca()
axes.set_ylim([0, 100])
plt.bar(x, normalpercent, 0.2, color = "gray", edgecolor = "black")

plt.ylabel("Number of responses, %")
plt.xticks(x, ('Strongly Disagree', 'Disagree', 'Neutral', 'Agree', 'Strongly Agree'))
plt.legend(handles=patches)
plt.tight_layout()
plt.show()

def get_vtype_yeslist(vtype, density):
    returnlist = []
    with open("data2.txt", 'r') as f:
        for i, line in enumerate(f):
            if line == "\n" or data[i].get("type") != vtype or density not in data[i].get("vname"):
                continue
            returnlist.append([0, not data[i].get("ok")])
            line = line.split("\t")
            items = [(line[j], line[j+1]) for j in range(0, len(line), 2)]
            for _, yesno in items:
                if yesno == "Yes":
                    returnlist[-1][0] += 1
    return returnlist

plt.figure(5)
vtypes = ["corner", "edge", "center"]*2
density = ["sparse"]*3 + ["dense"]*3
colors = ["gray", "indigo", "sienna"]*2
glitchcolor = "red"
#hatch = ['///', '--', 'xxx']*2

def make_plot(density):
    plt.ylabel("Number of responses")
    plt.xlabel("Individual videos")
    plt.xticks([])
    patches = [mpatches.Patch(color=colors[0], label='Corner')]
    patches.append(mpatches.Patch(color=colors[1], label='Edge'))
    patches.append(mpatches.Patch(color=colors[2], label='Center'))
    patches.append(mpatches.Patch(facecolor = glitchcolor, label='Glitched'))
    plt.title(density)
    plt.legend(handles=patches)
   

#bar_cycle = (cycler('hatch', ['///', '--','\///', 'xxx', '\\\\']) * cycler('color', 'w')*cycler('zorder', [10]))
#styles = bar_cycle()
fig = plt.gcf()
fig.suptitle("Amount of anomalies seen per video, anomaly videos only")
plt.subplot(121)
for j in range(0, 6):
    if j == 3:
        make_plot("Sparse")
        plt.subplot(122)
    l = get_vtype_yeslist(vtypes[j], density[j])
    #style = next(styles)
    for i, (val, glitched) in enumerate(l):
        plt.bar([j % 3 + 1 - 0.17 * (2 - i)], [val], 0.15, color = colors[j] if not glitched else glitchcolor,
                edgecolor = "black")
make_plot("Dense")

plt.tight_layout()
plt.show()

