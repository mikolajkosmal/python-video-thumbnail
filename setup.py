#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open("README.md") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()

requirements = [
    "opencv-python==4.2.0.32",  # Last 2.7 support version
]

test_requirements = [
    "pytest>=3",
]

setup(
    author="Mikolaj Kosmal",
    author_email="mikolaj.kosmal@gmail.com",
    python_requires="<3.9",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    description="Python package for capturing frames from video.",
    install_requires=requirements,
    license="MIT license",
    long_description=readme + "\n\n" + history,
    include_package_data=True,
    keywords="python_video_thumbnail",
    name="python_video_thumbnail",
    packages=find_packages(
        include=["python_video_thumbnail", "python_video_thumbnail.*"]
    ),
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/mikolajkosmal/python_video_thumbnail",
    version="0.1.0",
    zip_safe=False,
)
