import random

def guessingNumberGame():
	print('Welcome Player!')
	PICKS = ['YES','Yes','NO','No']
	play_game = input(f'Do you wish to play?(yes/no): ')
	if play_game.title() not in PICKS:
		print('Invalid input!')
	else:	
		number_of_guesses = 0
		while play_game == 'yes' or play_game == 'YES':
			try:
				number = int(input('Guess a number in the range of 1 through 50: '))
			except ValueError:
				print('Invalid input!')
			else:	
				if 1 <= number <= 50:
					number_of_guesses += 1
					randomNumber = random.randint(1,50)
					if number > randomNumber:
						print('Too high 😝 ...try again')
						play_game = input('\nGuess again?(yes/no): ')
					elif number < randomNumber:
						print('Too low 😔 ...try again')
						play_game = input('\nGuess again?(yes/no): ')
					else:
						print('Congratulations!! 🎈🎉...you guessed right after {} trials'.format(number_of_guesses))
						play_game = input('\nDo you wish to play again?(yes/no): ')
				else:
					print('Out of range!..guess a number in the range of 1 through 50')
					play_game = input('\nGuess again?(yes/no): ')
					if play_game.title() not in PICKS:
						print('Invalid input!')
					else:
						continue	

guessingNumberGame()
			
