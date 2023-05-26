# ML_property_type_classification


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