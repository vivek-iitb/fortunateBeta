#!/home/vivek/bin/env/ai/bin/python
import matplotlib.pyplot as plt
import numpy as np
import glob 
import os
import shutil

def plot_lines(file_names,ax):
  """
  Plots lines from a bunch of files.
  """
  for file_name in file_names:
    print(file_name)
    with open(file_name) as f:
      data = np.loadtxt(f, delimiter=" ")

    x = data[:, 0]
    y = data[:, 1]

    ax.plot(x, y, label=file_name)


def my_plot(stringname):
  fig, ax = plt.subplots()

  ax.set_xlabel("x")
  ax.set_ylabel("y")
  ax.set_title("Skeleton debug")
  for file in glob.glob(stringname):
      #ax.legend()
      #os.rmdir("output");
      #os.mkdir("output");
      split_paragraphs(file,"output")
      plot_lines(glob.glob("output/*"),ax)
  plt.draw()


if __name__ == "__main__":
  for token in ["output/mvik_*"]
    my_plot(token)
  plt.show()

