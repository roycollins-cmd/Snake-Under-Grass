"""
Monte Carlo type experiment to determine the probability that 2 people in a group, no matter how small, can have the same birthday
Monte Carlo Experiments: Experiments in which we conduct random trails to understand the likely outcomes
by Al Sweigart
"""

import random, datetime

def getBirthdays(numberOfBirthdays):
    """

    :param numberOfBirthdays:
    :return: a list of number random date objects for birthdays.
    """
    birthdays = []
    for i in range(numberOfBirthdays):
        startOfYear = datetime.date(2001, 1, 1)

        