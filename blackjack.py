"""
black jack is a card game where players try to get as close to 21 points as possible without going over

"""

import sys, random
from logging import getHandlerNames

# set up the constants:
HEARTS = chr(9829)
DIAMONDS = chr(9830)
SPADES = chr(9824)
CLUBS = chr(9827)
BACKSIDE = 'backside'

def main():
    print('''BLACK JACK BY ROY3D
    
    RULES:
        Try to get as close to 21 witout going over.
        Kings. Queens, and Jacks are worth 10 points.
        Aces are worth 1(when you have 2 cards), 11(when you have 3 cards
        Card 2 through 10 are worth their face value.
        (H)it to take another card.
        (S)tand to stop taking cards.
        On your first play, you can (D)ouble down to increase your bet
        but must hit exactly one more time before standing.
        In case of a tie, the bet is returned to the player.
        The dealer stops hitting at 17.''')

    money = 5000
    while True:
        #main game loop
        #check if player has run out of money
        if money <= 0:
            print('You are broke')
            print('Good thing this money is not real')
            print('thanks for playing')
            sys.exit()

        #let the player enter their bet for this round:
        print('Your money: ', money)
        bet = getBet(money)

        #give the dealer and player two cards from the deck each:
        deck = getDeck()
        dealerHand = [deck.pop(), deck.pop()]
        playerHand = [deck.pop(), deck.pop()]

        #Handle player actions:
        print('Bet: ', bet)
        while True:
            #keep looping until player stands or busts.
            displayHands(playerHand, dealerHand, False)
            print()

            #check if the player has bust:
            if getHandValue(playerHand) > 21:
                break

            #Get the player's move, either H, S, or D:
            move = getMove(playerHand, money - bet)

            #handle the player actions:
            if move == 'D':
                #Player is doubling down, tey can increase their bet:
                additionalBet = getBet(min(bet, (money - bet)))
                bet += additionalBet
                print('Bet increased to {}'.format(bet))
                print('Bet: ', bet)

            if move in ('H', 'D'):
                #hit/doubling down takes another card.
                newCard = deck.pop()
                rank, suit = newCard
                print('you drew a {} of {}'. format(rank, suit))
                playerHand.append(newCard)

                if getHandValue(playerHand) > 21:
                    #the player has busted
                    continue
            if move in ('S', 'D'):
                #standing or doubling stops the players turn
                break

        #handle the dealer's actions:
        if getHandValue(playerHand) <= 21:
            while getHandValue(dealerHand) <= 21:
                #the dealer hits:
                print('Dealer hits...')
                dealerHand.append(deck.pop())
                displayHands(playerHand, dealerHand, False)

                if getHandValue(dealerHand) > 21:
                    break #the dealer has busted.
                input('Press Enter to continue...')
                print('\n\n')

        #show the final hands:
        displayHands(playerHand, dealerHand,True)

        playerValue = getHandValue(playerHand)
        dealerValue = getHandValue(dealerHand)
        #Handle whether the player won, lost, or tied:
        if dealerValue > 21:
            print('Dealer busts! You win${}!'.format(bet))
            money += bet
        elif (playerValue > 21) or (playerValue < dealerValue):
            print ('You lost!')
            money -= bet
        elif playerValue > dealerValue:
            print('You won ${}!'.format(bet))
            money += bet
        elif playerValue == dealerValue:
            print('It\'s a draw, the bet is returned to you.')

        input('Press Enter to continue...')
        print('\n\n')

def getBet(maxBet):
    """ask the player how much they want to bet fo this round."""
    while True: #keep asking until they enter a valid amount.
        print('How much do you bet? (1 -{}, or QUIT)'.format(maxBet))
        bet = input('> ').upper().strip()
        if bet == 'QUIT':
            print('Thank you for playing!')
            sys.exit()

        if not bet.isdecimal():
            continue #if the player didn't enter a numer, ask again.

        bet = int(bet)
        if 1 <= bet <= maxBet:
            return bet #player entered a valid bet.

def getDeck():
    """
    :return: a list of (rank, suit) tuples for all 52 cards.
    """
    deck = []
    for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
        for rank in range(2, 11):
            deck.append((str(rank), suit)) #add the numbered cards
        for rank in ('J', 'Q', 'K', 'A'):
            deck.append((rank, suit)) #add the face and ace cards.
    random.shuffle(deck)
    return deck

def displayHands(playerHand, dealerHand, showDealerHand):
    """

    :param playerHand: shows the player's hand
    :param dealerHand: shows the dealer's cards
    :param showDealerHand: hide the dealer's first card if False
    :return:
    """
    print('\n')
    if showDealerHand:
        print('DEALER HAND', getHandValue(dealerHand))
        displayCards(dealerHand)
    else:
        print('DEALER HAND: ???')
        #Hide the dealer's first card:
        displayCards([BACKSIDE] + dealerHand[1:])

    #show the player's cards:
    print('PLAYER:', getHandValue(playerHand))
    displayCards(playerHand)

def getHandValue(cards):
    """

    :param cards:
    :return: the value of the cards. face cards are worth 10, aces are worth 11 or 1 (this function picks the most suitable ace value)
    """
    value = 0
    numberOfAces = 0

    #add the value for the non-ace cards:
    for card in cards:
        rank = card[0] #card is a tuple like (rank, suit)
        if rank == 'A':
            numberOfAces += 1
        elif rank in ('J', 'Q', 'K'):
            value += 10
        else:
            value += int(rank) #numbered cards are worth their number.

    #add the value for aces;
    value += numberOfAces #add 1 per ace
    for i in range(numberOfAces):
        #if another 10 can be added with busting, do so;
        if value + 10 <= 21:
            value += 10
    return value

def displayCards(cards):
    """

    :param cards: display all the cards in the list
    :return:
    """
    rows = ['', '', '', '', ''] #the text to display each row
    for i, card in enumerate(cards):
        rows[0] += '___ ' #print the top line of the card.
        if card == BACKSIDE:
            #print cards back
            rows[1] += '|## |'
            rows[2] += '|###|'
            rows[3] += '|_##|'
        else:
            #print the cards front:
            rank,suit = card #the card is a tuple data structure.
            rows[1] += '|{} | '.format(rank.ljust(2))
            rows[2] += '| {} | '.format(suit)
            rows[3] += '|_{}| '.format(rank.rjust(2, '_'))

    #print each ro on the screen;
    for row in rows:
        print(row)

def getMove(playerHand, money):
    """
    asks the player for their move, and returns 'H' for hit, 'S' for stand and 'D' for double down
    :param playerHand:
    :param money:
    :return:
    """

    while True: #keep looping until the player enters a correct move
        #determine what moves the player can make
        moves = ['(H)it', '(S)tand']

        #the player can double down on their first move, which we can tell
        #because they will have exactly two cards
        if len(playerHand) == 2 and money > 0:
            moves.append('(D)ouble down')

        #Get the player's move:
        movePrompt = ', '.join(moves) + '> '
        move = input(movePrompt).upper()
        if move in ('H', 'S'):
            return move #player has entered a valid move
        if move == 'D' and '(D)ouble down' in moves:
            return move #player has entered a valid move

#if the program is run (istead of imported), run the game;
if __name__ == '__main__':
    main()