from statistics import median
import matplotlib
matplotlib.use("Agg")
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import csv
x = open("./ee282/mytestfile.fastq")
line_data = []
in_progress = True
while in_progress:
    if x.readline().strip() == "":
        in_progress = False
    else:
        line = x.readline().strip()
        line = x.readline().strip()
        line = x.readline().strip()
        myquallist = list()
        for character in line:
            myquallist.append(1-(10.0**(-(ord(character)-33)/10.0)))
        data1=line_data.append([sum(myquallist)/len(myquallist), max(myquallist), min(myquallist), median(myquallist)])
df = pd.DataFrame(np.array(line_data), columns = ["avg", "max", "min", "med"])
print("ok")
scatterplot = sns.lmplot(x = "avg", y = "max", data = df, fit_reg = False)
scatterplot.savefig("scatter.png")
histoplot = sns.distplot(df["avg"])
hisfigure = histoplot.get_figure()
hisfigure.savefig("hist.png")
violinplot = sns.violinplot(x = "avg", data = df)
violinfig = violinplot.get_figure()
violinfig.savefig("violin.png")

