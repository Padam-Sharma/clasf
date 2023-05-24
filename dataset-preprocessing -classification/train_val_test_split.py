import pandas as pd
from glob import glob
import shutil
import random
from move_images_to_single_folder import make_dir
import numpy as np
from tqdm.notebook import tqdm
import os

pth = glob('/content/images/*/*')

random.shuffle(pth)

total_len = len(pth)
train_len = int(total_len * 0.7)
rem_len = total_len - train_len
val_len = int(rem_len * 2.0 / 3.0)
test_len = int(rem_len / 3)

print(100 * train_len / total_len, 100 * val_len / total_len, 100 * test_len / total_len)

make_dir('train')
make_dir('train/com')
make_dir('train/hoa')
make_dir('train/res')

make_dir('test')
make_dir('test/com')
make_dir('test/hoa')
make_dir('test/res')

make_dir('val')
make_dir('val/com')
make_dir('val/hoa')
make_dir('val/res')

train_pth = pth[0:train_len]
val_pth = pth[train_len:train_len + val_len]
test_pth = pth[train_len + val_len:]

len(train_pth) + len(val_pth) + len(test_pth)


def movettv(path, type):
    for i in tqdm(path):
        cls = i.split('/')[-2]
        img = i.split('/')[-1]
        src = i
        dst = '/content/' + type + '/' + cls + '/' + img
        shutil.copy(src, dst)


movettv(train_pth, 'train')
movettv(val_pth, 'val')
movettv(test_pth, 'test')
