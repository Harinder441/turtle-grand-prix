from turtle import Turtle, Screen
import random
#Improvements
## use function for winning
## play again option
## set starting postion function
## add difficulty level(no.)




# turtles
# color set
# get choice from user
# start on click
#win decision
track= Screen()

turtles=[]
for i in range(5):
    turtles.append(Turtle(shape="turtle",))
x= track.window_width()
y= track.window_height()
color_list=["blue","red","yellow","black","green"]
play = "yes"
while play=="yes":
    for i in range(5):
        turtles[i].penup()
        turtles[i].fillcolor(color_list[i])
        turtles[i].speed(6)
        turtles[i].setposition((-x/2+20,y/2-60- i*(y/6)))
    user_bet=track.textinput(title="Make your Bet", prompt="which turtle will win the race")


    cont=True
    while(cont):
        for turtle in turtles:
            turtle.forward(random.randint(0,10))
            if turtle.pos()[0] >= x/2-20:
                if user_bet==turtle.fillcolor():
                    print("you win")
                else:
                    print("you loss")
                cont= False
                print(f"{turtle.fillcolor()} is winner")

                play=track.textinput(title="Play again", prompt="Enter yes or no")
                print(play)


track.exitonclick()
