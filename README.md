# ML_property_type_classification

Commands to run both training and preprocessing (tested in COLAB)

```bash
pip install -q geopandas rasterio
python '/content/clasf/dataset-preprocessing-classification/main.py' --config '/content/clasf/dataset-inference-classification/config.yaml'
python '/content/clasf/dataset-inference-classification/main.py' --config '/content/clasf/dataset-inference-classification/config.yaml'
```

## 1. Data Preprocessing for Training

    Changed directory structure and removed mislabeling by moving images to their
    respective correct classes.

    Preprocess the dataset
    
    Split data into train, val and test in 7:2:1

    Applied augmentations to account for class imbalance

    Trained and tested EfficientNet-B0 model on this dataset

## 2. Data Preprocessing for Inference

    Changed directory structure and preprocessed the dataset

    Executed inference script and get predictions corresponding to file names