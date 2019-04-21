# Bonus challenges:
# 1. Make the circle bounce off the edges so it never leaves the screen
# 2. Instead of bouncing off the edges, make the edges 'wrap', i.e. if the circle
# hits the right edge of the screen it reappears from the left edge (and same for
# the top/bottom edges).
# 3. Draw multiple (10? 100?) circles moving around on the screen by creating a
# list of circle dictionaries initialised with random position and speed values,
# and loop over this list for every screen update, updating the position of each
# circle and drawing it to the screen
# 4. Make each circle check its distance from every other circle on the screen,
# and draw a line between any two circles that get closer to each other than some
# minimum distance (e.g. 200 pixels). To calculate the distance between two sets
# of x, y coordinates you will need the "Distance Formula" (which comes from the
# Pythagorean Theorem)
# 5. Use the `pygame.mixer` sound module to play a bouncing sound whenever one of
# the cirlces bounces off an edge (this actually sounds cool, especially if you
# use a different sound sample for top/bottom vs left/right edges).
# 6. Use the up/down arrow keys to increase/decrease the overall speed of the
# circles.

# modules required by the program
import pygame
import sys
import math
from random import randint

# global variables for this program
width  = 800
height = 600
speed_scale = 1.0
circles = []   # a list to store all circle info in, as dictionaries

circle_count = 70  # default value
# Get number of circles to use from command line argument, if given
if len(sys.argv) > 1:
    try:
        circle_count = int(sys.argv[1])
    except ValueError:
        print("Please give only an integer for the number of circles: got '{}'".format(sys.argv[1]))
        sys.exit()  # quit program



# functions for this program

def update_circle_position(circle, bounce=True):
    """Update the position of the circle passed in, and handle edge contact by
    either bouncing or wrapping, depending on second argument."""

    # Update the position values of this circle using the speed values of this
    # circle; multiply by the global speed variable to make the entire simulation
    # faster or slower
    circle['x_pos'] += int(circle['x_speed'] * speed_scale)
    circle['y_pos'] += int(circle['y_speed'] * speed_scale)

    # The optional second argument to this function lets us choose which of the
    # edge-handling styles we want to to use: bouncing off the edges, or wrapping
    # around from one edge to the other
    if bounce:
        # Bouncing:
        # when a circle touches an edge, reverse its speed on that  axis (x or y)
        # by multiplying by -1; this will reverse its direction
        if circle['x_pos'] >= width or circle['x_pos'] <= 0:
            circle['x_speed'] *= -1
            if sounds[0]: sounds[0].play()
        if circle['y_pos'] >= height or circle['y_pos'] <= 0:
            circle['y_speed'] *= -1
            if sounds[1]: sounds[1].play()
    else:
        # Wrapping:
        # when a circle touches an edge, change its position for that axis
        # so it appears on the opposite edge (moving in the same direction)
        # NOTE: Python lets you put the body of an 'if' condition on the same
        # line as the header! Only do this when the body is a short single line
        # as below.
        if circle['x_pos'] > width  : circle['x_pos'] = 0
        if circle['x_pos'] < 0      : circle['x_pos'] = width
        if circle['y_pos'] > height : circle['y_pos'] = 0
        if circle['y_pos'] < 0      : circle['y_pos'] = height

    return circle


def detect_nearby_circles(circle, distance_threshold=70):
    """Calculate the distance between the circle passed in and every other
    circle, and draw a line to any that are within the threshold distance."""

    for other_circle in circles:
        dist = distance_between_circles(circle, other_circle)
        if dist < distance_threshold:
            draw_line_between_circles(circle, other_circle)


def distance_between_circles(c1, c2):
    """Returns the distance between two circles, using the Distance Formula."""

    # Distance formula! dist = sqrt( (x2 - x1)^2 + (y2 - y1)^2 )
    # https://www.varsitytutors.com/hotmath/hotmath_help/topics/distance-formula

    dist_squared = (
                     (c2['x_pos'] - c1['x_pos'])**2 +
                     (c2['y_pos'] - c1['y_pos'])**2
                   )

    dist = math.sqrt( dist_squared )

    return dist


def draw_line_between_circles(c1, c2, thickness=1):
    """Draws a line between the given circles."""

    pygame.draw.line(
      screen,
      (0, 200, 0),  # green
      (c1['x_pos'], c1['y_pos']),  # from here
      (c2['x_pos'], c2['y_pos']),  # to here
      thickness
    )


def draw_circle(circle, size=10):
    """Draw the circle based on colour and position values in its dictionary"""

    pygame.draw.circle(
      screen,
      circle['colour'],                    # R,G,B colour tuple
      (circle['x_pos'], circle['y_pos']),  # position
      size,                                # radius
      0                                    # thickness; 0 means filled in
    )


def handle_event(event):
    """Handle a Pygame event; in particular, change speed on up/down arrow
    keypress, or quit on any other keypress."""

    global speed_scale   # So we can change this global variable

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            # Speed up all movement on up-key press
            speed_scale += 0.2
        elif event.key == pygame.K_DOWN:
            # Slow down all movement on up-key press
            speed_scale -= 0.2
        else:
            pygame.quit()  # clean up the pygame session
            sys.exit()


######### Main program code

# Every pygame program needs to run this setup function
pygame.init()

# Initialise the sound system and load the two sample files we want to use, into
# a tuple. If the files are not found in the same folder as this script file, an
# error will be caught and the sounds tuple will be set to None values, preventing
# the sounds from playing.
try:
    pygame.mixer.init()
    sounds = (
      pygame.mixer.Sound("paddle1.wav"),
      pygame.mixer.Sound("paddle2.wav")
     )
except Exception as ex:
    print("Sample file not found: {}.\nSounds disabled.".format(ex.args))
    sounds = (None, None)

# Create a primary screen object where the drawing happens
screen = pygame.display.set_mode( (width, height) )

# Or try out fullscreen mode:
# screen = pygame.display.set_mode( (0,0), pygame.FULLSCREEN )
# info = pygame.display.Info() # In fullscreen we don't know the size in advance;
# width = info.current_w       # so get the screen size from the Info function() -
# height = info.current_h      # we need it to calculate bouncing/wrapping


# Create a dictionary to append to the list 'circles' which will keep track of
# the position and speed of each individual circle; you could just use a list or
# tuple to store these values but then you would have to remember that circle[0]
# is the x position, and so on. Using a dictionary with meaningful  keys is much
# clearer (though ultimately slower than indexing into a list or tuple).
for i in range(circle_count):
    circles.append({
      'x_pos': randint(1, width-1),   # don't create directly on edges
      'y_pos': randint(1, height-1),  # (or they'll get stuck)
      'x_speed': randint(-7, 7),
      'y_speed': randint(-7, 7),
      'colour': (randint(0, 255), randint(0, 255), randint(0, 255))
    })


# Main draw loop
while True:
    
    # Loop through any pending events. The body of this loop is now long enough that
    # it deserves its own function, keeping the body of this 'while' loop short.
    for event in pygame.event.get():
        handle_event(event)

    # clear screen before each draw; otherwise we get 'trails'
    screen.fill(0)

    # Handle each circle using the functions defined at the top of the file.
    # Notice how short and readable the body of this loop becomes when we
    # use functions like this: it reads like a recipe of what to do for each
    # circle: 1) update position, 2) check for nearby circles, 3) draw the
    # circle. We see at a glance what is done with each circle, and if we want
    # any more details about any part, we can look inside the specific function.
    for circle in circles:
        circle = update_circle_position(circle, bounce=True)
        detect_nearby_circles(circle)
        draw_circle(circle)

    pygame.display.update()  # draw any changes made to the screen


    # end of main 'while' draw loop
