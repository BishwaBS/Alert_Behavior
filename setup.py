from setuptools import setup, find_packages
import codecs
import os

setup(
    name="Alert_Behavior",
    version = "1.0",
    author="Bishwa Sapkota",
    packages=["Alert_Behavior"],
    # long_description=long_description,
    install_requires =[
        "numpy ",
        "mediapipe ",
        "opencv-python",
        ]


)