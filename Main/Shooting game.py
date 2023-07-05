import turtle
import random

# Initialize the game window
window = turtle.Screen()
window.title("Archery Game")
window.bgcolor("gray")
window.setup(width=800, height=600)

# Create the archer
archer = turtle.Turtle()
archer.speed(0)
archer.shape("triangle")
archer.shapesize(1.3,1.3)
archer.penup()
archer.left(45)
archer.goto(-375, -270)
archer.pendown()

# Create the line of the archer
line = turtle.Turtle()
line.speed(0)
line.penup()
line.left(45)
line.goto(-405,-300)
line.pendown()
line.pensize(5)
line.forward(50)
line.stamp()

# Create the bullet of the archer
bullet = turtle.Turtle()
bullet.speed(0)
bullet.color("red")
bullet.shape("circle")
bullet.shapesize(1)
bullet.penup()
bullet.left(45)
bullet.goto(-355,-250)
bullet.pendown()

# Set up the player names and scores
player1_name = window.textinput("Player 1", "Enter Player 1's name:")
player2_name = window.textinput("Player 2", "Enter Player 2's name:")
score_limit = int(window.textinput("Score Limit","Enter the score limit:"))
# Who is turn
number = [1,2]
a = random.choice(number)
if a == 1:
    game_turn = player1_name
else:
    game_turn = player2_name    
game_speed = int(window.textinput("Game Speed", "Enter the game speed:"))
speed = game_speed
player1_score = 0
player2_score = 0

# show and update the board
def board(player1_name,player2_name,player1_score,player2_score,game_turn,game_speed):
    turtle.clear()
    turtle.penup()
    turtle.speed(5)
    turtle.color("skyblue")
    turtle.goto(-390, 275)
    turtle.write(player1_name + ": " + str(player1_score), align="left", font=("Arial", 14, "normal"))
    turtle.color("orange")
    turtle.goto(-390, 245)
    turtle.write(player2_name + ": " + str(player2_score), align="left", font=("Arial", 14, "normal"))
    turtle.goto(-390, 215)
    turtle.color("green")
    turtle.write("game_turn : " + game_turn, align="left", font=("Arial", 14, "normal"))
    turtle.goto(-390, 185)
    turtle.write("game_speed : " + str(game_speed) + "x", align="left", font=("Arial", 14, "normal"))
    turtle.color("black")
    turtle.hideturtle()


board(player1_name,player2_name,player1_score,player2_score,game_turn,game_speed)

# create Ball Player1
b1 = turtle.Turtle()
b1.penup()
b1.speed(game_speed)
b1.color("skyblue")
b1.shape("circle")
b1.shapesize(5)
random_x1 = random.randint(-350,350)
b1.goto(random_x1,50)

# create Ball Player2
b2 = turtle.Turtle()
b2.penup()
b2.speed(game_speed)
b2.color("orange")
b2.shape("circle")
b2.shapesize(5)
random_x2 = random.randint(-350,350)
b2.goto(random_x2,-50)

# Set up the key bindings
def move_up():
    archer.left(5)
    x1 = bullet.xcor()
    y1 = bullet.ycor()
    bullet.clear()
    bullet.hideturtle()
    bullet.speed(5)
    bullet.penup()
    bullet.goto(x1 - 0.75, y1 + 1.5)         
    bullet.pendown()
    bullet.showturtle()
    bullet.stamp()
    
        
def move_down():
    archer.left(-5)
    x1 = bullet.xcor()
    y1 = bullet.ycor()
    bullet.clear()
    bullet.hideturtle()
    bullet.speed(5)
    bullet.penup()
    bullet.goto(x1 + 0.75, y1 - 1.5) 
    bullet.pendown()
    bullet.showturtle()
    bullet.stamp()
    
def shoot():
    global player1_name, player2_name, player1_score, player2_score, game_turn, bullet, b1, b2      

    check = True
    while check == True:
        x1 = bullet.xcor()
        y1 = bullet.ycor()
        if check == True:
            x1 += 10
            y1 += 5
        bullet.clear()    
        bullet.speed(10)   
        bullet.setx(x1)
        bullet.sety(y1)
        if x1 > 350 or y1 > 250:
            check = False
            bullet.clear()
            bullet.hideturtle()
            bullet.penup()
            bullet.goto(-355,-250)
            bullet.pendown()
        bx2 = b2.xcor()
        by2 = b2.ycor()
        bx1 = b1.xcor()
        by1 = b1.ycor()    
        if game_turn == player1_name:
            if (x1 + 45 > bx2 and x1 - 45 < bx2 and y1 + 45 > by2 and y1 - 45 < by2):
                player1_score += 5
                board(player1_name,player2_name,player1_score,player2_score,game_turn,game_speed)     
                bullet.clear()
                bullet.hideturtle()
                check = False
                bullet.penup()
                bullet.goto(-355,-250)
                bullet.pendown()
            elif (x1 + 45 > bx1 and x1 - 45 < bx1 and y1 + 45 > by1 and y1 - 45 < by1):
                player1_score -= 3    
                board(player1_name,player2_name,player1_score,player2_score,game_turn,game_speed)     
                bullet.clear()
                bullet.hideturtle()
                check = False
                bullet.penup()
                bullet.goto(-355,-250)
                bullet.pendown()
        elif game_turn == player2_name:
            if (x1 + 45 > bx1 and x1 - 45 < bx1 and y1 + 45 > by1 and y1 - 45 < by1):
                player2_score += 5
                board(player1_name,player2_name,player1_score,player2_score,game_turn,game_speed)     
                bullet.clear()
                bullet.hideturtle()
                check = False
                bullet.penup()
                bullet.goto(-355,-250)
                bullet.pendown()
            elif (x1 + 45 > bx2 and x1 - 45 < bx2 and y1 + 45 > by2 and y1 - 45 < by2):
                player2_score -= 3       
                board(player1_name,player2_name,player1_score,player2_score,game_turn,game_speed)             
                bullet.clear()
                bullet.hideturtle()
                check = False
                bullet.penup()
                bullet.goto(-355,-250)
                bullet.pendown()                                

    # Update the scores
    if game_turn == player1_name:
        game_turn = player2_name
        board(player1_name,player2_name,player1_score,player2_score,player2_name,game_speed)
    elif game_turn == player2_name:
        game_turn = player1_name
        board(player1_name,player2_name,player1_score,player2_score,player1_name,game_speed) 

    
def save_game():
    data = []
    with open("game_state.txt", "r") as file:
        lines = file.readlines()
        for i in range(0,len(lines)):
            data.append(lines[i].strip())    
    with open("game_state.txt", "w") as file:
        file.write(player1_name + "\n")
        file.write(player2_name + "\n")
        file.write(str(player1_score) + "\n")
        file.write(str(player2_score) + "\n")
        if player1_score >= score_limit or player2_score >= score_limit:
            file.write("None\n")
        else:    
            file.write(game_turn + "\n")
        for i in range(0,len(lines)):
            file.write(data[i] + "\n")
    window.clear()
    window.bgcolor("gray")
    window.setup(width=800, height=600)    
    turtle.goto(0, 0)
    turtle.write("Game is Saved", align="center", font=("Arial", 24, "bold"))
    turtle.hideturtle()
    window.exitonclick()
    
def load_game():
    global player1_name, player2_name, player1_score, player2_score, game_turn

    with open("game_state.txt", "r") as file:
        lines = file.readlines()
        player1_name = lines[0].strip()
        player2_name = lines[1].strip()
        player1_score = int(lines[2].strip())
        player2_score = int(lines[3].strip())
        game_turn = lines[4].strip()
    board(player1_name,player2_name,player1_score,player2_score,game_turn,game_speed)    

# Set up the keyboard bindings
window.listen()
window.onkey(move_up, "Up")
window.onkey(move_down, "Down")
window.onkey(shoot, "space")
window.onkey(save_game, "s")
window.onkey(load_game, "l")

# Main game loop
where_1 = True
where_2 = True
while True:
    # Move the arrow
    x1 = b1.xcor()
    x2 = b2.xcor()
    y1 = b1.ycor()
    y2 = b2.ycor()
    
    if where_1 == True:
        x1 += 2*game_speed
    else:
        x1 -= 2*game_speed   
    
    if where_2 == True:
        x2 += 2*game_speed
    else:
        x2 -= 2*game_speed\
            
    b1.setx(x1)            
    b2.setx(x2)

    # Check for collision with the window edges
    if x1 > 350:
        where_1 = False
        b1.hideturtle()
        b1.speed(2*game_speed)
        b1.goto(350, y1)
        b1.showturtle()
    elif x1 < -350:
        where_1 = True
        b1.hideturtle()
        b1.speed(2*game_speed)
        b1.goto(-350, y1)
        b1.showturtle()   
    if x2 > 350:
        where_2 = False
        b2.hideturtle()
        b2.speed(2*game_speed)
        b2.goto(350, y2)
        b2.showturtle()
    elif x2 < -350:
        where_2 = True
        b2.hideturtle()
        b2.speed(2*game_speed)
        b2.goto(-350, y2)
        b2.showturtle()                       
        

    # Check for score limit reached
    if player1_score >= score_limit or player2_score >= score_limit:
        break
# Determine the winner
if player1_score > player2_score:
    winner = player1_name
elif player2_score > player1_score:
    winner = player2_name
else:
    winner = "No one (It's a tie)"

# Display the winner
turtle.goto(0, 0)
turtle.write("Game Over", align="center", font=("Arial", 24, "bold"))
turtle.goto(0, -50)
turtle.write("Winner: " + winner, align="center", font=("Arial", 20, "normal"))

turtle.done()    