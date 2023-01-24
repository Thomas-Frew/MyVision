#!/usr/bin/env python3
"""
    File Name: helpers.py
    Author: Thomas Frew
    Date created: 07/01/2023
    Date last modified: 24/01/2023
    Python Version: 3.11
    
    Helper functions for the MyVision, computer vision framework.
"""

# Use os
from os import listdir, getcwd

# Use the path library
from pathlib import Path

# Use csvs
import csv


def read_dataset_dir():
    """
    Reads the dataset's directory from the user.
    """
    suffix = input("Please enter the folder your images are located in.\n")
    directory = getcwd() + "\\" + suffix + "\\"
    return directory

def read_pngs(directory):
    """
    Returns a list of all PNGs in a given directory.
    """
    # A list of all files in the current directory
    file_names = listdir(directory)
    
    # The upper limit of PNGs to import
    N = 10000;
    
    # The list of imported PNGs
    png_file_names = []

    # Iterator
    n = 0

    # Read up to N files from the given directory
    for file in file_names:
        if (file.endswith('.png')):
            png_file_names.append(directory + file)
            n += 1

    # Confirm the number of loaded files
    print(f"Loaded {n} files from {directory}")
    
    # Return PNGs from the given directory
    return png_file_names


def save_training_dataset(training_data):
    """
    Saves a list of training data as a CSV training dataset
    """
    with open("Dataset.csv", "w+", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(training_data)



