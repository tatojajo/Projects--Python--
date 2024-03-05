import random

file_path = 'words.txt'

try:
    with open(file_path, 'r') as file:
        words = file.readlines()
except:
    print('There\'s an issue with the file!')

word_list = [word.strip() for word in words]

chosen_word = random.choice(word_list)

print("Welcome to Hangman!")
print("Try to guess the word.")

word_display = [' _ ' for _ in chosen_word]

guessed_letters = set()


attempts = 8

while attempts > 0 and ' _ ' in word_display:
    print("\n" + ' '.join(word_display))
    print("Attempts left:", attempts)
    
    if guessed_letters:
        print("Incorrect guesses:", ' '.join(sorted(guessed_letters)))
    
    char = input('Enter the letter: ').lower()
    
    if not char.isalpha():
        print("Please enter a valid letter.")
        continue
    
    if char in guessed_letters:
        print("You've already guessed this letter. Try again.")
        continue
    
    
    
    if char in chosen_word:
        for index, letter in enumerate(chosen_word):
            if letter == char:
                word_display[index] = char
    else:
        guessed_letters.add(char)
        attempts-=1
        print(f'You have left {attempts} attempts')
        
        
if ' _ ' not in word_display:
    print('Congratulations! You guessed the word:', chosen_word)
else:
    print("You ran out of attempts. The word was: " + chosen_word)
    print("You lost!")