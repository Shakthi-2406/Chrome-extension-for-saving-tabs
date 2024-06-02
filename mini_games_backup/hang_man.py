import random
words_bag=["hello","piggy","biscuit","cutie","purple","bottle","halwa","rajini","hockey","donkey","honey","munch","kiss","love","hug","mommy","yellow","health","heart","lung","computer","mouse","exam","kilogram","mango","chocolate","cake","python","game","vegetable","marriage","date","school","books","paper","teacher","bangle"]

question_word = random.choice(words_bag).upper()
letters_yet_to_find = set(question_word)
used_letters = set()
question_display = ""
lives = len(question_word) + 5

for letters in question_word:
    question_display += " _"
print("The word to find is " + question_display)
print(f'You have {lives} lives in this game')


while len(letters_yet_to_find)>0 and lives>0:
    user_guess = input("Guess a letter ").upper()
    if user_guess in used_letters:
        print("already used! u lost one life")
        lives -= 1
        print(f'You have {lives} lives left in this game')
    elif user_guess not in "QWERTYUIOPASDFGHJKLZXCVBNM":
        print("use only one alphabetic. You've lost one life")
        lives -= 1
        print(f'You have {lives} lives left in this game')
    elif len(user_guess)!=1:
        print("use only one letter")
    else:
        used_letters.add(user_guess)
        if user_guess not in question_word:
            lives -= 1
            print(f'You have {lives} lives left in this game')
        else:
            letters_yet_to_find.remove(user_guess)

    print("The used letters:\
        {",' * ' .join(used_letters)+"}" )
    word_progress = [leter if leter in used_letters else '_' for leter in question_word]
    print("Ur progress:\
        ",' ' .join(word_progress)+"\n" )
if lives==0:
    print("Sorry You've lost....:( the word you were supposed to find is \n\t\t"+question_word)
else:
    print("Woohooo You've won :) You found the word \n\t\t"+question_word)




