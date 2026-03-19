from app import Game

game = Game()
while True:
    user_guess = input("Guess a number: ")
    if user_guess == "x":
        break
    if user_guess == "s":
        print(game.hidden)
        continue
    user_guess = int(user_guess)
    response = game.guess(user_guess)
    if response == 'match':
        print("matched")
        break
    print(response)
