words_txt = []
guess = ''
colors = ''


#Locates our text file of words  and prints error if missing.
try:
    with open("words.txt") as f:
        for line in f:
            words_txt.append(line.strip())
except FileNotFoundError:
    print('\033[91m' + '\033[1m' + 'ERROR: File not found!!!' + '\033[0m')

print(
    '\033[1m' + '\nWelcome to Wordle Buddy! ' + '\033[0m' + '\U0001F604' + '\nI suggest starting your game with one of these three words:' + '\033[0m' + '\033[1m'  + ' adept, clamp, plaid' + '\033[0m')

#Enter your guess, if over 5 letters loops. Enter colors, if over 5 letters loops.
for guesses in range(6):
    guess = input('\033[1m'  + '\nEnter Guess: ' + '\033[0m').lower()
    if len(guess) > 5:
        guess = input('\033[1m' + 'Please try again. Remember your input must be only 5 letters in length: ' + '\033[0m'.lower())

    print('\033[92m' + '\nG = Green, ' + '\033[0m' + '\033[93m' + 'Y = Yellow, ' + '\033[0m' + 'X = Incorrect/Grey')

    colors = input('\033[1m' + 'Enter color of each letter' + '\033[0m' + ' (example: ggggg): ').lower()

    if len(colors) > 5:
        colors = input('\033[1m' + 'Please try again. Remember your input must be only 5 letters in length: ' + '\033[0m'.lower())

    if colors == 'ggggg':
        print('\033[1m' + '\nGreat Job! See you tomorrow! ' + '\033[0m' + '\U0001F973' + '\033[1m' + '\nNumber of Guesses:',guesses + 1)
        break

#Goes through our text file and removes words that are poor matches.
    temp = tuple(words_txt)
    for word in temp:
        for i in range(5):
            if colors[i] == "x" and guess[i] in word:
                words_txt.remove(word)
                break
            elif colors[i] == "g" and guess[i] != word[i]:
                words_txt.remove(word)
                break
            elif colors[i] == "y" and guess[i] not in word:
                words_txt.remove(word)
                break
            elif colors[i] == "y" and guess[i] == word[i]:
                words_txt.remove(word)
                break

#Prints us a list of words from our text file after being edited
    counter = 0
    print('\033[1m' + '\nHmmmmm! Maybe try one of these words next: ' + '\033[0m' + '\U0001F914')
    for word in words_txt:
        print(word, end=", ")
        counter += 1
        if counter == 10:
            print("")
            counter = 0
    print('')
