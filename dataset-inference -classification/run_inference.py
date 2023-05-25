import os

def model_train_main(config, logger):
    os.system('git clone https://github.com/Padam-Sharma/pytorch-image-models.git')
    os.system('cd "/content/pytorch-image-models"')
    os.system('pip install -q -e "/content/pytorch-image-models"')
    os.system('pip install -q focal_loss_torch')

    test_py_pth = config['test']['test_py_pth']
    test_dir = config['test']['test_dir']
    model_type = config['test']['model_type']
    saved_model_path = config['test']['saved_model_path']
    batch_size = config['test']['batch_size']
    img_size = config['test']['img_size']
    num_classes = config['test']['num_classes']
    log_freq = config['test']['log_freq']

    test_cmd = f'python {test_py_pth} --data-dir {test_dir} --model {model_type} --checkpoint {saved_model_path} --img-size {img_size} --batch-size {batch_size} --num-classes {num_classes} --log-freq {log_freq}'

    os.system(test_cmd)
    