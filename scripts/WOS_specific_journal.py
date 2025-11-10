# -*- coding: utf-8 -*-
"""
Created on Wed May 17 14:52:55 2017

@author: Madhuri Kaul
"""

# Find the citation year of a particular journal after running main script
jn1 = ' NEW ENGL J MED' #insert name of journal from MaxCitedJournals list, follow code pattern to expand as needed
jn2 = ' CIRCULATION'
indices = [i for i, x in enumerate(journal) if x == jn1]
jyr1 = year[indices]
indices = [i for i, x in enumerate(journal) if x == jn2]
jyr2 = year[indices]
d = {jn1: jyr1, jn2: jyr2}
pdf = pd.DataFrame.from_dict(d,orient = 'index')
pdf = pdf.transpose()
pdf.to_csv('Specific_Journal_Cited_Pub_Years.csv')