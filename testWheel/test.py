# from testWheel.__init__ import *
import yaml
import sys
import os
import io
import json
from simpleconfigparser import simpleconfigparser

class ConfigLibrary():

    # def __init__(self):

    def get_config_content(file_path):    #reads .conf, .cfg file format
        config = simpleconfigparser()
        config.read(file_path)
        details_dict = {s: dict(config.items(s, True)) for s in config.sections()}
                
        return details_dict
    
    def get_yaml_content(file_path):    # reads .yaml file format
        with open(file_path) as file:
            data = yaml.full_load(file)
        return data
        
    def write_config_file(file_path, filename = 'config',file_extention='json'):   # writes file data into .json or .env file
        config = simpleconfigparser()
        config.read(file_path)
        new_data = {s: dict(config.items(s, True)) for s in config.sections()}

        if file_extention == 'json':
            filename = filename + '.json'
        else:
            filename = '.env'
        with open(filename, 'w') as file:
            json.dump(new_data, file, indent = 4, ensure_ascii=False)
            
        with open(filename, "w") as f:
            f.write("{}".format(new_data))

        return 'Success'

    def set_config_env(env_name,env_value):

        os.environ[env_name] = env_value

        return 'Success'



