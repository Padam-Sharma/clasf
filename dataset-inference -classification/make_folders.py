import pandas as pd
from glob import glob
import shutil
import random
import numpy as np
from tqdm.notebook import tqdm
from utils import make_dir
import os


def make_folders_main(config, logger):
    inference_pth = config['inference']['drive']['tif_ann_pth']
    pwd_root_pth = config['inference']['pwd_root_pth']

    input_dir = config['PATH']['input']
    intermediate_dir = config['PATH']['intermediate']
    output_dir = config['PATH']['output']

    make_dir(input_dir)
    make_dir(intermediate_dir)
    make_dir(output_dir)
    make_dir(output_dir+'/png_clipped')

    move_inference_folder_cmd = f"cp -r {inference_pth} {input_dir}"
    print("Moving tiffs and annotations to input directory")
    os.system(move_inference_folder_cmd)



