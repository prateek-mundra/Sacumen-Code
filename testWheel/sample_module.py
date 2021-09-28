# from testWheel.__init__ import *
import yaml
import sys
import os
import io
import json
import configparser
import collections
from configparser import ConfigParser


class ConfigLibrary:

    # def __init__(self):

    def get_config_content(self,file_path):
        """
        this method reads .conf, .cfg file given by the user
        configParser module is used to read confgurations file
        This will give you a dictionary where keys are same as in config file and their corresponding values        
        """
        config = configparser.ConfigParser()
        config.read(file_path)
        details_dict = {s: dict(config.items(s, True))
                        for s in config.sections()}
        print(details_dict)
        
        details_dict__flat = self.parse_dict(details_dict)
        print(details_dict__flat)
    
    
    def parse_dict(self, details_dict, lkey=''):
        ret = {}
        for rkey,val in details_dict.items():
            key = lkey+rkey
            if isinstance(val, dict):
                ret.update(self.parse_dict(val, key+'_'))
            else:
                ret[key] = val
        return ret
   

    def get_yaml_content(self, file_path):
        """ this method reads .yaml file
        to convert yaml file to python package full_load method is used.
        """
        with open(file_path) as file:
            try:
                data = yaml.full_load(file)
                return data
            except yaml.YAMLError as e:
                print(e)

    # writes file data into .json or .env file
    def write_config_file(self, file_path, filename='config', file_extention='json'):
        config = configparser.ConfigParser()
        config.read(file_path)
        new_data = {s: dict(config.items(s, True)) for s in config.sections()}

        if file_extention == 'json':
            filename = filename + '.json'
        else:
            filename += '.env'
                    
        with open(filename, 'w') as file:
            json.dump(new_data, file, indent=4, ensure_ascii=False)

        with open(filename, "w") as f:
            f.write("{}".format(new_data))

        return 'Success'

    def set_config_env(self, env_name, env_value):
        # set environment variable
        os.environ[env_name] = env_value
        print(os.environ[env_var])
        return 'Success'


# file handling : if not json or env
# save file = 


