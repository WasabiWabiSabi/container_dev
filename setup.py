import pathlib
from setuptools import find_packages, setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="cmc_csci046_Wasabi_containers",
    version="1.0.0",
    description="Containers from my Data Structures class, including Binary Tree, Binary Search Tree, the AVL Tree, and Heap!",
    long_description=README,
    long_description_content_type="text/markdown"
    url="https://github.com/WasabiWabiSabi/container_dev",
    author="WasabiWabiSabi",
    license="GPL",
    classifiers=[
        "License :: OSI Approved :: GPL License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=find_packages(exclude=("tests",)),
    include_package_data=True,
        ]
    },
)
