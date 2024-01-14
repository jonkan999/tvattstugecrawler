import configparser
import os

def get_config():
  config = configparser.ConfigParser()
  config.read(os.path.expanduser('~/.config.ini'))

  username = config['credentials']['username']
  password = config['credentials']['password']
  
  return username, password
