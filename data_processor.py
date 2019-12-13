import csv
import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
import statistics as stat
import math


"""
1. Data is imported as a CSV
2. CSV data is organized into arrays based around the four groups:

    Double Provocative
    Double Neutral
    Single Provocative (Polio)
    Single Provocative (MMR)
3. Manually renamed dimensions
    Of the colours given, which do you prefer? CHANGED TO colour
    In light of the Disneyland Measles Outbreak of 2015, there is a correlation between cases administered with the MMR vaccine and the potential of a measles outbreak.
    CHANGED TO
    DP_1
    DN_1
    Polio_1
    MMR_1
    There is not enough evidence that the percentages given would result in any major dangers.
    CHANGED TO
    DP_2
    ""
    The graph shows a potential return to the safe threshold. Therefore this momentary dip above the threshold for herd immunity is of little concern.
    CHANGED TO
    DP_3
    ""
    Regarding personal freedoms and rights to bodily autonomy, it is inappropriate to ask schools to report on this information even when the information is completely anonymous.
    DP_4
    ""
    With your knowledge and understanding of the effects, measles has on the cases affected, the disease is serious enough to warrant mandatory vaccination.
    DP_5
    ""
    With regards to more than just the measles virus, parents should prefer to use traditional methods such as peer-to-peer exposure in order to inoculate rather than western medical methods.
    CHANGED TO
    DP_6
    ""
    Polio has become uncommon in most resource-rich countries, but cases still appear around the world. Even though the threshold for polio is lower (80%-85%) than that of measles it is still necessary to take medical measures to prevent its spread.
    CHANGED TO
    DP_7
    ""
    What are your comments and/or concerns about the subject matter and how it is being handled?
    CHANGED TO
    COMMENTS

"""

data = pd.read_csv('survey_data.csv')

colours = [0,0,0,0] #[Purple,Orange,Red,Yellow]
for colour in data["colour"]:
    if colour == "Purple":
        colours[0] = colours[0]+1
    if colour == "Orange":
        colours[1] = colours[1]+1
    if colour == "Red":
        colours[2] = colours[2]+1
    if colour == "Yellow":
        colours[3] = colours[3]+1
"""
Count the values given
COUNT = [numAgreee,numSomewhat,numNeut,numS,numDisagree]
"""

#takes an np array and sums the values
def count(a,d):
    arr = [0,0,0,0,0]
    for y in d:
        da = d[y]
        for x in da:
            if x == "Agree":
                arr[0] = arr[0]+1
            if x == "Somewhat Agree":
                arr[1] = arr[1]+1
            if x == "Neutral":
                arr[2] = arr[2]+1
            if x == "Somewhat Disagree":
                arr[3] = arr[3]+1
            if x == "Disagree":
                arr[4] = arr[4]+1
        a.append(arr)
        arr = [0,0,0,0,0]
    return a

full_data = count([],data)[2:-1]
#print(full_data)

"""
Separate into sets
"""

DP = np.array(full_data[0:7])
DN = np.array(full_data[7:14])
Polio = np.array(full_data[14:21])
MMR = np.array(full_data[21:28])


sum_DP = sum(DP)
sum_DN = sum(DN)
sum_Polio = sum(Polio)
sum_MMR = sum(MMR)

p_DP = sum_DP/sum(sum_DP)
p_DN = sum_DN/sum(sum_DN)
p_Polio = sum_Polio/sum(sum_Polio)
p_MMR = sum_MMR/sum(sum_MMR)

population_sum = sum_DN + sum_DP + sum_MMR + sum_Polio

p_pop = population_sum/sum(population_sum)

"""
From sums we see that people were most devicive during the Polio Vulnerable section
Least for the MMR vulnerable phase
While the double charged and double neutral varried only barely

STATS:
Pg 9-10: " Thus, there appears to be no standard for the number of points on rating
scales, and common practice varies widely. "
from Jon A. Krosnick and Stanley Presser

Assign numbers to values
Agree: 5
Somewhat Agree: 4
Neutral: 3
Somewhat Disagree: 2
Disagree: 1

Standard Div and stats calculator: https://www.socscistatistics.com/tests/ztest_sample_mean/default2.aspx

"""

adj = np.array([5,4,3,2,1])
DP_adj = sum_DP*adj
DN_adj = sum_DN*adj
Polio_adj = sum_Polio*adj
MMR_adj = sum_MMR*adj
pop_adj = population_sum*adj


pop_mean = sum(pop_adj)/sum(population_sum)

pop_variance = []
count = 1.0
for x in population_sum:
    pop_variance.append(x*((count - pop_mean)*(count - pop_mean)))
    count = count-0.25



dp_mean = sum(DP_adj)/sum(sum_DP)
dn_mean = sum(DN_adj)/sum(sum_DN)
Polio_mean = sum(Polio_adj)/sum(sum_Polio)
MMR_mean = sum(MMR_adj)/sum(sum_MMR)


"""
Stats Calculations
Get Means on each question for each case
DP = np.array(full_data[0:7])
DN = np.array(full_data[7:14])
Polio = np.array(full_data[14:21])
MMR = np.array(full_data[21:28])
"""

def true_vals(vals):
    tv = []
    count = 0
    for x in vals:
        for y in range(x):
            tv.append(adj[count])
        count = count + 1
    return tv

DP_mean = []
DP_std = []
for q in DP:
    pop = sum(q)
    mean = sum(q*adj)/pop
    DP_mean.append(mean)
    DP_std.append(stat.stdev(true_vals(q),mean))
print(DP_std)
print(DP_mean)
nDP= sum(DP[0])

DN_mean = []
DN_std = []
for q in DN:
    pop = sum(q)
    mean = sum(q*adj)/pop
    DN_mean.append(mean)
    DN_std.append(stat.stdev(true_vals(q),mean))
print(DN_std)
print(DN_mean)
nDN= sum(DN[0])

Polio_mean = []
Polio_std = []
for q in Polio:
    pop = sum(q)
    mean = sum(q*adj)/pop
    Polio_mean.append(mean)
    Polio_std.append(stat.stdev(true_vals(q),mean))
print(Polio_std)
print(Polio_mean)
nPolio= sum(Polio[0])


MMR_mean = []
MMR_std = []
for q in MMR:
    pop = sum(q)
    mean = sum(q*adj)/pop
    MMR_mean.append(mean)
    MMR_std.append(stat.stdev(true_vals(q),mean))
print(MMR_std)
print(MMR_mean)
nMMR= sum(MMR[0])

"""
Stats Continued, statistical significance
using ALPHA = 0.05
Using a two tailed test, want to be above or bellow
critial Z = 1.960
so we reject H0 is Z not in (-1.96,1.96)
"""

#DP vs. DN
Z = 1.960
def sigstat(n1,mean1,std1,n2,mean2,std2):
    mean_dif = np.array(mean1) - np.array(mean2)
    dist_std = []
    for index in range(len(mean1)):

        dist_std.append(math.sqrt((std1[index]**2/n1)+(std2[index]**2/n2)))

    dist_std = np.array(dist_std)
    mean_dif = np.array(mean_dif)
    z_std = np.array(dist_std * Z)
    return np.array(abs(mean_dif) > z_std)
    #dist_std = math.sqrt((std1[0]**2/n1)+(std2[0]**2/n2))
    #return dist_std


print("DP vs DN\n",sigstat(nDP,DP_mean,DP_std,nDN,DN_mean,DN_std))
print("DP vs Polio\n",sigstat(nDP,DP_mean,DP_std,nPolio,Polio_mean,Polio_std))
print("DP vs Measles\n",sigstat(nDP,DP_mean,DP_std,nMMR,MMR_mean,MMR_std))

print("DN vs Polio\n",sigstat(nDN,DN_mean,DN_std,nPolio,Polio_mean,Polio_std))
print("DN vs Measles\n", sigstat(nDN,DN_mean,DN_std,nMMR,MMR_mean,MMR_std))

print("Polio vs Measles\n",sigstat(nPolio,Polio_mean,Polio_std,nMMR,MMR_mean,MMR_std))




"""
VIsuals
"""
labels = 'Agree','Somewhat Agree','Neutral','Somewhat Disagree','Disagree'
explode = (0.1,0,0,0,0)

fig1, ax1 = plt.subplots()
ax1.pie(p_pop, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
#plt.show()
