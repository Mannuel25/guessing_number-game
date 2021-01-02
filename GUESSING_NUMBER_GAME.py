import random

def guessingNumberGame():
	print('Welcome Player!')
	play_game = input(f'Do you wish to play?(yes/no): ')
	number_of_guesses = 0
	while play_game == 'yes' or play_game == 'YES':
		print('\nGreat..let\'s get started!')
		number = int(input('Guess a number between 1 and 100: '))
		if number <= 100:
			number_of_guesses += 1
			randomNumber = random.randint(1,100)
			if number > randomNumber:
				print('Too high :( ..try again')
				play_game = input('\nGuess again?(yes/no): ')
			elif number < randomNumber:
				print('Too low :( ..try again')
				play_game = input('\nGuess again?(yes/no): ')
			else:
				print('Congratulations {}, you guessed right!!..[Number of guesses: {}]'.format(name,number_of_guesses))
				play_game = input('\nDo you wish to play again?(yes/no): ')
		else:
			print('Out of range..guess a number between 1 and 100')
			play_game = input('\nGuess again?(yes/no): ')

guessingNumberGame()
