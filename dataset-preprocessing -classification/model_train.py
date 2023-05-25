import os

def model_train_main(config, logger):
    os.system('git clone https://github.com/Padam-Sharma/pytorch-image-models.git')
    os.system('%%cd pytorch-image-models')
    os.system('pip install -q -e .')
    os.system('pip install -q focal_loss_torch')

    train_py_pth = config['train']['train_py_pth']
    train_dir = config['train']['train_dir']
    model_type = config['train']['model_type']
    batch_size = config['train']['batch_size']
    img_size = config['train']['img_size']
    val_split = config['train']['val_split']
    epochs = config['train']['epochs']
    num_classes = config['train']['num_classes']

    train_cmd = f'python {train_py_pth} --data-dir {train_dir} --model {model_type} --pretrained --batch-size {batch_size} --img-size {img_size} --val-split {val_split} --epochs {epochs} --num-classes {num_classes}'

    os.system(train_cmd)

    test_py_pth = config['test']['val_py_pth']
    test_dir = config['test']['val_dir']
    model_type = config['test']['model_type']
    saved_model_path = config['test']['saved_model_path']
    batch_size = config['test']['batch_size']
    img_size = config['test']['img_size']
    num_classes = config['test']['num_classes']
    log_freq = config['test']['log_freq']

    test_cmd = f'python {test_py_pth} --data-dir {test_dir} --model {model_type} --checkpoint {saved_model_path} --img-size {img_size} --batch-size {batch_size} --num-classes {num_classes} --log-freq {log_freq}'

    os.system(test_cmd)
