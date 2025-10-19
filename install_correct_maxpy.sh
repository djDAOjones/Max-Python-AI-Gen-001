#!/bin/bash
# Install the CORRECT MaxPy for Max/MSP from GitHub

# Uninstall the wrong package
pip uninstall -y maxpy

# Install directly from GitHub
pip install git+https://github.com/Barnard-PL-Labs/MaxPy.git
