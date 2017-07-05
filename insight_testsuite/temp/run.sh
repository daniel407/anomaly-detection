#!/bin/bash

python3 ./src/process_log.py ./log_input/batch_log.json ./log_input/stream_log.json ./log_output/flagged_purchases.json

#python3 ./src/process_log.py ./sample_dataset/batch_log.json ./sample_dataset/stream_log.json ./log_output/flagged_purchases.json
