# -*- coding: utf-8 -*-
"""
Created on Fri May 5 16:20:14 2017

@author: Madhuri Kaul

Program for WOS Cited References Analysis 
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter

df = pd.read_pickle('concatenated.pkl')
df = df.dropna(subset = ['PY','CR'])  # Get rid of badly imported data
cited_ref = df.CR
orig_art_yr = df.PY

a = cited_ref.size
refs_per = np.zeros(a)  # Citations per article
name = []               # Citation author
year = []               # Cited article year of pub
age = []                # Cited article age wrt published art.
journal = []            # Journal name of cited article

for i, row in enumerate(cited_ref.values):
    auths = cited_ref.values[i]   # Read the cell with all the citations for one article
    parts = auths.split(';')      # Split the citations based on semi-colon
    refs_per[i] = 0;              # Count the number of citations
    
# Split the citation into parts based on comma to get the year and journal name
    for j in parts:
        if len(j.split(',')) == 3:
             n,y,jou =  j.split(',')
        elif len(j.split(',')) == 4:
             n,y,jou,ver =  j.split(',')
        elif len(j.split(',')) == 5:
             n,y,jou,ver,page =  j.split(',')
        elif len(j.split(',')) == 6:
             n,y,jou,ver,page,doi =  j.split(',')
        y = y.strip()
        if y.isdigit():      # Some citations don't have a year, throw  them away
            name.append(n)
            year.append(y)            
            year = [int(i) for i in year]
            temp = orig_art_yr.values[i] - float(y)
            age.append(temp)         
            journal.append(jou)
            refs_per[i] += 1
        else:
            pass

## Write the Top Most Cited Journals to csv file                
journal = [x.upper() for x in journal]  # Convert all names to uppercase
cc = Counter(journal)
p = cc.most_common()
cols = ['name','count']
pp = pd.DataFrame(p,columns = cols)
pp['name'] = pp['name'].str.upper()  # Convert all names to uppercase
pp = pp.set_index('name')
pp = pp.groupby(pp.index).sum()      # Find duplicate names and add the counts
pp = pp.sort_values(['count'], ascending = [False])   # Sort list by counts
pp.to_csv('MaxCitedJournals.csv')                    # Write to csv file

############################################################################# 
# Let's make some figures

# Number of articles published per year
orig_art_yr = np.array(orig_art_yr,int)
plt.figure()
bins=np.arange(min(orig_art_yr), max(orig_art_yr)+2)
plt.hist(orig_art_yr, bins)
plt.xticks(orig_art_yr+0.5, orig_art_yr, rotation = 90)              
plt.ylabel('Number of articles published per year')   

# Year of publication of cited articles
year = np.array(year)
plt.figure()
plt.hist(year, bins = np.arange(min(year), max(year) + 2, 1))
plt.xlabel('Year of publication of cited articles')   

# Age of cited references wrt. published article
age = np.array(age)
plt.figure()
#plt.hist(age, bins=np.arange(min(age), max(age) + 2, 1))
plt.hist(age, bins = np.arange(0, 100, 1))
plt.xlabel('Age of cited articles (years)')  
plt.ylabel('Count')  

# Total number of cited references per year, and 
# Average number of cited references per article per year
ref_peryear = []
avgref_peryear = []
xx = np.unique(orig_art_yr)
i = min(orig_art_yr)
for i in xx:
    ii = orig_art_yr == i
    p = refs_per[ii].sum()
    pp = refs_per[ii].mean()
    ref_peryear.append(p)
    avgref_peryear.append(pp)
    
ref_peryear = np.array(ref_peryear)
avgref_peryear = np.array(avgref_peryear)
plt.figure()
plt.plot(xx,ref_peryear,'o-')
plt.xticks(xx, xx, rotation=90)              
plt.ylabel('Number of citations per year')           

plt.figure()
plt.plot(xx,avgref_peryear,'o-')
plt.xticks(xx, xx, rotation=90)              
plt.ylabel('Avg. number of citations per article, per year')  


## Write to file
temp1 = pd.DataFrame({'Original article year': orig_art_yr,'references per article': refs_per})
temp1.to_csv('OriginalArticle_Year_RefCount.csv')
del temp1

temp1 = pd.DataFrame({'Cited journal year': year,'Cited journal age': age})
temp1.to_csv('CitedJournalAge.csv')
del temp1

temp1 = pd.DataFrame({'Year': xx, 'Total refs per year': ref_peryear,'Ave refs per article per year': avgref_peryear}) 	  
temp1.to_csv('ReferenceStats.csv')
del temp1