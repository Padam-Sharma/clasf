import os

def run_inference_main(config, logger):
    os.system('git clone https://github.com/Padam-Sharma/pytorch-image-models.git')
    os.system('cd "/content/pytorch-image-models"')
    os.system('pip install -q -e "/content/pytorch-image-models"')
    os.system('pip install -q focal_loss_torch')

    test_py_pth = config['inference']['test_py_pth']
    test_dir = config['inference']['test_dir']
    model_type = config['inference']['model_type']
    saved_model_path = config['inference']['saved_model_pth']
    batch_size = config['inference']['batch_size']
    img_size = config['inference']['img_size']
    num_classes = config['inference']['num_classes']
    log_freq = config['inference']['log_freq']

    test_cmd = f'python {test_py_pth} --data-dir {test_dir} --model {model_type} --checkpoint {saved_model_path} --img-size {img_size} --batch-size {batch_size} --num-classes {num_classes} --log-freq {log_freq}'

    os.system(test_cmd)
