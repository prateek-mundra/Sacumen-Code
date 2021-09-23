### Details about Module ###
This Project is designed to create a module which can read .yaml, .cfg and .conf file formats and generate a dictionary out of it.

Depending upon the parameters given, module should store the configurations in .env or .json file format or set the configurations in os environment.

1. Create Virutal Environment
    `pip install virtualenv` /* Install virtual environment */
    `virtualenv venv`  /* Create a virtual environment */
    `venv/bin/activate` /* Activate the virtual environment */

2. Install yaml module
    `pip install pyyaml`

3. Install pytest module for creating unit test cases
    `pip install pytest`

4. Before creating wheel file, we need to install a couple of python packages
    `pip install wheel setuptools`

5. Generate wheel file
    `python setup.py bdist_wheel`

6. A dist folder gets created which stores the wheel(.whl) file.

7. Run pip install < wheel file name > 

