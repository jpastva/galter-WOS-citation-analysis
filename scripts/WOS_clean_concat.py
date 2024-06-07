# -*- coding: utf-8 -*-
"""
Created on Thu May  4 09:47:27 2017

@author: mkaul
"""


import pandas as pd
import glob
import csv
import sys 

def concatenate_citations(input_path, output_path):
    in_path = input_path + '/*.txt'    # input location of .txt files to process
    for fname in glob.glob(in_path):   # loop through all files in the directory
        print(fname)
        with open(fname, 'r') as source_file:   # this will open file with the system's default encoding (typically UTF-8), if needed change to other encoding, specify in the third argument
            newfname = output_path + fname[len(input_path):len(fname)-4] + '.csv' # output location of converted files
            with open(newfname, 'w', encoding='utf-8') as dest_file:   # write to new file
                for line in source_file:
                    values = line.split('\t')   # split text by tab characters
                    values = values[1:45]
                    values = [x.encode('utf-8') for x in values]
                    temp = [str(x,'utf8') for x in values]
                    wr = csv.writer(dest_file, dialect='excel')
                    wr.writerow(temp)
    
    df_list = []
    out_path = output_path + '/*.csv'
    for fname in glob.glob(out_path):
        df_list.append(pd.read_csv(fname))

    complete_df = pd.concat(df_list)
    complete_df.to_pickle(output_path + '/concatenated.pkl')


def main():
    input_path = sys.argv[1]
    output_path = sys.argv[2]

    concatenate_citations(input_path, output_path)

    print("Done, find outputs in " + output_path) 


if __name__ == "__main__":
    main()