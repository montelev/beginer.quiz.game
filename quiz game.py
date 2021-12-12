echo "# beginer.quiz.game" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/montelev/beginer.quiz.game.git
git push -u origin main


print("Welcome to my anime quiz!")

playing = input("Do you want to play? ")

if playing.lower()  != "yes":
    quit()

print("Okay! Let's play :)")
score = 0
answer = input("What anime does Sasuke belong to? ")
if answer.lower() == "naruto":
    print("correct!")
    score += 1
else:
    print("Incorrect!! ")

answer = input("In naruto who's Team 7 sensei? ")
if answer.lower() == "kakashi":
    print("correct!")
    score += 1
else:
    print("Incorrect!! ")

answer = input("In demon slayer, whos' sword is black? ")
if answer.lower() == "tanjiro":
    print("correct!")
    score += 1
else:
    print("Incorrect!! ")

answer = input("The mark on Tanjiros' face is on his left or right? ")
if answer.lower() == "left":
    print("correct!")
    score += 1
else:
    print("Incorrect!! ")

answer = input("How many stars did gokus dragonball(80's) have ")
if answer.lower() == "four":
    print("correct!")
    score += 1
else:
    print("Incorrect!! ")

print("you got " + str(score) + " Questions correct! ")
print("you got " + str((score/5) * 100) + "%.")