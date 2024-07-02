def config_parser(config_path):
    with open(config_path, 'r') as config:
        config = dict()
        lines = config.readlines()
        for line in lines:
            k, v = line.split(' = ')
            config[k] = v.split('\n')[0]
        return config