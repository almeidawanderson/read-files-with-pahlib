from glob import glob
import os
from os import path
import shutil

if path.exists('desafio2'):
  shutil.rmtree('desafio2')
  
os.mkdir('desafio2')

for file in glob('files/pasta_0/*.txt'):
  shutil.copy(file, 'desafio2')
  

