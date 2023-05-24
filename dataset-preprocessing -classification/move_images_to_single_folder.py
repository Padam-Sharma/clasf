import pandas as pd
from glob import glob
import shutil
import random
import numpy as np
from tqdm.notebook import tqdm
from utils import make_dir
import os


def move_to_single_folder_main(config, logger):
    img_pth = config["PATH"]["drive"]["image_path"]
    csv_pth = config["PATH"]["drive"]["image_path"]
    pwd_root_pth = config["PATH"]["pwd"]["root_path"]
    os.system(f"cp {csv_pth} {pwd_root_pth}")
    os.system(f"cp -r {img_pth} {pwd_root_pth}")
    df = pd.read_csv('/content/corrected data.csv')

    print(len(set(list(df['oid']))), len(list(df['oid'])))

    (list(df['Duplicate'])).count(2)

    make_dir('all_images')
    make_dir('images')
    make_dir('images/com')
    make_dir('images/hoa')
    make_dir('images/res')

    test_pth = glob('/content/property classf data/test/*/*')
    train_pth = glob('/content/property classf data/train/*/*')
    val_pth = glob('/content/property classf data/val/*/*')

    print(len(test_pth) + len(train_pth) + len(val_pth))

    all_pth = test_pth + train_pth + val_pth
    for i in tqdm(all_pth):
        src = i
        dst = '/content/all_images/' + i.split('/')[-1]
        shutil.copy(src, dst)

    print(len(glob('/content/all_images/*')))

    duplicates = []
    cls_map = {'Comm': 'com', 'HOA': 'hoa', 'Resi': 'res'}
    for i in df.iterrows():
        oid = i[1]['oid']
        dup = i[1]['Duplicate']
        cls = i[1]['correct_class']
        if oid not in duplicates:
            duplicates.append(oid)
            src = '/content/all_images/' + oid + '.png'
            dst = '/content/images/' + cls_map[cls] + '/' + oid + '.png'
            shutil.copy(src, dst)
        else:
            pass

    print(len(glob('/content/images/*/*')))
