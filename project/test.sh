#!/bin/bash


# Store the current working directory
project_dir=$(pwd)

echo "=== Executing pipeline ==="


# Execute your pipeline
python project/data/pipeline.py

# Validate the output file(s)
if [ -f "project/data/nuremberg_stops_immoscout.sqlite" ]; then
  echo "Output file(s) exist."
else
  echo "Output file(s) not found."
fi

echo "=== Running Tests ==="
python project/test.py

read -p "Press any key to continue... " -n1 -s
