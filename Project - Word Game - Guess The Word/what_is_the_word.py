import random

word_book = ['Python', 'Programming', 'Fun', 'Love', 'Bangladesh', 
             'Father', 'Mother','Sister','Brother','Family','Data',
             'Language','Development','Robot', 'Dhaka', 'Algorithm'
             ]


# chooses a random word from the word_book
def choose_random_word():
    length_of_word_book = len(word_book)
    random_number = random.randint(0,length_of_word_book-1)
    unknown_word_from_word_book = word_book[random_number]

    return unknown_word_from_word_book

# shuffles the word
def elomelo(word):
    to_be_shuffled = list(word)
    # print(to_be_shuffled)
    random.shuffle(to_be_shuffled)
    shuffled = ' '.join(to_be_shuffled)
    
    return shuffled

# checks if the word is correct
def check_answer(answer, word):
    if answer.upper() == word.upper():
        print('\tCORRECT ANSWER')
        return True
    elif answer.upper() == 'EXIT':
        return False
    else:
        print('\tWRONG ANSWER')
        return False



if __name__ == '__main__':

  
    score = 0
    start = True


    # loop keeps running until the user guesses the word wrong
    while True:
        word = choose_random_word()
        shuffled_word = elomelo(word)

        print(f'Guess The Correct Word: {shuffled_word.lower()}')
        answer = input("Enter your answer: ")

        # checks if the answer is correct; if correct then the score increases by 1
        if check_answer(answer, word):
            score += 1
            print(f'*********** SCORE: {score} *********** \n')
            continue
        else:
            print('*********** GAME OVER ***********')
            print(f'*********** FINAL SCORE: {score} ***********')
            break
