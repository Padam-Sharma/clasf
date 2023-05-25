import pandas as pd
from glob import glob
import shutil
import random
import numpy as np
from tqdm.notebook import tqdm
from utils import make_dir
import os


def make_folders_main(config, logger):
    inference_tif_pth = config['inference']['drive']['tif_pth']
    inference_ann_pth = config['inference']['drive']['ann_pth']
    pwd_root_pth = config['inference']['pwd_root_pth']

    input_dir = config['PATH']['input']
    intermediate_dir = config['PATH']['intermediate']
    output_dir = config['PATH']['output']

    make_dir(input_dir)
    make_dir(intermediate_dir)
    make_dir(output_dir)
    make_dir(output_dir+'/png_clipped')

    move_tif_cmd = f"cp -r {inference_tif_pth} {input_dir}"
    move_ann_cmd = f"cp -r {inference_ann_pth} {input_dir}"
    print("Moving tiffs and annotations to input directory")
    os.system(move_tif_cmd)
    os.system(move_ann_cmd)



