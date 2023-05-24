import pandas as pd
from glob import glob
import shutil
import random
import numpy as np
from tqdm.notebook import tqdm
import os


def correcting_labels_main(config, logger):
    csv_pth = config['PATH']['drive']['csv_2_path']
    new_img_pth = config["PATH"]['drive']['new_img_pth']
    pwd_root_pth = config['PATH']['pwd']['root_path']
    combined_img_path = config["PATH"]['pwd']['combined_img_path']

    move_csv_cmd = f"cp {csv_pth} {pwd_root_pth}"
    move_img_cmd = f"cp -r {new_img_pth} {pwd_root_pth}"
    os.system(move_csv_cmd)
    os.system(move_img_cmd)
    feb_df = pd.read_csv(csv_pth)

    duplicates = []
    cls_map = {'COMM': 'com', 'HOA': 'hoa', 'RES': 'res'}

    print('Starting to split images by class...')
    for i in feb_df.iterrows():
        oid = i[1]['oid']
        cls = i[1]['correct class']
        if oid not in duplicates:
            duplicates.append(oid)
            src = new_img_pth + '/' + oid + '.png'
            dst = combined_img_path + cls_map[cls] + '/' + oid + '.png'
            print(src)
            print(dst)
            print()
            shutil.copy(src, dst)
        else:
            pass
    print('Split complete... \n')
    print('No. of images after split', len(glob(combined_img_path+'/*/*')))

    print('No. of images after split classwise \n')
    for i in glob(combined_img_path+'/*'):
        print(i.split('/')[-1], len(glob(i + '/*')))
