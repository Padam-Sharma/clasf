import shutil
import geopandas as gpd
import shapely
import os
import warnings
warnings.filterwarnings("ignore")



def multiparts_to_singleparts(geometries_list):
    """
    Converts multipolygons to polygons.
    """

    flattened_geometries = []
    
    for i in geometries_list:
        if type(i)== shapely.geometry.multipolygon.MultiPolygon:
            for j in i:
                flattened_geometries.append(j)

        else:
            flattened_geometries.append(i)

    return flattened_geometries



def get_vertices_list(geometries):
    """
    Dissolves polygons into one polygon and then undissolve it to merge overlapping polygons.
    """    
    
    gseries = gpd.GeoSeries(geometries)
    single_parts_geometries = multiparts_to_singleparts(gseries)

    vertices_list = []
    
    for polygon in  single_parts_geometries:
        if polygon == None:
            continue
        x, y = polygon.exterior.coords.xy
        vertices = [shapely.geometry.Point(x[i], y[i]) for i in range(len(x))]
    
        vertices_list=  vertices_list + vertices

    return vertices_list



def count_attributes(file_name):
    gdf = gpd.read_file(file_name)
    geometry = gdf['geometry']
    polygons = []
    multipolygons = []
    others = []

    for i in geometry:
        if type(i) == shapely.geometry.multipolygon.MultiPolygon:
            multipolygons.append(i)

        elif type(i) == shapely.geometry.polygon.Polygon:
            polygons.append(i)
        
        else:
            others.append(i)

    vertices = get_vertices_list(geometry)
    attributes = {"vertices": len(vertices), "polygons": len(polygons), "multipolygons": len(multipolygons), "others": len(others)}
    return attributes


def count_attributes_in_folder(folder_path):
    files = os.listdir(folder_path)


def validate_config(config, logger):
    """
    Checks the validity of the config file and applies certain checks before accepting the config.
    """

    if not os.path.exists(config["PATH"]["input"]):
        logger.error(f'Config is not valid. Input folder path \"{config["PATH"]["input"]}\" does not exist. Exiting...')
        raise ValueError(f'Config is not valid. Input folder path \"{config["PATH"]["input"]}\" does not exist. Exiting...')


    folder_types = os.listdir(config["PATH"]["input"])
    classes_in_config = list(config['GENERAL']['classes'].keys())

    for i in folder_types:
        classes_in_input_folder = os.listdir(f'{config["PATH"]["input"]}/{i}/annotations')
        classes_in_input_folder = [j for j in classes_in_input_folder if '.' not in j]

        for j in classes_in_input_folder:
            if j not in classes_in_config:
                logger.error(f'Input folder contains class "{j}" in folder_type "{i}" which is not available in config. Exiting...')
                raise ValueError(f'Input folder contains classes "{j}" in folder_type "{i}" which is not available in config. Exiting...')
                
    pixel_values = list(config['GENERAL']['classes'].values())
    
    if 0 in pixel_values:
        logger.error('Config is not valid. Found "0" as pixel value in classes. Exiting...')
        raise ValueError('Config is not valid. Found "0" as pixel value in classes. Exiting...')


    pixel_values = list(config['GENERAL']['classes'].values())
    background_class = max(pixel_values) + 1

    if background_class in config['PIXELS']['class_order']:
        logger.error('Config is not valid. Found background pixel value in config["PIXELS"]["class_order"]. Exiting...')
        raise ValueError('Config is not valid. Found background pixel value in config["PIXELS"]["class_order"]. Exiting...')

    pixel_values_in_order = config['PIXELS']['class_order']

    for j in pixel_values:
        if j not in pixel_values_in_order:
            logger.error('Config is not valid. Number of pixel values is not consistent between config["GENERAL"]["classes"] and config["PIXELS"]["class_order"]. Exiting...')
            raise ValueError('Config is not valid. Number of pixel values is not consistent between config["GENERAL"]["classes"] and config["PIXELS"]["class_order"]. Exiting...')
                

def cleanup(config):
    shutil.rmtree(config["PATH"]["intermediate"], ignore_errors=True)
    shutil.rmtree(config["PATH"]["output"], ignore_errors=True)
