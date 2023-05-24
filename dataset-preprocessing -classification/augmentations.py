import pandas as pd
from glob import glob
import shutil
import random
from move_images_to_single_folder import make_dir
import numpy as np
from tqdm.notebook import tqdm
import os
import torch
import torchvision.transforms as transforms
from torchvision.utils import save_image
import cv2 as cv
from matplotlib import pyplot as plt
from PIL import Image

total_data = glob('/content/train/*/*')

for i in total_data:
    src = i
    cls = i.split('/')[-2]
    img = i.split('/')[-1]
    dst = '/content/train_aug/' + cls + '/' + img
    shutil.copy(src, dst)

Resize_Transformation = transforms.Compose([
    transforms.ToPILImage(),
    transforms.Resize(size=(512, 512)),
])
Horizontal_Flipping_Transformation = transforms.Compose([
    transforms.ToPILImage(),
    transforms.RandomHorizontalFlip(p=1)
])
Vertical_Flipping_Transformation = transforms.Compose([
    transforms.ToPILImage(),
    transforms.RandomVerticalFlip(p=1)
])
Color_Transformation = transforms.Compose([
    transforms.ToPILImage(),
    transforms.ColorJitter(brightness=(0.1, 0.6), contrast=1, saturation=0, hue=0.4)
])
Contrast_Transformation = transforms.Compose([
    transforms.ToPILImage(),
    transforms.RandomAutocontrast(p=1)
])
Rotate_Transformation = transforms.Compose([
    transforms.ToPILImage(),
    transforms.RandomRotation(degrees=66)
])


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


def get_len_aug(type):
    print(len(glob('/content/train_aug/' + type + '/*')))


def get_len(type):
    print(len(glob('/content/train/' + type + '/*')))


cls_ = ['com', 'hoa', 'res']

for i in cls_:
    get_len_aug(i)

for i in tqdm(glob('/content/train_aug/res/*')):
    augment(i)

for i in tqdm(glob('/content/train_aug/hoa/*')):
    augment(i)

cls_ = ['com', 'hoa', 'res']

for i in cls_:
    get_len_aug(i)

dl_hoa = glob('/content/train_aug/hoa/*')
random.shuffle(dl_hoa)

dl_res = glob('/content/train_aug/res/*')
random.shuffle(dl_res)

for i in dl_hoa[0:1400]:
    os.remove(i)

cls_ = ['com', 'hoa', 'res']

for i in cls_:
    get_len_aug(i)
