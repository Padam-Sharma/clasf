import os, sys
from PIL import Image
Image.MAX_IMAGE_PIXELS = None
from glob import glob

import os
import multiprocessing as mp
import threading
import shutil
import warnings
warnings.filterwarnings("ignore")
import logging
logger = logging.getLogger('')
from tqdm import tqdm

def convert_png(infile, outfile):
    im = Image.open(infile)
    new_width = 512
    aspect_ratio = im.height / im.width
    new_height = int(new_width * aspect_ratio)
    resized_image = im.resize((new_width, new_height), Image.ANTIALIAS)
    out = resized_image.convert("RGB")
    out.save(outfile, "PNG", quality=100)

def convert_png_process_folder(config):
    logger.info(f'Converting tifs to png')
    clipped_tifs_dir = f'{config["PATH"]["output"]}/tifs_clipped'
    png_dir = f'{config["PATH"]["output"]}/png_clipped'
    
    shutil.rmtree(png_dir, ignore_errors=True)
    os.makedirs(png_dir, exist_ok=True)
    num_processes = 4 

    task_list = []
    for tif in os.listdir(clipped_tifs_dir):
        if tif .endswith('.tif'):
            file_name = tif.split('.')[0]
            in_tif_path = os.path.join(clipped_tifs_dir, tif)        
            out_png_path = os.path.join(png_dir, file_name+'.png')
            if os.path.exists(in_tif_path):
                task_list.append([in_tif_path, out_png_path])
            else:
                logger.warning(f'Skipping {in_tif_path} as {in_tif_path} doesn\'t exist')
                
    p = mp.Pool(num_processes)
    p.starmap(convert_png, task_list)
    p.close()
    p.join()

def convert_png_main(config, tmp_logger):
    global logger 
    logger = tmp_logger
      
    threads = []

    thread = threading.Thread(target=convert_png_process_folder, args=(config,))
    threads.append(thread)
    thread.start()
        
    for thread in tqdm(threads):
        thread.join()