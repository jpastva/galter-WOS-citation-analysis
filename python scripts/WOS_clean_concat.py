# -*- coding: utf-8 -*-
"""
Created on Thu May  4 09:47:27 2017

@author: mkaul
"""


import pandas as pd
import glob
import codecs
import csv

path = "/*.txt"    # input location of .txt files to convert/concatenate
for fname in glob.glob(path):
    with codecs.open(fname, 'r', 'UTF-16LE') as source_file:
        newfname = fname[0:len(fname)-4] + '.csv'
        with codecs.open(newfname, 'w','utf8') as dest_file:
            for line in source_file:
                values = line.split('\t')
                values = values[1:45]
                values = [x.encode('utf-8') for x in values]
                temp = [str(x,'utf8') for x in values]
                wr = csv.writer(dest_file, dialect='excel')
                wr.writerow(temp)

df_list = []
path = "/*.csv"    # input desired location of converted files                
for fname in glob.glob(path):
    df_list.append(pd.read_csv(fname))

complete_df = pd.concat(df_list)
complete_df.to_pickle('concatenated.pkl')
