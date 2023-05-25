import time
import warnings
import yaml
import os
import sys
import logging
import logging.config
import time
import argparse
from move_images_to_single_folder import move_to_single_folder_main
from correcting_labels import correcting_labels_main
from train_val_test_split import train_val_test_split_main
from augmentations import augmentations_main

warnings.filterwarnings("ignore")

t1 = time.time()

logging.basicConfig(filename='../log.txt', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', filemode='w',
                    datefmt='%d-%b-%y %H:%M:%S', level=logging.DEBUG)
logging.config.dictConfig({'version': 1, 'disable_existing_loggers': True})

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

    # logger.info('---------- Starting to move all images to single folder ----------')
    # move_to_single_folder_main(config, logger)
    # time.sleep(1)

    # logger.info('---------- Correcting labels ----------')
    # correcting_labels_main(config, logger)
    # time.sleep(1)

    # logger.info('---------- Splitting into train, val and test ----------')
    # train_val_test_split_main(config, logger)
    # time.sleep(1)

    logger.info('---------- Augmenting train dataset ----------')
    augmentations_main(config, logger)
    time.sleep(1)

    logger.info('---------- Training and testing the model ----------')
    augmentations_main(config, logger)
    time.sleep(1)

    t2 = time.time()
    logger.info(f'time_taken: {round(t2 - t1, 2)} seconds')


if __name__ == '__main__':
    main()