import random

max_num = 4
max_try = 5

def main():
    while True:
        secretN = secretnum()
        print('I have Thought up a number')
        print(f' You have {max_try} guesses to get it.')

        
        for i in range(1,max_try):
            print(f"Guess #{i}")
            guess = input('>')
            
            if len(guess) != max_num:
                print('please choose correct length')           
            elif guess == secretN:
                print("You got it!")
                break
            else:
                clue = clues(guess, secretN)
                print(clue)
            
        print('Your moves is out')
        print('Do you want to play again? (yes or no')
        if not input('>').lower().startswith('y'):
            break


    print('Thanks to play playing!')     

 

def secretnum():
    number = list('0123456789')
    random.shuffle(number)
    secretN = ''
    
    for i in range(max_num):
        secretN += str(number[i])

    return secretN



def clues(guess, secretN):
    if guess == secretN:
        return 'Wow! You got it'

    clues = []
    for i in range(len(guess)):
        if guess[i] == secretN[i]:
            clues.append('Fermi')
        elif guess[i] in secretN:
            clues.append('Pico')

    if len(clues) == 0:
        return 'Bagels'

    else:
        clues.sort()
        return ' '.join(clues)


if __name__ == "__main__":
    main()