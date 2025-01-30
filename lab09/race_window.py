import turtle

class RaceWindow:
    X_START_POS = -300
    X_END_POS = 300
    Y_LINE_START = 200
    Y_LINE_END = -200
    COLORS = ['red', 'green', 'orange', 'yellow', 'blue', 'purple', 'black', 'brown']


    def __init__(self):
        self.screen = turtle.Screen()
        self.setup_window()
        self.draw_sratline()
        self.draw_endline()
        self.write_numbers()              

    def setup_window(self):
        self.screen.screensize(800 , 600)
        self.screen.title("Turtle Race") 
        self.screen.bgcolor("light yellow")        

    def draw_sratline(self):
        start = turtle.Turtle()
        start.penup()
        start.goto(self.X_START_POS, self.Y_LINE_START)
        start.pendown()
        start.goto(self.X_START_POS, self.Y_LINE_END)

    def draw_endline(self):
        end = turtle.Turtle()
        end.penup()
        end.goto(self.X_END_POS, self.Y_LINE_START)
        end.pendown()
        end.goto(self.X_END_POS, self.Y_LINE_END)

    def write_numbers(self):
        num = turtle.Turtle()
        num.penup()
        num.goto(self.X_START_POS - 30, self.Y_LINE_START - 20)
        num.setheading(-90)
        for i in range(1,9): 
            num.pendown()
            num.write(i)           
            num.penup()
            num.forward(50)
        
    def get_start_X(self , nbr):
        return self.X_START_POS
    
    def get_start_Y(self , nbr):
        return (self.Y_LINE_START-10) + (nbr-1) * -50
    
    def get_color(self, nbr):
        return self.COLORS[nbr-1]
    