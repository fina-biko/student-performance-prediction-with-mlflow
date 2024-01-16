from setuptools import setup,find_packages
import os
from typing import list

HYPHEN_e_dot='e .'
def requirements(filename)-> list[str]:
    requirements=[]
    with open (filename) as fileobj:
        requirements=fileobj.readlines()
        requirements=[line.replace('/n','')for line in requirements]
        if HYPHEN_e_dot in requirements:
            requirements.remove(HYPHEN_e_dot)
        return requirements
         

    
setup(
    name='RUFINA ATIENO',
    author='KRISH NAIK',
    packages=find_packages(),
    requires=requirements(requirements.txt)
)
    