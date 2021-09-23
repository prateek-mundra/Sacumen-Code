import pytest
from testWheel import test
output = test.ConfigLibrary()

def test_get_config_content(file_path):
    conf_file =  output.get_config_content("config.cfg")
    assert conf_file


def test_get_yaml_content(file_path):
    yaml_file =  output.get_yaml_content("config.yaml")
    assert yaml_file
    
# def test_name():
#     assert test.ConfigLibrary.name()
