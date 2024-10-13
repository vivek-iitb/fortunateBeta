#!/home/vivek/bin/env/ai/bin/python

import sys 
import matplotlib.pyplot as plt
import numpy as np
import glob 
import os
import shutil

def split_para(file_name, output_dir):
  with open(file_name) as f:
    para = []
    tmp_para = []
    for line in f:
      print(line)
      if line == "\n":
        # A new paragraph has been found.
        if tmp_para:
          para.append("".join(tmp_para))
          tmp_para = [] # reset current_graph once new line is observed
      else:
        tmp_para.append(line) # accumulate lines until see \n

  # Write the last paragraph if it is not empty.
  if tmp_para:
    para.append("".join(tmp_para))
  
  for i, paragraph in enumerate(para):
    fname = "mvik_" + str(i) + ".txt"
    with open(output_dir + "/"+ fname, "w+") as f:
      f.write(paragraph)

if __name__ == "__main__":
  print("dfgg" , sys.argv[1])
  file_name = sys.argv[1]
  output_dir = "output"
  split_para(file_name, output_dir)
