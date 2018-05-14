import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np
from itertools import groupby
import re

number_of_subjects = 11
videos_meta = [
     # Group 1
     [('sparse_11', 1),  ('sparse_32', 11), ('sparse_22_1', 5), ('sparse_00_1', 13), ('sparse_00_5', 33), ('sparse_00_9', 37),  
      ('dense_11', 17),  ('dense_32', 27), ('dense_22_1', 21), ('dense_00_1', 29), ('dense_00_5', 41), ('dense_00_9', 45)],
     # Group 2
     [('sparse_31', 10), ('sparse_12', 2),  ('sparse_22_2', 6), ('sparse_00_2', 14), ('sparse_00_6', 34), ('sparse_00_10', 38),
      ('dense_31', 26), ('dense_12', 18),  ('dense_22_2', 22), ('dense_00_2', 30), ('dense_00_6', 42), ('dense_00_10', 46)],
     # Group 3
     [('sparse_13', 3),  ('sparse_21', 4),  ('sparse_22_3', 7), ('sparse_00_3', 15), ('sparse_00_7', 35), ('sparse_00_11', 39),
      ('dense_13', 19),  ('dense_21', 20),  ('dense_22_3', 23), ('dense_00_3', 31), ('dense_00_7', 43), ('dense_00_11', 47)],
     # Group 4
     [('sparse_33', 12), ('sparse_23', 9),  ('sparse_22_4', 8), ('sparse_00_4', 16), ('sparse_00_8', 36), ('sparse_00_12', 40),
      ('dense_33', 28), ('dense_23', 25),  ('dense_22_4', 24), ('dense_00_4', 32), ('dense_00_8', 44), ('dense_00_12', 48)]
    ]


def getOrder(offset):
    latinsquare = [0, 11, 1, 10, 2, 9, 3, 8, 4, 7, 5, 6]
    return [(i + offset - 1) % 12 for i in latinsquare]
	
def getGroupOrder(subject_number):
    return [(i + subject_number - 1) % 4 for i in [0, 3, 1, 2]]


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


dense = sorted([v.get("yescount") for v in data if v.get("type") != "normal" and v.get("ok") and "dense" in v.get("vname")], key = lambda x: -x)
dense = {k: len(list(g)) for k, g in groupby(dense)}

glitched = sorted([v.get("yescount") for v in data if v.get("type") != "normal" and not v.get("ok") and "dense" in v.get("vname")], key = lambda x: -x)
glitched = {k: len(list(g)) for k, g in groupby(glitched)}

sparse = sorted([v.get("yescount") for v in data if v.get("type") != "normal" and v.get("ok") and "sparse" in v.get("vname")], key = lambda x: -x)
sparse = {k: len(list(g)) for k, g in groupby(sparse)}

x = np.arange(12)
x = np.array([i for i in x if dense.get(i, 0) + sparse.get(i, 0) + glitched.get(i, 0) > 0])
dense = [dense.get(i, 0) for i in x]
sparse = [sparse.get(i, 0) for i in x]
glitched = [glitched.get(i, 0) for i in x]
plt.bar(x + 0.45 / 2, dense, 0.45, color = "brown", edgecolor = "black")
plt.bar(x + 0.45 / 2, glitched, 0.45, bottom = dense, color = "red", edgecolor = "black", hatch = "///")
plt.bar(x - 0.45 / 2, sparse,  0.45, color = "gray", edgecolor = "black")


#  Extra labels
plt.ylabel("Number of videos")
plt.xlabel("Number of 'Yes' responses")
patches = [mpatches.Patch(color='brown', label='High density videos')]
patches.append(mpatches.Patch(color='gray', label='Low density videos'))
patches.append(mpatches.Patch(edgecolor="black", hatch="///", facecolor='red', label='Glitched videos (high density)'))
plt.legend(handles=patches)

#plt.title("Videos per amount of subjects that saw an anomaly, anomaly videos only")
plt.tight_layout()
plt.tight_layout()
plt.savefig("Figure_1.png")
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
#plt.title("Amount of yes/no responses per realism rating, all videos")
plt.tight_layout()
plt.tight_layout()
plt.savefig("Figure_2.png")
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
plt.tight_layout()
plt.savefig("Figure_3.png")
plt.show()

plt.figure(4)
anomtotal = sum([v for _, v in anomno.items()])
normaltotal = sum([v for _, v in normalno.items()])
anompercent = [100 * anomno[i] / anomtotal for i in range(1, 6)]
normalpercent = [100 * normalno[i] / normaltotal for i in range(1, 6)]

#plt.subplot(211)
#plt.title("Amount of no responses in percent per realism rating, anomaly videos only")
axes = plt.gca()
axes.set_ylim([0, 100])
plt.bar(x - 0.2, anompercent, 0.4, color = "gray", edgecolor = "black")

#plt.ylabel("Number of responses, %")
patches = [mpatches.Patch(color='gray', label='Anomaly videos'),
           mpatches.Patch(color='brown', label='Control videos')]
#plt.xticks(x, ('Strongly Disagree', 'Disagree', 'Neutral', 'Agree', 'Strongly Agree'))

#plt.legend(handles=patches)
#plt.tight_layout()

#plt.subplot(212)
#plt.title("Amount of no responses in percent per realism rating, non-anomaly videos only")
axes = plt.gca()
axes.set_ylim([0, 100])
plt.bar(x + 0.2, normalpercent, 0.4, color = "brown", edgecolor = "black")

plt.ylabel("Number of responses, %")
plt.xticks(x, ('Strongly Disagree', 'Disagree', 'Neutral', 'Agree', 'Strongly Agree'))
plt.legend(handles=patches)
plt.tight_layout()
plt.tight_layout()
plt.savefig("Figure_4.png")
plt.show()

def get_vtype_yeslist(vtype, density):
    returnlist = []
    with open("data2.txt", 'r') as f:
        for i, line in enumerate(f):
            if line == "\n" or data[i].get("type") != vtype or density not in data[i].get("vname"):
                continue
            returnlist.append([0, not data[i].get("ok")])
            line = line.split("\t")
            if (i == 16):
                print(line)
            items = [(line[j], line[j+1]) for j in range(0, len(line), 2)]
            if (i == 16):
                print(items)
            for _, yesno in items:
                
                if "Yes" in yesno:
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
#    plt.xlabel("Individual videos")
    plt.xticks([1 - 0.17 / 2, 2 - 0.17 / 2, 3 - 0.17 / 2], ["Corner", "Edge", "Center"])
    """    patches.append(mpatches.Patch(color=colors[1], label='Edge'))
    patches.append(mpatches.Patch(color=colors[2], label='Center'))
    patches.append(mpatches.Patch(color=colors[0], label='Corner'))"""
    plt.title(density)
   

#bar_cycle = (cycler('hatch', ['///', '--','\///', 'xxx', '\\\\']) * cycler('color', 'w')*cycler('zorder', [10]))
#styles = bar_cycle()
fig = plt.gcf()
#fig.suptitle("Amount of anomalies seen per video, anomaly videos only")
plt.subplot(211)
for j in range(0, 6):
    if j == 3:
        make_plot("Sparse")
        plt.subplot(212)
    l = get_vtype_yeslist(vtypes[j], density[j])
    #style = next(styles)
    for i, (val, glitched) in enumerate(l):
        if not glitched:
            plt.bar([j % 3 + 1 - 0.17 * (2 - i)], [val], 0.15, color = colors[j], edgecolor = "black")
        else:
            plt.bar([j % 3 + 1 - 0.17 * (2 - i)], [val], 0.15, color = "red", edgecolor = "black", hatch = "///")
patches = [mpatches.Patch(edgecolor="black", hatch="///", facecolor='red', label='Glitched videos')]
plt.legend(handles=patches)
make_plot("Dense")

plt.tight_layout()
plt.tight_layout()
plt.savefig("Figure_5.png")
plt.show()

plt.figure(6)

subject_data = []
def get_data2_values():
    returnlist = []
    with open("data2.txt", 'r') as f:
        for i, line in enumerate(f):
            if line == "\n":
                continue
            line = line.split("\t")
            items = [(line[j], line[j+1]) for j in range(0, len(line), 2)]
            returnlist.append({s + 1 : item for s, item in enumerate(items)})
    return returnlist

colors = ['xkcd:azure', 'xkcd:aqua', 'xkcd:brown', 'crimson', 
          'darkgreen', 'xkcd:goldenrod', 'grey', 'indigo',
          'magenta', 'xkcd:purple', 'xkcd:silver', 'xkcd:tomato']

data2_values = get_data2_values()
subject_values = []
subject_values_unchanged = []
for subject_number in range(1, number_of_subjects + 1):
    order = []
    for grpnum in getGroupOrder(subject_number):
        videos = videos_meta[grpnum]
        for i in getOrder(subject_number + grpnum * 3):
            _, v_id = videos[i]
            order.append(v_id)
    y = []
    y_so_far = []
    subject_values_unchanged.append([])
    for i in order:
        y_so_far.append(int(data2_values[i - 1].get(subject_number)[0]))
        subject_values_unchanged[-1].append(y_so_far[-1])
        y.append(np.mean(y_so_far))
    x = range(1, len(y) + 1)
    subject_values.append(y_so_far)
    axes = plt.gca()
    axes.set_ylim([0.5, 5.5])
    axes.grid(color='gray', linestyle='--', linewidth=1)
    plt.plot(x, y, 'bo-', color = colors[subject_number- 1])
plt.tight_layout()
plt.savefig("Figure_6.png")
plt.show()

plt.figure(7)
y = []
print([len(subject_values_unchanged[i]) for i in range(number_of_subjects)])
for i in range(48):
    y.append(0)
    for subject in range(number_of_subjects):
        y[-1] += subject_values_unchanged[subject][i]
x = range(1, 49)
axes = plt.gca()
axes.grid(color='gray', linestyle='--', linewidth=1)
plt.bar(x, y, color = 'brown', edgecolor = 'black')
plt.tight_layout()
plt.savefig("Figure_7.png")
plt.show()

plt.figure(8)
x = range(1, 49)
subject_avg_so_far = []
subject_avg = []
for i in range(48):
    for j in range(number_of_subjects):
        subject_avg_so_far.append(subject_values[j][i])
    subject_avg.append(np.mean(subject_avg_so_far))
plt.plot(x, subject_avg, 'bo-', color = 'brown')
axes = plt.gca()
axes.set_ylim([0.5, 5.5])
axes.grid(color='gray', linestyle='--', linewidth=1)
plt.tight_layout()
plt.savefig("Figure_8.png")
plt.show()
    
plt.figure(9)
x = range(1, 49)
subject_avg = []
mean_devi = []
for i in range(48):
    subject_avg_so_far = []
    for j in range(number_of_subjects):
        subject_avg_so_far.append(subject_values[j][i])
    avg = np.mean(subject_avg_so_far)
    subject_avg.append(avg)
    mean_devi.append(np.mean([abs(val - avg) for val in subject_avg_so_far]))
plt.plot(x, subject_avg, 'bo-', color = 'darkgreen')
plt.plot(x, mean_devi, 'bo-', color = 'brown')

patches = [mpatches.Patch(color='darkgreen', label='Average rating')]
patches.append(mpatches.Patch(color='brown', label='Mean deviation'))
#plt.title("Average rating and mean deviation for each video position")
plt.legend(handles=patches)

axes = plt.gca()
axes.set_ylim([0.5, 5.5])
axes.grid(axis = 'y', color='gray', linestyle='--', linewidth=1)
plt.tight_layout()
plt.savefig("Figure_9.png")
plt.show()


plt.figure(10)
axes = plt.gca()
axes.set_ylim([0, 7])
types = ['corner', 'edge', 'center', 'normal']
colours = ['gray', 'indigo', 'sienna', 'cyan']
divider = [8, 8, 8, 24]
for i in range(4):
    l = get_vtype_yeslist(types[i], "sparse")
    l += get_vtype_yeslist(types[i], "dense")
    val = 0
    glitchval = 0
    for amount, glitched in l:
        if glitched:
            glitchval += amount
        else:
            val += amount
    val /= divider[i]
    glitchval /= divider[i]
    print(l)
    print(val)
    plt.bar([i], [val], 0.35, color = colours[i], edgecolor = 'black')
    plt.bar([i], [glitchval], 0.35, bottom = [val], color = "red", edgecolor = 'black', hatch = "///")

plt.ylabel("Average amount that saw anomaly")
plt.xlabel("Video type")
patches = [mpatches.Patch(edgecolor="black", hatch="///", facecolor='red', label='Glitched videos')]
plt.legend(handles=patches)
plt.xticks(range(4), ('Corner', 'Edge', 'Center', 'No anomaly'))
#plt.title("Amount of yes/no responses per realism rating, all videos")
plt.tight_layout()
plt.savefig("Figure_10.png")
plt.show()

plt.figure(11)
plt.subplot(211)
axes = plt.gca()
axes.set_ylim([0, 7])
types = ['corner', 'edge', 'center', 'normal']
colours = ['gray', 'indigo', 'sienna', 'cyan']
divider = [4, 4, 4, 12]
for i in range(4):
    l = get_vtype_yeslist(types[i], "sparse")
    val = 0
    glitchval = 0
    for amount, glitched in l:
        if glitched:
            glitchval += amount
        else:
            val += amount
    val /= divider[i]
    glitchval /= divider[i]
    print(l)
    print(val)
    plt.bar([i], [val], 0.35, color = colours[i], edgecolor = 'black')
    plt.bar([i], [glitchval], 0.35, bottom = [val], color = "red", edgecolor = 'black')

plt.ylabel("Average amount that saw anomaly")
plt.xlabel("Video type")
#patches = [mpatches.Patch(edgecolor="black", hatch="///", facecolor='red', label='Glitched videos')]
#plt.legend(handles=patches)
plt.xticks(range(4), ('Corner', 'Edge', 'Center', 'No anomaly'))
plt.title("Sparse videos")
plt.subplot(212)
axes = plt.gca()
axes.set_ylim([0, 7])
types = ['corner', 'edge', 'center', 'normal']
colours = ['gray', 'indigo', 'sienna', 'cyan']
divider = [4, 4, 4, 12]
for i in range(4):
    l = get_vtype_yeslist(types[i], "dense")
    val = 0
    glitchval = 0
    for amount, glitched in l:
        if glitched:
            glitchval += amount
        else:
            val += amount
    val /= divider[i]
    glitchval /= divider[i]
    print(l)
    print(val)
    plt.bar([i], [val], 0.35, color = colours[i], edgecolor = 'black')
    plt.bar([i], [glitchval], 0.35, bottom = [val], color = "red", edgecolor = 'black', hatch="///")

plt.ylabel("Average amount that saw anomaly")
plt.xlabel("Video type")
patches = [mpatches.Patch(edgecolor="black", hatch="///", facecolor='red', label='Glitched videos')]
plt.legend(handles=patches)
plt.xticks(range(4), ('Corner', 'Edge', 'Center', 'No anomaly'))
plt.title("Dense videos")
plt.tight_layout()
plt.savefig("Figure_11.png")
plt.show()

plt.figure(12)

def make_plot(density):
    plt.ylabel("Number of responses")
#    plt.xlabel("Individual videos")
    """    patches.append(mpatches.Patch(color=colors[1], label='Edge'))
    patches.append(mpatches.Patch(color=colors[2], label='Center'))
    patches.append(mpatches.Patch(color=colors[0], label='Corner'))"""
    plt.xticks(range(12), ["Video 1"] + [""]*10 + ["Video 12"])
    plt.yticks(range(8))
    plt.title(density)   

#bar_cycle = (cycler('hatch', ['///', '--','\///', 'xxx', '\\\\']) * cycler('color', 'w')*cycler('zorder', [10]))
#styles = bar_cycle()
fig = plt.gcf()
#fig.suptitle("Amount of anomalies seen per video, anomaly videos only")
plt.subplot(211)
for density in ["sparse", "dense"]:
    if density == "dense":
        make_plot("Sparse")
        plt.subplot(212)
    l = get_vtype_yeslist("normal", density)
    #style = next(styles)
    for i, (val, glitched) in enumerate(l):
        if not glitched:
            plt.bar([i], [val], 0.95, color = "gray", edgecolor = "black")
        else:
            plt.bar([i], [val], 0.95, color = "red", edgecolor = "black", hatch = "///")
patches = [mpatches.Patch(edgecolor="black", hatch="///", facecolor='red', label='Glitched videos')]
plt.legend(handles=patches)
make_plot("Dense")

plt.tight_layout()
plt.savefig("Figure_12.png")
plt.show()


