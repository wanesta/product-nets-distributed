import socket

config = {}

host = socket.gethostname()
config['host'] = host.lower()
config['location'] = 'apex'

if config['host'] == 'altria':
    config['data_path'] = '/home/kevin/nas/dataset/Ads-RecSys-Datasets'
    config['env'] = 'cpu'
else:
    if config['location'] == 'apex':
        config['data_path'] = '/newNAS/Datasets/MLGroup/Ads-RecSys-Datasets'
    elif config['location'] == 'huawei':
        config['data_path'] = '/home/distributed_train/Data/'
    config['env'] = 'gpu'

default_values_qu = {
    'logdir': '../log',
    'restore': False,
    'val': False,
    'batch_size': 2000,
    'test_batch_size': 5000,
    'learning_rate': 1e-4,
    'dataset': 'criteo_9d',
    'model': 'pin',
    'optimizer': 'adam',
    'l2_scale': 0,
    'embed_size': 30,
    'nn_layers': '[["full", 700], ["act", "relu"], '
                 '["full", 700], ["act", "relu"], '
                 '["full", 700], ["act", "relu"], '
                 '["full", 700], ["act", "relu"], '
                 '["full", 700], ["act", "relu"], '
                 '["full", 1]]',
    'sub_nn_layers': '[["full", 40], ["act", "relu"], '
                     '["full", 5]]',
    'max_step': 0,
    'max_data': 0,
    'num_rounds': 2,
    'eval_level': 5,
    'log_frequency': 1000,
}

default_values_nmz = {
    'logdir': '../log',
    'restore': False,
    'val': False,
    'batch_size': 2000,
    'test_batch_size': 2000,
    'learning_rate': 1e-4,
    'dataset': 'criteo_9d',
    'model': 'pin',
    'optimizer': 'adam',
    'l2_scale': 0,
    'embed_size': 30,
    'nn_layers': '[["full", 700], ["act", "relu"], '
                 '["full", 700], ["act", "relu"], '
                 '["full", 700], ["act", "relu"], '
                 '["full", 700], ["act", "relu"], '
                 '["full", 700], ["act", "relu"], '
                 '["full", 1]]',
    'sub_nn_layers': '[["full", 40], ["act", "relu"], '
                     '["full", 5]]',
    'max_step': 0,
    'max_data': 0,
    'num_rounds': 2,
    'eval_level': 5,
    'log_frequency': 1000,
}
