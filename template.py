''' specify the projects structure

    split the paths into folders and files
    check if the folders are empty then create
    check if the files do not exist and create them
'''
import os
import logging

from pathlib import Path
project_name='mlproject'

list_of_files=[
    ".github/workflows.gitkeep",
    f"src/{project_name}/__init__.py",
   
    f"src/{project_name}/components/__init__.py",
    
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",

    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "main.py",
    "schema.yaml",
    "params.yaml",
    "config.yaml",
    "requirements.txt",
    "setup.py",
    "app.py",
    "dockerfile"
   
]

'''for filepath in list_of_files:
    filepath=Path(filepath)
    filedir,filename=os.path.split(filepath)

    if filedir!="":
        os.makedirs(filedir,exist_ok=True)
    if(not os.path.exists(filename)):
        with open(filename,'w') as f:
            pass

'''
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir = filepath.parent
    filename = filepath.name

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)

    full_filepath = filedir / filename

    if not os.path.exists(full_filepath):
        with open(full_filepath, 'w'):
            pass   



    

    
