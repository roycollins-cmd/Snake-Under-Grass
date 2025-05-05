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

        #get a random day into the year:
        randomNumberOfDays = datetime.timedelta(random.randint(0, 364))
        birthday = startOfYear + randomNumberOfDays
        birthdays.append(birthday)
    return birthdays

def getMatch(birthdays):
    """
    :param birthdays:
    :return: the date object of a birthday that occurs more than once in the birthday list
    """
    #compare each birthday to every other birthday:
    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays):
            if birthdayA == birthdayB:
                return birthdayA #returns the matching birthday for real

#Display the intro
print('''Birthday Paradox, engineered by Al Sweigart. Practice by roy Kucherera

this program shows us that in a given group of N people, the odds that 2 of them
have matching birthdays is surprisingly large. This Program does a Monte Carlo simulation (that is, repeated random simulations)
to explore this concept
It's not actually a paradox, it's just a surprising result''')

#setting up a tuple of month names in order
MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

while True: #keep asking until the user enters a valid amount.
    print('How many birthdays shall I generate? (Max is 100)')
    response = input('> ')

    if response.isdecimal() and (0 < int(response) <= 100):
        numBDays = int(response)
        break #user has a valid amount
    print()

#generate and display the birthdays
print('Here are', numBDays, 'birthdays')
birthdays = getBirthdays(numBDays)
for i, birthday in enumerate(birthdays):
    if i != 0:
        #display a comma for each birthday after the first birthday.
        print(',', end='')
        monthName = MONTHS[birthday.month - 1]
        dateText = '{} {}'.format(monthName, birthday)
        print(dateText, end='')
    print()
    print()

#Determine if there are two birthdays that match
match = getMatch(birthdays)

#Display the results:
print('in this simulation,', end='')
if match != None:
    monthName = MONTHS[match.month - 1]
    dateText = '{} {}'.format(monthName, match.day)
    print('multiple people have a birthday on', dateText)
else:
    print('there are no matching birthdays')
print()

#run through 100,000 simulations
print('Generating', numBDays, 'random birthdays 100,000 times (one hundred thousand times)...')
input('Press Enter to continue...')
print()

print('Let\'s run another 100,000 simulations.')
simMatch = 0 #How many simulations had matching birthdays
for i in range(100_000):
    # report on the progress every 10,000 simulations
    if i % 10_000 == 0:
        print(i, 'simulations done...')
    birthdays = getBirthdays(numBDays)
    if getMatch(birthdays) != None:
        simMatch += 1
print('100,000 simulations done.')

#Display the simulation results
probability = round(simMatch / 100_000 * 100, 2)
print('Out of 100,000 simulations of', numBDays, 'people, there was a')
print('matching birthday in that group', simMatch, 'times. This means')
print('that', numBDays, 'people have a', probability, '% chance of')
print('having a matching birthday in that group')
print('That\'s probably more than you would think!')

        