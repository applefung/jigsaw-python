#Name:Feng Yeqing  ID:20510788
import turtle
import random
width=turtle.window_width()
height=turtle.window_height()
turtle.hideturtle()
### This part of Python code will create the jigsaw pieces when starting up
### by setting up random positions and loading the corresponding image
def createJigsaw():
    global allTurtles

    # Initialize the variables of total number of rows and columns
    # Now we go through the jigsaw piece row-column structure
    # Go through each row
        # Go through each column in this row
    for row in range(3):
        for column in range(3):
            # Make a new turtle
            x=random.randint(-width/2,width/2)
            y=random.randint(-height/2,height/2)
            turtleone=turtle.Turtle()
            turtleone.up()
            turtleone.goto(x,y)
            turtle.down()
            # Move it to a random position

            # Build the image file name
            thisFilename="image"+"-"+str(row)+"-"+str(column)+".gif"
            turtle.addshape(thisFilename)
            turtleone.shape(thisFilename)
            turtleone.ondrag(turtleone.goto)
            turtleone.speed(0)
            allTurtles.append(turtleone)
            # Add the image to the turtle system
            # Apply the new image to this turtle
 
            # Now fix it so that when this turtle is dragged, it goes to the place where it is dragged
             
            # Add the new turtle to the new list of turtles

        
### This part of Python code will only run when the user presses "c" to check the jigsaw
def checkJigsaw():
    checkResult=True # At the start, we assume everything is OK

    for thisTurtle in allTurtles: # Go through every single turtle that we made
        thisX = thisTurtle.xcor() # Get the x coordinate of this turtle
        thisY = thisTurtle.ycor() # Get the y coordinate of this turtle

        # An example filename is "image-2-1.gif"
        thisFilename = thisTurtle.shape() # Take the image filename of this turtle
        
        lengthOfThisFilenameWithoutExtension= len(thisFilename)-4 # How long the filename is without the ".gif"
        thisFilenameWithoutExtension=thisFilename[ : lengthOfThisFilenameWithoutExtension ] # Remove the ".gif"
        piecesOfFilenameWithoutExtension=thisFilenameWithoutExtension.split("-") # Divide the filename into 3 pieces

        thisRow=piecesOfFilenameWithoutExtension[1] # Take the Row number from the filename (the second piece of text)
        thisCol=piecesOfFilenameWithoutExtension[2] # Take the Col number from the filename (the third piece of text)
        
        thisRow=int(thisRow) # Have to convert the text to an integer before comparing it with a number
        thisCol=int(thisCol) # Have to convert the text to an integer before comparing it with a number

        # We need to check this turtle with all other turtles for position violations
        for compareTurtle in allTurtles: # Go through every other turtle
            compareX = compareTurtle.xcor() # Get the x coordinate of the turtle
            compareY = compareTurtle.ycor() # Get the y coordinate of the turtle

            # An example filename is "image-2-1.gif"
            compareFilename = compareTurtle.shape() # Take the image filename of this turtle
            
            lengthOfCompareFilenameWithoutExtension= len(compareFilename)-4 # How long the filename is without the ".gif"
            compareFilenameWithoutExtension=compareFilename[ : lengthOfCompareFilenameWithoutExtension ] # Remove the ".gif"
            piecesOfFilenameWithoutExtension=compareFilenameWithoutExtension.split("-") # Divide the filename into 3 pieces

            compareRow=piecesOfFilenameWithoutExtension[1] # Take the Row number from the filename (the second piece of text)
            compareCol=piecesOfFilenameWithoutExtension[2] # Take the Col number from the filename (the third piece of text)
            
            compareRow=int(compareRow) # Have to convert the text to an integer before comparing it with a number
            compareCol=int(compareCol) # Have to convert the text to an integer before comparing it with a number

            # Here, the four position violations will be checked
            # The jigsaw is wrong if any of them fails

            # The piece has a smaller column value but is on the right
            if thisCol < compareCol and thisX >= compareX:
                checkResult = False
                break
            # The piece has a larger column value but is on the left
            elif thisCol > compareCol and thisX <= compareX:
                checkResult = False
                break
            # The piece has a smaller row value but is on the bottom
            elif  thisRow < compareRow and thisY <= compareY:
                checkResult = False
                break
            # The piece has a larger row value but is on the top
            elif  thisRow > compareRow and thisY >= compareY:
                checkResult = False
                break

            
            
    # Let's check the final result and show an appropriate message
    if checkResult == True:
        turtle.clear()
        turtle.color("red")
        turtle.write("Congratulations! Your jigsaw is correct!",font=("Arial",20,"bold"))
    else:
        turtle.clear()
        turtle.color("red")
        turtle.write("Oh no! Your jigsaw is WRONG!!",font=("Arial",20,"bold"))

### Here is the main part of the program

allTurtles=[] # We will store all the turtles in this list

createJigsaw() # Create the jigsaw pieces
    
turtle.onkeypress(checkJigsaw, "c") # Press 'c' whenever you want to check the jigsaw

turtle.listen() # Listen for key presses

### Note: turtle.mainloop() is exactly the same as turtle.done()
turtle.mainloop() # Keep checking if anything is happening, if so do something appropriate
