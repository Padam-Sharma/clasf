import pandas as pd
from glob import glob
import shutil
import random
import numpy as np
from tqdm.notebook import tqdm
import os
import torch
import torchvision.transforms as transforms
from torchvision.utils import save_image


def make_dir(path):
    os.makedirs(path, exist_ok=True)


def rmdir(path):
    shutil.rmtree(path)


def movettv(path, type):
    for i in tqdm(path):
        cls = i.split('/')[-2]
        img = i.split('/')[-1]
        src = i
        dst = '/content/' + type + '/' + cls + '/' + img
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


def get_len_aug(type):
    print(len(glob('/content/train_aug/' + type + '/*')))


def get_len(type):
    print(len(glob('/content/train/' + type + '/*')))
