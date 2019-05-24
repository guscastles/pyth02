## PYTH02 Bonuc Challenges: 2D Grpahics with PyGame

**Bonus features to add:**
- Make the circle bounce off the edges so it never leaves the screen
- Instead of bouncing off the edges, make the edges 'wrap', i.e. if the circle
hits the right edge of the screen it reappears from the left edge (and same for
the top/bottom edges).
- Draw multiple (10? 100?) circles moving around on the screen by creating a
list of circle dictionaries initialised with random position and speed values,
and loop over this list for every screen update, updating the position of each
circle and drawing it to the screen
- Make each circle check its distance from every other circle on the screen,
and draw a line between any two circles that get closer to each other than some
minimum distance (e.g. 200 pixels). To calculate the distance between two sets
of x, y coordinates you will need the "Distance Formula" (which comes from the
Pythagorean Theorem)
- Use the `pygame.mixer` sound module to play a bouncing sound whenever one of
the cirlces bounces off an edge (this actually sounds cool, especially if you
use a different sound sample for top/bottom vs left/right edges).
6- Use the up/down arrow keys to increase/decrease the overall speed of the
circles.
