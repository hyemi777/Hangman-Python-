import random 
import string
from words import words
from lives import lives_visual_dict

def getValidWord(words):
  word = random.choice(words)
  while '-' in word or ' ' in word:
    word = random.choice(words)
  return word.upper()


def hangman():
  word = getValidWord(words)
  wordLetters = set(word) #letters in the word
  alphabet = set(string.ascii_uppercase)
  usedLetters = set() #tracking what the user has already guessed
  lives = 6
  
  while len(wordLetters) > 0 and lives > 0:
    #letters used
   
    print('You have ', lives, ' lives left. You have used these letters ', ' '.join(usedLetters))
    
    print(lives_visual_dict[lives])
    wordList = [letter if letter in usedLetters else '-' for letter in word]
    print('Current word: ', ' '.join(wordList))

    userInput = input('Guess a letter: ').upper() 
    print('\n')
    if userInput in alphabet - usedLetters:
      usedLetters.add(userInput)
      if userInput in wordLetters:
        wordLetters.remove(userInput)
      else: 
        print('Your letter is not in the word. Try again.')
        lives -= 1
    elif userInput in usedLetters:
      print('You have already used that letter.')

    else:
      print('You did not type a valid character.')

  #gets here when len(wordLetters) == 0 OR lives == 0
  if lives == 0:
    print('Sorry, you died. The word was ', word)
  else:
    print('Yay! You guessed the word ', word, '!!')


if __name__ == '__main__':
    hangman()