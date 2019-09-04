from __future__ import absolute_import, division, print_function

# Make sure we can import stuff from util/
# This script needs to be run from the root of the DeepSpeech repository
import sys
import os
sys.path.insert(1, os.path.join(sys.path[0], '..'))

import codecs
import fnmatch
import pandas
import tqdm
import subprocess
import tarfile
import unicodedata

import urllib
from tensorflow.python.platform import gfile


def _convert_audio_and_split_sentences(source_dir):
  files = []
  for root, dirnames, filenames in os.walk(source_dir):
    for filename in fnmatch.filter(filenames, '*.txt'):
      trans_filename = os.path.join(root, filename)
      with codecs.open(trans_filename, "r", "utf-8") as fin:
        for line in fin:
          transcript = line
          transcript = transcript.lower().strip()
          wav_file = trans_filename.replace(".txt" , ".wav")
          if not os.path.exists(wav_file):
            print("Wav file path does not esists")
            print(wav_file)
            continue
          else:
            wav_filesize = os.path.getsize(wav_file)
            files.append((os.path.abspath(wav_file), wav_filesize, transcript))


  train = pandas.DataFrame(data=files, columns=["wav_filename", "wav_filesize", "transcript"])
  train.to_csv("train_data.csv", index=False)

if __name__ == "__main__":
  _convert_audio_and_split_sentences(sys.argv[1])
