"""Setup script."""
import os
from setuptools import setup, find_packages

setup(
    # mandatory
    name="causality_notes",
    # mandatory
    version="0.1",
    # mandatory
    author="Eric J. Ma",
    description=("Notes on causal inference methods."),
    packages=find_packages(),
)
