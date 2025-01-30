'''import heapq
import math
import turtle
import maze

def heuristic(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def draw_path(path):
    pen = turtle.Turtle()
    turtle.Screen().delay(0)
    turtle.Screen().tracer(10)
    pen.speed(0)
    pen.hideturtle()
    pen.penup()
    pen.color("red")
    
    for x, y in path:
        pen.goto(x, y)
        pen.dot(2, "red")

def a_star_solver(maze: maze):
    start = maze.entry()
    goal = (start[0], maze._window_height // 2)  # Exit is at the bottom
    
    open_list = []
    heapq.heappush(open_list, (0, start))
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}
    
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Up, Down, Right, Left
    
    while open_list:
        _, current = heapq.heappop(open_list)
        
        if maze.at_exit(current) and current[1] > 160:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            draw_path(path)
            print(len(path))  # Draw the path with red dots
            return path
        
        for dx, dy in directions:
            neighbor = (current[0] + dx, current[1] + dy)
            if maze.wall_in_front(math.degrees(math.atan2(-dy, dx)), current) or neighbor[1] < -160:
                continue
            
            tentative_g_score = g_score[current] + 1
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                heapq.heappush(open_list, (f_score[neighbor], neighbor))
    
    return None  # No path found
'''






import heapq
import math
import turtle
import maze

def heuristic(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def draw_path(path):
    pen = turtle.Turtle()
    turtle.Screen().delay(0)
    turtle.Screen().tracer(10)
    pen.speed(0)
    pen.hideturtle()
    pen.penup()
    pen.color("red")
    
    for x, y in path:
        pen.goto(x, y)
        pen.dot(2, "red")

def a_star_solver(maze):
    start = maze.entry()
    goal = (start[0], -maze._window_height // 2)  # Exit is at the bottom
    
    open_list = []
    heapq.heappush(open_list, (0, start))
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}
    
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0),  # Up, Down, Right, Left
                  (1, 1), (1, -1), (-1, 1), (-1, -1)]  # Diagonal movements
    
    while open_list:
        _, current = heapq.heappop(open_list)
        
        if maze.at_exit(current) and current[1] > 160:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            draw_path(path)
            print(len(path))  # Draw the path with red dots
            return path
        
        for dx, dy in directions:
            neighbor = (current[0] + dx, current[1] + dy)
            if maze.wall_in_front(math.degrees(math.atan2(-dy, dx)), current)  or neighbor[1] < -160:
                continue
            
            tentative_g_score = g_score[current] + (1.4 if dx != 0 and dy != 0 else 1)  # Diagonal movement costs more
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                heapq.heappush(open_list, (f_score[neighbor], neighbor))
    
    return None  # No path found

i = 5

m = maze.Maze(int(i))
path = a_star_solver(m)
turtle.done()