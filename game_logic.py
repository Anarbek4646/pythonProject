import random
from decouple import config
from casino import Casino

class GameLogic:
    def __init__(self):
        self.my_money = int(config('MY_MONEY'))
        self.slot_numbers = list(range(1, 31))

    def make_bet(self):
        while True:
            try:
                bet = int(input(f"You have ${self.my_money}. Enter your bet: "))
                if bet > self.my_money:
                    print("You don't have enough money. Try again.")
                else:
                    return bet
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def choose_slot(self):
        while True:
            try:
                slot = int(input('Сhoose a winning slot from 1-30: '))
                return slot
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def play_game(self):
        casino = Casino(self.slot_numbers)
        while True:

            bet = self.make_bet()
            win_slot = casino.play()
            if win_slot != self.choose_slot():
                print(f"You lost! win slot-{win_slot} "
                      f"Try again.")
                self.my_money -= bet
            else:
                print(f"Congratulations! You won! You guessed the winning slot ({win_slot})!")
                self.my_money += bet
            print(f"Your current balance: ${self.my_money}")

            play_again = input("Do you want to play again? (y/n): ")
            if play_again.lower() != 'y':
                print("Thanks for playing. Final balance:", self.my_money)
                break

if __name__ == '__main__':
    game_logic = GameLogic()
    game_logic.play_game()