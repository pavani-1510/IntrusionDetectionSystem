def setup_logging(log_file='app.log'):
    import logging
    logging.basicConfig(filename=log_file, level=logging.INFO,
                        format='%(asctime)s:%(levelname)s:%(message)s')

def load_config(config_file='config.json'):
    import json
    with open(config_file, 'r') as file:
        config = json.load(file)
    return config

def visualize_data(data, title='Data Visualization'):
    import matplotlib.pyplot as plt
    plt.figure(figsize=(10, 6))
    plt.title(title)
    plt.plot(data)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.show()