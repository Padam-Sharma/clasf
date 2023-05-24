import time
import warnings
from clip_tifs import clip_tifs_main
from convex_hull import convex_hull_main
from convert_to_png import convert_png_main
from utils import validate_config, cleanup
import yaml
import os
import sys
import logging
import logging.config
import time
import argparse

warnings.filterwarnings("ignore")

t1 = time.time()

logging.basicConfig(filename='../log.txt', format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s', filemode='w', datefmt='%d-%b-%y %H:%M:%S', level = logging.DEBUG)
logging.config.dictConfig({'version': 1,'disable_existing_loggers': True})

for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)

logger = logging.getLogger('')
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler('../log.txt')
sh = logging.StreamHandler(sys.stdout)
file_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
stream_format = logging.Formatter('%(message)s')
fh.setFormatter(file_format)
sh.setFormatter(stream_format)
logger.addHandler(fh)
logger.addHandler(sh)


def main():
    
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=str)
    args, _ = parser.parse_known_args()
    print("Received arguments {}".format(args))
    
    config = yaml.safe_load(open(str(args.config)))

    # logger.info('---------- Starting to take convex hull ----------')
    # convex_hull_main(config, logger)
    # time.sleep(1)
    # exit()

    # logger.info('---------- Starting tifs clipping ----------')
    # clip_tifs_main(config, logger)
    # time.sleep(1)

    logger.info('---------- Starting convert to png----------')
    convert_png_main(config, logger)
    time.sleep(1)


    t2 = time.time()
    logger.info(f'time_taken: {round(t2-t1,2)} seconds')


if __name__ == '__main__':
    main()