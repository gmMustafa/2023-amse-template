#!/bin/bash -x

echo "=== Executing pipeline ==="
# Execute your pipeline
python project/data/pipeline.py
#python data/pipeline.py

# Validate the output file(s)
if [ -f "nuremberg_stops_immoscout.sqlite" ]; then
  echo "Output file(s) exist."
else
  echo "Output file(s) not found."
fi

echo "=== Running Tests ==="
python project/test.py
#python test.py

read -p "Press any key to continue... " -n1 -s
exit 0
