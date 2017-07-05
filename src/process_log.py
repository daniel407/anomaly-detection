# -*- coding: utf-8 -*-

import sys
import json
import datetime

from universe import Universe
from flagger import Flagger
from process import read_batch_log, read_stream_log

# reading the file paths from the arguments
batch_log_path = sys.argv[1]
stream_log_path = sys.argv[2]
flagged_purchases_path = sys.argv[3]

# parsing through the batch_log line by line
universe = read_batch_log(batch_log_path)

# parsing through the stream_log line by line
read_stream_log(stream_log_path, universe, flagged_purchases_path)
