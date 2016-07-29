import os, logging
try:
    with open('pyco-nlp.cfg', 'r') as f:
        conf = f.readlines()
        configuration_dict = dict(line.split('=') for line in conf)
except FileNotFoundError:
    logging.error('Congiguration file not found')
os.system('./server.sh')