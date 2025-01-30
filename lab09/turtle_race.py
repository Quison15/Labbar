
from race_window import RaceWindow
from race_turtle import RaceTurtle, MoleTurtle,AbsentMindedTurtle, DizzyTurtle
import random

w = RaceWindow()
del1 = False

#Del 1
turtles: list[RaceTurtle] = []
winners: list[RaceTurtle] = []
if del1:

    for i in range(8):
        turtles.append(RaceTurtle(w,i+1))


    while turtles: 
        for turtle in turtles:
            if turtle.xcor() <= w.X_END_POS:
                turtle.race_step()
                continue
            
            turtles.remove(turtle)
            winners.append(turtle)

    for i in range(3):
        print(f"På plats {i+1}: {winners[i]}")


#Del 2
else:
    for i in range(8):
        choice = random.randint(1,3)
        match choice:
            case 1:
                turtles.append(MoleTurtle(w,i+1))
            case 2:
                turtles.append(AbsentMindedTurtle(w,i+1,random.randint(0,100)))
            case 3:
                turtles.append(DizzyTurtle(w,i+1,random.randint(1,5)))

    for i in range(8):
        print(turtles[i])

    while turtles: 
            for turtle in turtles:
                if turtle.xcor() <= w.X_END_POS:
                    turtle.race_step()
                    continue
                
                turtles.remove(turtle)
                winners.append(turtle)

    for i in range(3):
        print(f"På plats {i+1}: {winners[i]}")
        