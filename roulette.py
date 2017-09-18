"""Build a working roulette game.  At minimum, this script should
Complete one round of roulette - but if you're up to the challenge,
feel free to build a full command line interface through which
"""

import random

bank_account = 1000
bet_amount = 0
bet_color = None
bet_number = None
number_rolled = 0
color_rolled = ""

green = [0, 37]
red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
black = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]


def take_bet(account):
    if account <= 0:
        print("Sorry, you've lost all of your money.")
        return(-1)

    choice = input("\nWhat would you like to bet on, a color or number?: ")
    amount = input("How much money would you like to bet (keep in mind you have $%i in your account): " % (account))
    bet_amount = int(amount)

    if account < bet_amount:
        print("Sorry, but you can't bet more than what you have; which is %i. Bet a smaller amount" % (account))

    if choice == "color":
        color = input("What color would you like to bet on -> green, red or black: ")
        bet_color = color
        are_you_sure = input("Are you sure you want to bet $%i on %s?: " % (bet_amount, bet_color))
        if are_you_sure == "yes":
            return(bet_amount, bet_color)
        else:
            return(None)

    elif choice == "number":
        number = input("Pick a number between 0 and 37 that you would like to bet on: ")
        bet_number = int(number)
        are_you_sure = input("Are you sure you want to bet $%i on %i?:" % (bet_amount, bet_number))
        if are_you_sure == "yes":
            return(bet_amount, bet_number)
        else:
            return(None)


def roll_ball():
    """Return a random number between 0 and 37."""
    number_rolled = random.randint(0, 37)
    if green.count(number_rolled) > 0:
        color_rolled = "green"
    elif red.count(number_rolled) > 0:
        color_rolled = "red"
    elif black.count(number_rolled) > 0:
        color_rolled = "black"

    print("\nNumber: %i - Color: %s" % (number_rolled, color_rolled))
    return(number_rolled, color_rolled)


def check_results(bet_tup, res_tup):
    """
    Compare bet_color to color rolled.
    Compares bet_number to number_rolled.
    """
    colors = ["red", "green", "black"]
    if colors.count(bet_tup[1]) > 0:
        if bet_tup[1] == res_tup[1]:
            print("You've guessed the right color!\n")
            return(1)
        else:
            print("Sorry, but you didn't win this round.\n")
            return(-1)

    elif bet_tup[1]:
        if bet_tup[1] == res_tup[0]:
            print("I don't know if it's luck or not but you've guessed the right number!\n")
            return(2)
        else:
            print("Sorry, but you didn't win this round.\n")
            return(-2)


def payout(number, tup, account):
    """Return total amount won or lost by user based on results of roll."""
    local_account = account
    if number == 1:
        print("You're payout is $%i" % (tup[0]/2))
        local_account = local_account + (tup[0] / 2)
        print("You now have $%i in your account." % (local_account))
    elif number == -1:
        print("You've lost $%i" % (tup[0]/2))
        local_account = local_account - (tup[0] / 2)
        print("You now have $%i in your account." % (local_account))
    elif number == -2:
        print("You've lost $%i" % (tup[0] * 2))
        local_account = local_account - (tup[0] * 2)
        print("You now have $%i in your account." % (local_account))
    elif number == 2:
        print("You're payout is $%i" % (tup[0] * 2))
        local_account = local_account + (tup[0] * 2)
        print("You now have $%i in your account." % (local_account))

    return local_account


if __name__ == '__main__':
    """Initiate roulette game."""
    def roulette(account):
        placed_bet = take_bet(account)
        if placed_bet is None:
            roulette(account)
        elif placed_bet == -1:
            print("Go get some cash then come back!")
            return

        roll_results = roll_ball()
        newaccount = payout(check_results(placed_bet, roll_results), placed_bet, account)

        contin = input("\nWould you like to keep [p]laying or [c]ash out? (enter 'p' or 'c'): ")
        if contin == "p":
            roulette(newaccount)
        else:
            print("Thanks for playing, hope you enjoyed the game!")

    roulette(bank_account)
