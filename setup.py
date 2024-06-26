from setuptools import setup , find_packages
from typing import List

def get_requirements(filepath : str) -> List[str]:
    HYPHEN_DOT_E = "-e "
    requirements = []
    with open(filepath, 'r') as file_obj:
        result = file_obj.readlines()
        
        for package in result:
            requirements.append(package[:-1])

    for package in requirements:
        if (package == HYPHEN_DOT_E):
            requirements.remove(HYPHEN_DOT_E)
    return requirements

setup(
    name="Text Summarizer",
    version="0.0.1",
    description="An app which is gonna summarise the text.",
    long_description="This app is based upon the concept of fine tuning the existing model and traininf the fine-tuned model to get results.",
    author="Piyush Goyal",
    author_email="piyushgoyal11824@gmail.com",
    packages=find_packages(),
    install_requires = get_requirements("./requirements.txt"),
)

