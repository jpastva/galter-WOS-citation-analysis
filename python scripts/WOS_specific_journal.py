# -*- coding: utf-8 -*-
"""
Created on Wed May 17 14:52:55 2017

@author: Madhuri Kaul
"""

# Find the citation year of a particular journal after running main script

indices = [i for i, x in enumerate(journal) if x == " J AM ACAD DERMATOL"]
jyr = year[indices]
np.savetxt("SpecificJournalYears.csv", jyr, delimiter=",",fmt='%10.5f')  