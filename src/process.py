# -*- coding: utf-8 -*-

import json

from universe import Universe
from flagger import Flagger


def read_batch_log(batch_log_path):
    """
    Reads the batch_log file and builds the initial 
    state
    of the social network. Also reads the parameters 
    D and T from the batch_log file.

    Args:
    batch_log_path (str) : path to the batch_log file

    Returns:
    universe (Universe) : object containing the state 
    of the social network after reading in the 
    batch_log
    """

    universe = None
    with open(batch_log_path, 'r') as f:

        # extract T and D parameters
        dt = json.loads(f.readline())
        D = int(dt['D'])
        T = int(dt['T'])

        # defining the 'universe' which represent the 
        # total network
        universe = Universe(T=T, D=D, flagger=None)

        for line in f:

            data = json.loads(line)

            if data['event_type'] == 'purchase':
                user_id = data['id']
                if user_id not in universe.users:
                    universe.create_user(user_id)
                universe.add_purchase(
                    user_id, data['timestamp'], float(
                        data['amount']))

            if data['event_type'] == 'befriend':
                id1 = data['id1']
                id2 = data['id2']
                if id1 not in universe.users:
                    universe.create_user(id1)
                if id2 not in universe.users:
                    universe.create_user(id2)
                universe.add_friendship(id1, id2)

            if data['event_type'] == 'unfriend':
                id1 = data['id1']
                id2 = data['id2']
                if id1 not in universe.users:
                    universe.create_user(id1)
                if id2 not in universe.users:
                    universe.create_user(id2)
                universe.remove_friendship(id1, id2)

    return universe


def read_stream_log(stream_log_path, universe, 
                    flagged_purchases_path):
    """
    Reads the stream_log file and flags events accordingly

    Args:
    stream_log_path (str) : path to the stream_log file
    universe (Universe) : Universe object representing 
    the state of the social network
    flagged_purchases_path : path to the output file
    """

    # set up flagger object with output path
    flagger = Flagger(flagged_purchases_path)

    # set the flagger
    universe.flagger = flagger

    with open(stream_log_path, 'r') as f:
        for line in f:

            data = json.loads(line)

            if data['event_type'] == 'purchase':
                user_id = data['id']
                if user_id not in universe.users:
                    universe.create_user(user_id)
                universe.add_purchase(
                    user_id, data['timestamp'], float(
                        data['amount']))

            if data['event_type'] == 'befriend':
                id1 = data['id1']
                id2 = data['id2']
                if id1 not in universe.users:
                    universe.create_user(id1)
                if id2 not in universe.users:
                    universe.create_user(id2)
                universe.add_friendship(id1, id2)

            if data['event_type'] == 'unfriend':
                id1 = data['id1']
                id2 = data['id2']
                if id1 not in universe.users:
                    universe.create_user(id1)
                if id2 not in universe.users:
                    universe.create_user(id2)
                universe.remove_friendship(id1, id2)
