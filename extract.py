from __future__ import absolute_import, division, print_function
import sys
import os
sys.path.insert(1, os.path.join(sys.path[0], '..'))

import codecs
import fnmatch
import unicodedata
import urllib

def split(word):
    return [char for char in word]

def _convert_audio_and_split_sentences(source_dir):
  files = []
  f = codecs.open("out.txt",'w', "utf-8-sig")
  for root, dirnames, filenames in os.walk(source_dir):
    for filename in fnmatch.filter(filenames, '*.txt'):
      trans_filename = os.path.join(root, filename)
      with codecs.open(trans_filename, "r", "utf-8-sig") as fin:
        for line in fin:
          transcript = line
          transcript = transcript.lower().strip()
          for word in transcript:
              files.append(word)
  file = set(files)
  for item in file:
        f.write("%s\n" % item)
  f.close()
  return

if __name__ == "__main__":
    _convert_audio_and_split_sentences(sys.argv[1])
