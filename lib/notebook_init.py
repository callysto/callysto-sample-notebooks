import sys, os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(dir_path)

from ipywidgets import interact, interactive, widgets
from textblob import TextBlob
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

import pylab

# equivalent to %matplotlib inline within the notebook itself
get_ipython().magic('matplotlib inline')

pylab.rcParams['figure.figsize'] = (14, 6)