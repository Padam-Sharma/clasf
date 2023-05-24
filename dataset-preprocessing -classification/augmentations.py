from glob import glob
import shutil
import random
import numpy as np
from tqdm.notebook import tqdm
import os
from utils import Resize_Transformation, Rotate_Transformation, Color_Transformation, Contrast_Transformation, \
    Horizontal_Flipping_Transformation, Vertical_Flipping_Transformation
from utils import get_len, get_len_aug, make_dir
from PIL import Image


def augmentations_main(config, logger):
    pwd_root_pth = config['PATH']['pwd']['root_path']
    aug_pth = config['PATH']['pwd']['aug_img_path']

    total_data = glob(pwd_root_pth+'/train/*/*')

    make_dir(aug_pth)
    make_dir(aug_pth + '/com')
    make_dir(aug_pth + '/hoa')
    make_dir(aug_pth + 'res')

    for i in total_data:
        src = i
        cls = i.split('/')[-2]
        img = i.split('/')[-1]
        dst = aug_pth + cls + '/' + img
        shutil.copy(src, dst)

    def prob():
        return random.choice([0, 1, 2])

    def augment(img_pth):
        image = Image.open(img_pth)
        # display(img)
        image = np.array(image)
        # save_pth = img_pth.replace('clswise', 'clswise_aug')
        save_pth = img_pth
        save_pth = save_pth[:-4] + '_' + '.png'
        x = 0
        if prob():
            aug_img = Resize_Transformation(image)
            save_pth = save_pth.split('.')[0] + str(x) + '.png'
            x += 1
            aug_img.save(save_pth)
            # display(aug_img)
        if prob():
            aug_img = Horizontal_Flipping_Transformation(image)
            save_pth = save_pth.split('.')[0] + str(x) + '.png'
            x += 1
            aug_img.save(save_pth)
            # display(aug_img)
        if prob():
            aug_img = Vertical_Flipping_Transformation(image)
            save_pth = save_pth.split('.')[0] + str(x) + '.png'
            x += 1
            aug_img.save(save_pth)
            # display(aug_img)
        if prob():
            aug_img = Color_Transformation(image)
            save_pth = save_pth.split('.')[0] + str(x) + '.png'
            x += 1
            aug_img.save(save_pth)
            # display(aug_img)
        if prob():
            aug_img = Rotate_Transformation(image)
            save_pth = save_pth.split('.')[0] + str(x) + '.png'
            x += 1
            aug_img.save(save_pth)
            # display(aug_img)
        if prob():
            aug_img = Contrast_Transformation(image)
            save_pth = save_pth.split('.')[0] + str(x) + '.png'
            x += 1
            aug_img.save(save_pth)
            # display(aug_img)

    cls_ = ['com', 'hoa', 'res']

    for i in cls_:
        get_len_aug(i)

    for i in tqdm(glob(aug_pth + '/res/*')):
        augment(i)

    for i in tqdm(glob(aug_pth + '/hoa/*')):
        augment(i)

    cls_ = ['com', 'hoa', 'res']

    for i in cls_:
        get_len_aug(i)

    dl_hoa = glob(aug_pth + '/hoa/*')
    random.shuffle(dl_hoa)

    dl_res = glob(aug_pth + '/res/*')
    random.shuffle(dl_res)

    for i in dl_hoa[0:1400]:
        os.remove(i)

    cls_ = ['com', 'hoa', 'res']

    for i in cls_:
        get_len_aug(i)
