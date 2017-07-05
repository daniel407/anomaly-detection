# -*- coding: utf-8 -*-

import operator
from user import User


class Universe(object):
    """
    This class is the registry for all users in the
    social network.

    It manages the actions of adding and removing
    friendships,
    purchases and flagging. Certain actions trigger
    and update of the individual users' network.
    """

    def __init__(self, T, D, flagger=None):
        """
        Constructor sets core parameters, initiates
        user dictionary and flagger object.

        Args:
        T (int) : time parameter retrospective
        sampling

        D (int) : depth (degree) of users' social
        net considered

        flagger (Flagger) : object which handles
        output of flagging of purchase events
        """
        self.T = T
        self.D = D
        self.users = {}
        self.flagger = flagger

    def create_user(self, user_id):
        """
        creates a user with id in the dictionary

        Args:
        user_id (str) : the user's unique identifier
        """
        self.users[user_id] = User()

    def add_friendship(self, user_id_1, user_id_2):
        """
        Registers a friendship between two users and
        subsequently triggers the update of the
        surrounding network.

        Args:
        user_id_1 (str) : involved user
        user_id_2 (str) : involved user

        Function is symmetric to input order.
        """
        self.users[user_id_1].friends.append(user_id_2)
        self.users[user_id_2].friends.append(user_id_1)
        self.update_networks(user_id_1, user_id_2)

    def remove_friendship(self, user_id_1, user_id_2):
        """
        De-registers a friendship between two users and
        subsequently triggers the update of the
        surrounding network.

        Args:
        user_id_1 (str) : involved user
        user_id_2 (str) : involved user

        Function is symmetric to input order.
        """
        self.users[user_id_1].friends.remove(user_id_2)
        self.users[user_id_2].friends.remove(user_id_1)
        self.update_networks(user_id_1, user_id_2)

    def update_networks(self, user_id_1, user_id_2):
        """
        A friending or unfriending event requires a
        remapping of the involved users networks.
        A list of unique members which have been in
        the defined networks of both users is created and
        each member's network is updated. Afterwards
        the network purchases are reestablished.

        Args:
        user_id_1 (str) : involved user
        user_id_2 (str) : involved user

        Function is symmetric to input order.
        """
        networks_to_update = [user_id_1, user_id_2]
        networks_to_update += self.users[user_id_1].network
        networks_to_update += self.users[user_id_2].network
        networks_to_update = list(set(networks_to_update))
        for member_id in networks_to_update:
            self.users[member_id].network = self.determine_network(
                member_id, avoid=[], level=1)
            self.update_network_purchases(member_id)

    def determine_network(self, user_id, avoid=[], level=1):
        """
        This method is used to recursively determine_network
        the network of degree D of a user.

        Args:

        user_id (str) : user's unique identifier

        avoid [] : list of user_id's which will not be visited,
        such as nodes that have been processed already.

        level : degree of depth in the recursion. Is used to
        trigger break when D is reached.

        Returns:
        list : network of degeree D of the user
        """
        if user_id not in avoid:
            avoid.append(user_id)
        user = self.users[user_id]
        nodes = user.friends[:]
        for node in nodes:
            if node in avoid:
                nodes.remove(node)
        avoid += nodes
        if level == self.D:
            return nodes
        else:
            level += 1
            nw = nodes[:]
            for friend in nodes:
                nw += self.determine_network(friend, avoid=avoid,
                                             level=level)
            return nw

    def update_network_purchases(self, user_id):
        """
        Re-assesses the user's network_purchases, typically after
        a friendship change event.
        Afterwards triggers to update the mean, sd, and threshold
        for flagging accordingly.

        Args:
        user_id (str) : user's unique identifier
        """

        user = self.users[user_id]
        np = []

        # the purchases of each member in the network are collected
        # and then sorted by chronological order
        for member_id in user.network:
            member = self.users[member_id]
            np += member.purchases
        user.network_purchases = sorted(
            np, key=operator.itemgetter(0), reverse=False)

        # the most recent T purchases are kept
        while len(user.network_purchases) > self.T:
            user.network_purchases.pop(0)

        # threshold update after network update
        user.update_threshold()

    def add_purchase(self, user_id, timestamp, amount):
        """
        Tests if a user's purchase surpasses the threshold and if
        positive, flags the event.
        Updates the user's purchase history and the network_purchases
        list of every member of the network.

        Args:
        user_id (str): user's unique identifier
        timestamp (str): timestamp of purchase
        amount (float): amount of purchase
        """
        user = self.users[user_id]

        # test if the purchase surpasses the flagging threshold
        if self.flagger is not None:
            if len(user.network_purchases) >= 2 and amount > user.threshold:
                self.flagger.flag(
                    timestamp=timestamp,
                    amount=amount,
                    user_id=user_id,
                    mean=user.mean,
                    sd=user.sd)

        # adding the purchase in the User and limiting the list to T
        user.purchases.append((timestamp, amount))
        if len(user.purchases) > self.T:
            user.purchases.pop(0)

        # adding the purchase to the user's network's network_purchases
        for member_id in user.network:
            member = self.users[member_id]
            member.network_purchases.append((timestamp, amount))
            if len(member.network_purchases) > self.T:
                member.network_purchases.pop(0)
            member.update_threshold()
