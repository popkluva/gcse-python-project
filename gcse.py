from gcse_data import *
import random
import sys

name = input("Enter your name: ")
school = input("Enter your school: ")
if school != "Example":
    sys.exit("Not from correct school or it is not capitalised correctly")

song1 = random.choice(song_list)
song1_index = song_list.index(song1)
artist1 = artist_list[song1_index]
word = song1

print(song1[0])
print(artist1)

while guess != word and not out:
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out = True
if out:
    sys.exit("Out of guesses, game ended")
else:
    print("Correct")
if guess_count == 1:
    score += 3
else:
    score += 1
guess_count = 0

song_list.remove(song1)
artist_list.remove(artist1)
song2 = random.choice(song_list)
song2_index = song_list.index(song2)
artist2 = artist_list[song2_index]
word = song2

print(song2[0])
print(artist2)

while guess != word and not out:
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out = True
if out:
    sys.exit("Out of guesses, game ended")
else:
    print("Correct")
if guess_count == 1:
    score += 3
else:
    score += 1
guess_count = 0

song_list.remove(song2)
artist_list.remove(artist2)
song3 = random.choice(song_list)
song3_index = song_list.index(song3)
artist3 = artist_list[song3_index]
word = song3

print(song3[0])
print(artist3)

while guess != word and not out:
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out = True
if out:
    sys.exit("Out of guesses, game ended")
else:
    print("Correct")
if guess_count == 1:
    score += 3
else:
    score += 1
guess_count = 0

song_list.remove(song3)
artist_list.remove(artist3)
song4 = random.choice(song_list)
song4_index = song_list.index(song4)
artist4 = artist_list[song4_index]
word = song4

print(song4[0])
print(artist4)

while guess != word and not out:
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out = True
if out:
    sys.exit("Out of guesses, game ended")
else:
    print("Correct")
if guess_count == 1:
    score += 3
else:
    score += 1
guess_count = 0

song_list.remove(song4)
artist_list.remove(artist4)
song5 = random.choice(song_list)
song5_index = song_list.index(song5)
artist5 = artist_list[song5_index]
word = song5

print(song5[0])
print(artist5)

while guess != word and not out:
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out = True
if out:
    sys.exit("Out of guesses, game ended")
else:
    print("Correct")
if guess_count == 1:
    score += 3
else:
    score += 1
guess_count = 0

print("Congratulations " + name + ", you beat the game with " + str(score) + " points!")
data = open("gcse_data.py", "a")
data.write("\n" + name + " = " + str(score))
data.close()
