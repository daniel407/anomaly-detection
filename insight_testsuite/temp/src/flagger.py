# -*- coding: utf-8 -*-

import json
from collections import OrderedDict


class Flagger(object):
    """
    Used to export flagged events into the output file
    """

    def __init__(self, target_path):
        """
        Constructor initializes with path for output file.

        Args:
        target_path (str): path to flagged_purchases.json
        """

        self.target_path = target_path

        # delete any previous output
        f = open(self.target_path, 'w')
        f.close()

    def flag(self, timestamp, amount, user_id, mean, sd):
        """
        opens and closes the outputfile to append a flagged event

        Args:
        timestamp (str) : flagged event detail
        amount (float) : flagged event detail
        user_id (str) : flagged event detail
        mean (float) : flagged event detail
        sd (float) : flagged event detail
        """
        with open(self.target_path, 'a') as outfile:
            data = OrderedDict([('event_type',
                                 'purchase'),
                                ('timestamp',
                                 timestamp),
                                ('id',
                                 user_id),
                                ('amount',
                                 '{0:.2f}'.format(amount)),
                                ('mean',
                                 '{0:.2f}'.format(mean)),
                                ('sd',
                                 '{0:.2f}'.format(sd))])
            json.dump(data, outfile)
            outfile.write('\n')
