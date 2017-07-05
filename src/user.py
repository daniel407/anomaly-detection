# -*- coding: utf-8 -*-

from statistics import mean, pstdev


class User(object):

    """
    Class to store user related data such as friends, 
    network, purchases and threshold
    """

    def __init__(self):
        """
        Constructor initiates blank user template.

        Fields:

        friends: maintains a list of user_ids which are 
        direct (degree 1) friends

        purchases:
        maintains a list of purchases made by 
        the user. The list is kept at length T

        network_purchases:
        maintains a list of purchases made within the 
        user's network

        network:
        maintains a list of user_ids which are in the 
        user's network

        mean:
        mean of network_purchases

        sd:
        standard deviation of network_purchases

        threshold:
        the upper limit above which a flagging 
        will be triggered
        """
        self.friends = []
        self.purchases = []
        self.network_purchases = []
        self.network = []
        self.mean = 0.0
        self.sd = 0.0
        self.threshold = 0.0

    def update_threshold(self):
        """
        udpates the metrics used to detect anomalies

        threshold = mean + 3*sd
        """
        if len(self.network_purchases) > 0:
            np = []
            for network_purchase in self.network_purchases:
                np.append(network_purchase[1])
            self.mean = mean(np)
            self.sd = pstdev(np)
            self.threshold = self.mean + 3 * self.sd
        else:
            self.mean = 0.0
            self.sd = 0.0
            self.threshold = 0.0
