import pandas as pd
from glob import glob
import shutil
import random
import numpy as np
from tqdm.notebook import tqdm
import os

feb_df = pd.read_csv('/content/Classification activity_2 - Sheet1.csv')

duplicates = []
cls_map = {'COMM': 'com', 'HOA': 'hoa', 'RES': 'res'}
for i in feb_df.iterrows():
    oid = i[1]['oid']
    cls = i[1]['correct class']
    if oid not in duplicates:
        duplicates.append(oid)
        src = '/content/png_clipped/' + oid + '.png'
        dst = '/content/images/' + cls_map[cls] + '/' + oid + '.png'
        shutil.copy(src, dst)
    else:
        pass

print(len(glob('/content/images/*/*')))

for i in glob('/content/images/*'):
    print(i.split('/')[-1], len(glob(i + '/*')))


