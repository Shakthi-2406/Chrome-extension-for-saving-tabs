import random
words=["hello","piggy","biscuit","cutie","purple","donkey","honey","munch","kiss","love","hug","mommy"]
word = random.choice(words).upper()
# space = " "
word_found=""
for letter in word:
	word_found += "_ " 
# word = space.join(word)
print(word)
i= 5
letter = set(word)
track = set(word)
used_letters = set()
print(word_found)
while i and len(track)>0:
	guess=input("Guess a letter!!! ").upper()
	if guess in used_letters:
		i-=1
		print("Try with a new letter, already used!")
	elif guess not in "ASDFGHJKLMNBVCXZQWERTYUIOP":
		print("Enter only one that too a valid character")	
	elif len(guess) > 1:
		print("Enter only one character")
	elif guess == "":
		print("Blank spaces are not allowed")
	else:
		used_letters.add(guess)
		if guess in word:
			print("This letter is right!")
			track.remove(guess)
			word_list = [leti if leti in used_letters else "_" for leti in word]
			print('Current state: ', ' '.join(word_list))
			# value = word.index(guess)
			# print(value)
			# word_found = word_found[:value] + guess + word_found[value:]
			# value1 = word.rfind(guess)
			# word_found = word_found[:value1] + guess + word_found[value1:]
			# word_found = guess for letter in word and 
			print (word_found)
		else:
				i -= 1
	print('Your used letters are: ', ' '.join(used_letters))
print (used_letters)
