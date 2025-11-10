# -*- coding: utf-8 -*-
"""
Created on Thu May  4 09:47:27 2017

@author: mkaul
"""


import pandas as pd
import glob
import csv
import sys 

def concatenate_citations(input_dir, output_dir):
    in_path = input_dir + '/*.txt'    # input location of .txt files to process
    for fname in glob.glob(in_path):   # loop through all files in the directory
        print(fname)
        with open(fname, 'r') as source_file:   # this will open file with the system's default encoding (typically UTF-8), if needed change to other encoding, specify in the third argument
            newfname = output_dir + fname[len(input_dir):len(fname)-4] + '.csv' # output location of converted files
            with open(newfname, 'w', encoding='utf-8') as dest_file:   # write to new file
                for line in source_file:
                    values = line.split('\t')   # split text by tab characters
                    # values = values[1:45]
                    values = [x.encode('utf-8') for x in values]
                    temp = [str(x,'utf8') for x in values]
                    wr = csv.writer(dest_file, dialect='excel')
                    wr.writerow(temp)
    
    df_list = []
    out_path = output_dir + '/*.csv'
    for fname in glob.glob(out_path):
        df_list.append(pd.read_csv(fname))

    complete_df = pd.concat(df_list)
    complete_df.to_pickle(output_dir + '/concatenated.pkl')


def main():
    args = sys.argv
    match len(args):
        case 3:
            input_dir = args[1]
            output_dir = args[2]
        case 2:
            input_dir = args[1] # assume the argument is the input path
            output_dir = "."    # default output path is current working directory
        case 1:
            input_dir = "."     # current working directory
            output_dir = "."    # current working directory
        case _:
            print("Usage: python WOS_citation_analysis.py <input_path> <output_path>")
            sys.exit(1)

    concatenate_citations(input_dir, output_dir)

    print("Done, find outputs in " + output_dir) 


if __name__ == "__main__":
    main()