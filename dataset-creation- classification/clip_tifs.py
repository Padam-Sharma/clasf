import os
import multiprocessing as mp
import threading
import shutil
import warnings
warnings.filterwarnings("ignore")
import logging
logger = logging.getLogger('')
from tqdm import tqdm

def clip_tif(in_shp_path, in_tif_path, out_tif_path): 
    """
    Clips tifs to the extent of the parcel. It helps in reducing the size of the tif.
    """
    try:
        os.system('gdalwarp -q -of GTiff -cutline {} -crop_to_cutline {} {}'.format(in_shp_path, in_tif_path, out_tif_path))
    except Exception as e:
        logger.warning(e)
        logger.warning('some issue in ', in_tif_path)


def clip_tifs_process_folder(config, folder_type):
    logger.info(f'Clipping tifs for {folder_type}')
    input_tifs_dir = f'{config["PATH"]["input"]}/{folder_type}/tifs'
    input_parcel_dir = f'{config["PATH"]["input"]}/{folder_type}/annotations-conv_hull'
    clipped_tifs_dir = f'{config["PATH"]["output"]}/{folder_type}/tifs_clipped'
    
    shutil.rmtree(clipped_tifs_dir, ignore_errors=True)
    # print("yess")
    os.makedirs(clipped_tifs_dir, exist_ok=True)
    num_processes = 4 

    task_list = []
    for tif in os.listdir(input_tifs_dir):
        if tif .endswith('.tif'):
            file_name = tif.split('.')[0]
            in_tif_path = os.path.join(input_tifs_dir, tif)        
            in_shp_path = os.path.join(input_parcel_dir, file_name+'.geojson')
            out_tif_path = os.path.join(clipped_tifs_dir, file_name+'.tif')
            if os.path.exists(in_shp_path):
                task_list.append([in_shp_path, in_tif_path, out_tif_path])
            else:
                logger.warning(f'Skipping {in_tif_path} as {in_shp_path} doesn\'t exist')
                
    p = mp.Pool(num_processes)
    p.starmap(clip_tif, task_list)
    p.close()
    p.join()


def clip_tifs_main(config, tmp_logger):
    global logger 
    logger = tmp_logger
    folder_types = os.listdir(config["PATH"]["input"])
    print(folder_types)
    folder_types = sorted(folder_types)
      
    threads = []

    for folder_type in folder_types:
        thread = threading.Thread(target=clip_tifs_process_folder, args=(config, folder_type,))
        threads.append(thread)
        thread.start()
        
    for thread in tqdm(threads):
        thread.join()

    #for f in folder_types:
    #    clip_tifs_process_folder(config, f)
    
        