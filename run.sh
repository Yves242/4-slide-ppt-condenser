#!/bin/bash

# Define the folder 
folder="slides"

# STEP 1: Remove old files if it exists
if [ -d "$folder" ]; then
    # Remove all contents inside the folder but retain the folder
    rm -rf "$folder"/*
else
    echo "The folder '$folder' does not exist."
fi

# STEP 2: Extract images
python3 part1.py

# STEP 3: Merge all into 1 pdf
python3 part2.py

