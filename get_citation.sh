#!/bin/bash

cd /home/jay/projects/daily_motiv
# Don't want to see output from this step
pip install -r requirements.txt> /dev/null 2>&1
./maintain_log_file.sh

python3 main.py


