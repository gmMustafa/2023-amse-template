#!/bin/bash


# Store the current working directory
project_dir=$(pwd)

echo "=== Executing pipeline ==="

# Change directory to the data folder
cd ./data

# Execute your pipeline
python pipeline.py


# Validate the output file(s)
if [ -f "./data/nuremberg_stops_immoscout.sqlite" ]; then
  echo "Output file(s) exist."
else
  echo "Output file(s) not found."
fi

# Change directory back to the project folder
cd "$project_dir"

echo "=== Running Tests ==="
python test.py

read -p "Press any key to continue... " -n1 -s
