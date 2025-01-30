import turtle
import random


from race_window import RaceWindow
class RaceTurtle(turtle.Turtle):
    def __init__(self,w: RaceWindow, nbr):
        super().__init__(shape = "classic", undobuffersize = 1000, visible = True)
        self.nbr = nbr
        self.x = w.get_start_X(nbr)
        self.y = w.get_start_Y(nbr)
        self.teleport(self.x,self.y)
        

    def race_step(self):
        self.forward(random.randint(1,6))
    
    def __str__(self):
        return f"Nummer {self.nbr}"

class MoleTurtle(RaceTurtle):
    def race_step(self):
        if random.random() > 0.5:
            self.penup()
        else:
            self.pendown()
        super().race_step()
    def __str__(self):
        return super().__str__() + " - MoleTurtle"

class AbsentMindedTurtle(RaceTurtle):
    def __init__(self, w, nbr,absentGrade):
        super().__init__(w, nbr)
        self.absentGrade = absentGrade /100

    def race_step(self):
        if random.random() > self.absentGrade:
            super().race_step()

    def __str__(self):
        return super().__str__() + f" - AbsentMindedTurtle ({int(self.absentGrade*100)}% Frånvarande)"
    
class DizzyTurtle(RaceTurtle):

    def __init__(self, w: RaceWindow, nbr, dizzyGrade):
        super().__init__(w, nbr)
        self.w = w
        self.dizzyGrade = dizzyGrade

    def race_step(self):
        super().race_step()
        wobble = random.randint(-self.dizzyGrade, self.dizzyGrade)
        self.setheading(self.heading()+wobble)
        self.keep_on_track()
    def keep_on_track(self):
        yBorder = self.w.Y_LINE_START
        x,y = self.pos()
        if x < self.w.X_START_POS or abs(y) > yBorder:
            self.setheading(self.towards(self.w.X_END_POS,self.y))
            #self.forward(10)
            

    def __str__(self):
        return super().__str__() + f" - DizzyTurtle (Yrsel: {self.dizzyGrade})"
    
#turtle.Screen().delay(0.1)
if __name__ == '__main__':
    w = RaceWindow()
    t = DizzyTurtle(w,5,5)
    t.keep_on_track() 
    turtle.mainloop()