import pandas as pd
from glob import glob
import shutil
import random
import numpy as np
from tqdm.notebook import tqdm
from utils import make_dir
import os


def move_to_single_folder_main(config, logger):
    img_pth = config['PATH']['drive']['image_path']
    csv_pth = config['PATH']['drive']['csv_1_path']
    pwd_root_pth = config['PATH']['pwd']['root_path']
    org_img_combined_path = config["PATH"]['pwd']['org_img_combined_path']
    combined_img_path = config["PATH"]['pwd']['combined_img_path']

    move_csv_cmd = f"cp {csv_pth} {pwd_root_pth}"
    move_img_cmd = f"cp -r {img_pth} {pwd_root_pth}"
    os.system(move_csv_cmd)
    os.system(move_img_cmd)

    df = pd.read_csv(csv_pth)

    print('No. of unique rows :', len(set(list(df['oid']))), 'No. of total rows :', len(list(df['oid'])))

    make_dir('all_images')
    make_dir('images')
    make_dir('images/com')
    make_dir('images/hoa')
    make_dir('images/res')

    test_pth = glob(img_pth+'/test/*/*')
    train_pth = glob(img_pth+'/train/*/*')
    val_pth = glob(img_pth+'/val/*/*')

    print(len(test_pth) + len(train_pth) + len(val_pth))

    print('Moving images from train, val and test to single folder')
    all_pth = test_pth + train_pth + val_pth
    for i in tqdm(all_pth):
        src = i
        dst = org_img_combined_path + i.split('/')[-1]
        shutil.copy(src, dst)
    print('Moved...')

    print('No. of images after moving :',len(glob(org_img_combined_path+'/*')))

    print('Starting to split images by class...')
    duplicates = []
    cls_map = {'Comm': 'com', 'HOA': 'hoa', 'Resi': 'res'}
    for i in df.iterrows():
        oid = i[1]['oid']
        dup = i[1]['Duplicate']
        cls = i[1]['correct_class']
        if oid not in duplicates:
            duplicates.append(oid)
            src = org_img_combined_path + oid + '.png'
            dst = combined_img_path + cls_map[cls] + '/' + oid + '.png'
            shutil.copy(src, dst)
        else:
            pass
    print('Split complete...')

    print('No. of images after split', len(glob(combined_img_path+'/*/*')))
