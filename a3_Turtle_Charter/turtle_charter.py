# A module for drawing a chart with the turtle
import turtle  # import module

# Funcions
def count_observation(data_name):
    """Count the number of observations
    
    Arguments: 
        dt_name: the path to the file
    """
    #filename = str(data_name)
    with open(data_name) as file: 
        num_lines = 0
        for line in file: 
            num_lines = num_lines + 1
        num_obs = num_lines/3
    return(int(num_obs))

def get_max_value(dt_name):
    """the maximum value of the first 
    feature across the observations

    Arguments: 
        dt_name: the path to the file

    Returns:
        'max_num' = max number across features as an integer
    """
    with open(dt_name) as file:
        num = 0
        max_num = 0
        for line in file:
            num += 1
            if num % 3 == 2 and int(line) > int(max_num):           
                max_num = line
        return(int(max_num))

# Drawing x- and y- axes and y-ticks.
def draw_x_axis():
    """ Draw x axis
    
    Arguments: 
        NA
    """

    young.penup()
    young.goto(30,30)
    young.pendown()
    young.forward(750)
    young.left(360)
  
def draw_y_axis(dt_name):
    """Draw y axis"
    
    Arguments: 
        dt_name: the path to the file
    """
    young.penup()
    young.goto(30,30)
    young.pendown()
    young.goto(30,30+get_max_value(dt_name)*6.5)
    young.left(90)
    
def draw_y_tick_mark(dt_name):
    """Draw y tick marks and their lables.
    
    Arguments: 
        dt_name: the path to the file
    """
    num = (get_max_value(dt_name)*6.5)/10
    for i in range(1,11):
        young.penup()
        young.home()
        young.goto(30,30)
        young.pendown()    
        young.goto(30,30+num*i)
        young.backward(5)
        young.write(str((get_max_value(dt_name)/10)*i),align = "right", font=("Arial", 9, "normal"))
        young.left(90)
        
def draw_axes(dt_name):        
    """Draw x- and y- axes and y-tick marks and their lables.
    
    Arguments: 
        dt_name: the path to the file
    """
    draw_x_axis()
    draw_y_axis(dt_name)
    draw_y_tick_mark(dt_name)
    young.penup()
    young.goto(30,30)

def draw_rectangle(height, rec_width, rec_color):
    """Draw and color a rectangle with a certian height and width.
    
    Arguments: 
        height: the height of the rectangle
        rec_width: the width of the rectacgle
        rec_color: the color of the rectacgle
    """
    young.begin_fill()               # start filling this shape
    young.color(rec_color)
    young.left(90)
    young.forward(height) # the height of the rectangle
    young.write("   " + str(height/6.5), font=("Arial", 9, "normal")) 
    young.right(90)
    young.forward(rec_width) # the width of the rectangle
    young.right(90)
    young.forward(height)
    young.left(90)
    young.end_fill()

def get_values(dt_name, feature_num):
    """Get values of a specific feature
    
    Arguments: 
        dt_name: the path to the file
        feature_num: the feature number

    Returns:
        'values': a list containing all values in a specific feature, 
    """
    with open(dt_name) as file:
        num = 0
        values = []
        for line in file:
            num += 1
            if num % 3 == (feature_num+1) % 3:          
                values.append(line)
        return(values)

def draw_x_axis_lable(dt_name):
    """Draw x-axis lable
    
    Arguments: 
        dt_name: the path to the file
    """
    lables = get_values(dt_name, 0)
    bar_width = (740-10*count_observation(dt_name))/count_observation(dt_name)
    for i in range(count_observation(dt_name)):
        young.penup()
        young.home()
        young.goto(63,0)    
        young.forward(bar_width*i + 10*i)
        young.write(lables[i],align = "center", font=("Arial", 9, "normal"))
        young.left(90)

def draw_bars(dt_name, feather_num):
    """Draw bars
    
    Arguments: 
        dt_name: the path to the file
        feature_num: the feature number
    """    
    idx = 0
    bar_width = (740-10*count_observation(dt_name))/count_observation(dt_name)
    values = get_values(dt_name, feather_num)
    young.penup()
    young.home()
    young.goto(40,30)
    for bar_height in values:    
        young.pendown()
        draw_rectangle(6.5*int(bar_height), bar_width, choose_color(idx))
        idx += 1
        young.penup()
        young.forward(10)
        young.left(360)
    young.goto(30,30)

def choose_color(index):
    """Choose a color in a list
    
    Arguments: 
        index: the index number
    """    
    colors = ["lightcoral", "lightblue", "green","purple","orange","gold"]
    return colors[index%6]

if __name__ == "__main__":
    data_name = input("Which file to visualize? ") # Reads the txt file at path
    chart_name = input("What should the chart be named? ") #Assign the window name
    
    # Define window size as constants
    window = turtle.Screen()  # create a window for the turtle to draw on
    window.title(chart_name)  # the title to show at the top of the window
    WINDOW_WIDTH = 800  # specify window size (width, height)
    WINDOW_HEIGHT = 500
    window.setup(WINDOW_WIDTH, WINDOW_HEIGHT)  
    window.setworldcoordinates(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT)  # coordinate system: origin at lower-left

    # Create the turtle
    young = turtle.Turtle()
    young.speed("fastest")  # how fast the turtle should move

    filename = str(data_name)
    
    # Functions
    draw_axes(filename)
    draw_x_axis_lable(filename)
    draw_bars(filename, 1)

# Make the turtle graphics appear and run, waiting for the user to close the screen
# This MUST be the last statement executed in the script
window.mainloop()
