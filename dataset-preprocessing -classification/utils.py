import pandas as pd
from glob import glob
import shutil
import random
import numpy as np
from tqdm.notebook import tqdm
import os


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

