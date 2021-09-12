import glob
import zipfile
import os
from pathlib import Path

def setup_dirs(): 
  if not os.path.exists('test-results'):
    os.makedirs('test-results')

def find(): 
  rootDir = 'test-results'
  for dirName, subdirList, fileList in os.walk(rootDir, topdown=False):
    print('Found directory: %s' % dirName)
    # assert folder name here 
    for fname in fileList:
      print('\t%s' % fname)
  

def main(): 
    # check if file exists & get filename
    for zip_file in Path('.').glob("archive-*.zip"):
      if (zip_file):
        print(zip_file)

    with zipfile.ZipFile(zip_file) as zp:
      zp.extractall('./test-results')
      path = './test-results'
      assert os.path.exists(f'{path}')
      
if __name__ == "__main__":
  setup_dirs()
  main()
  find()