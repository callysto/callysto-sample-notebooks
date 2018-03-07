import os

scriptdir = os.path.dirname(os.path.realpath(__file__))
os.environ['GUTENBERG_DATA'] = os.path.join(scriptdir, "..", "data", "cache", "gutenberg")

from gutenberg_lite import load_etext
from gutenberg_lite import strip_headers
from textblob import TextBlob
import pandas as pd
import matplotlib.pyplot as plt

def get_gutenberg_text(gutenberg_id):
  text = strip_headers(load_etext(gutenberg_id)).strip()
  text = text.replace("’","'").replace("“","\"").replace("”","\"")
  return text

def noun_phrases(text):
  words = TextBlob(text)
  return words.noun_phrases

def count_unique(text_list):
  unique_texts = list(set(text_list))
  text_counts =  { text: text_list.count(text) for text in unique_texts }
  sorted_texts = sorted(text_counts.items(), key=lambda x: x[1], reverse=True)

  count_df = pd.DataFrame(data=sorted_texts, columns=['text', 'count'])
  count_df = count_df.sort_values(by=['count'], ascending=False)
  return count_df

def plot_text_counts(text_count_df):
  text_count_df = text_count_df.sort_values(by=['count'], ascending=True)
  text_count_plt = text_count_df.plot(kind="barh", x='text')
  text_count_plt