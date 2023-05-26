import os
import multiprocessing as mp
import threading
import shutil
import warnings

warnings.filterwarnings("ignore")
import logging

logger = logging.getLogger('')
from glob import glob
import shapely
import geopandas as gpd


def convex_hull(input_path, out_path):
    hull_gdf = gpd.read_file(input_path).convex_hull
    hull_gdf.to_file(out_path, driver="GeoJSON")
    pass


def convex_hull_process_folder(config):
    logger.info(f'Taking convex hull')
    input_parcel_dir = f'{config["PATH"]["input"]}/parcel'
    output_parcel_dir = f'{config["PATH"]["input"]}/annotations-conv_hull'

    shutil.rmtree(output_parcel_dir, ignore_errors=True)
    os.makedirs(output_parcel_dir, exist_ok=True)
    num_processes = 4

    task_list = []
    for parcel in os.listdir(input_parcel_dir):
        if parcel.endswith('.geojson'):
            file_name = parcel.split('.')[0]
            in_parcel_path = os.path.join(input_parcel_dir, file_name + '.geojson')
            out_parcel_path = os.path.join(output_parcel_dir, file_name + '.geojson')
            if os.path.exists(in_parcel_path):
                task_list.append([in_parcel_path, out_parcel_path])
            else:
                logger.warning(f'Skipping {in_parcel_path} as {out_parcel_path} doesn\'t exist')

    p = mp.Pool(num_processes)
    p.starmap(convex_hull, task_list)
    p.close()
    p.join()


def convex_hull_main(config, tmp_logger):
    global logger
    logger = tmp_logger

    threads = []

    thread = threading.Thread(target=convex_hull_process_folder, args=(config,))
    threads.append(thread)
    thread.start()

    for thread in threads:
        thread.join()

