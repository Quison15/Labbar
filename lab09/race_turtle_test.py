
from race_window import RaceWindow
from race_turtle import RaceTurtle

w = RaceWindow()
t1 = RaceTurtle(w , 1)

while t1.xcor() <= w.X_END_POS:
    t1.race_step()

print('I mål ' , t1) 