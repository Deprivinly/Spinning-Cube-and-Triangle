# Spinning-Cube-and-Triangle

Key Concepts
3D Projection and Rotation:

The 3D objects (cube and triangle) are defined by their vertices in 3D space.
To display these objects on a 2D screen, the vertices are rotated and then projected into 2D space using simple projection math.
Animation and Dynamics:

The cube and triangle move (bounce) within the window and rotate around all three axes.
Colors change smoothly over time using the HSV (Hue, Saturation, Value) color model.
Step-by-Step Explanation
1. Initialization
Pygame Setup:
Initializes Pygame, sets up the display, and defines a clock for frame-rate control.
Screen Dimensions:
width, height = 800, 600: The window size is 800x600 pixels.
Objects:
Cube: Defined by 8 vertices (Vector3) and 12 edges.
Triangle: Defined by 4 vertices (Vector3) and 6 edges.
2. Rotation Logic (rotate_point)
This function rotates a 3D point around the X, Y, and Z axes using rotation matrices.
The angles (angle_x, angle_y, angle_z) are incremented with every frame for continuous rotation.
3. Projection Logic (project_point)
Converts a rotated 3D point into a 2D point on the screen:
Perspective Projection: Simulates depth by scaling points based on their distance from the camera (factor = 300 / (4 + point.z)).
This makes objects farther away appear smaller.
4. Animation
The cube and triangle are assigned:
Position (cube_pos and triangle_pos): Starting positions on the screen.
Velocity (cube_vel and triangle_vel): Movement speeds.
Positions are updated every frame based on their velocities.
5. Collision Detection
Checks if the cube or triangle hits the "walls" of the window:
If a position goes out of bounds, the velocity is reversed (cube_vel.x *= -1), making the object "bounce."
6. Color Changing
The hue value cycles smoothly from 0 to 1 using colorsys.hsv_to_rgb().
This generates RGB colors that shift through the spectrum (e.g., red to orange to yellow, etc.).
7. Drawing
Vertices: Each vertex of the cube and triangle is rotated and projected into 2D space.
Edges: Lines are drawn between projected points using pygame.draw.line(). These represent the edges of the cube and triangle.
Color: The color of the edges is dynamically updated based on the hue value.
Core Loop (while running)
The main loop controls the animation:

Event Handling: Checks for pygame.QUIT to exit the program.
Screen Clearing: Clears the screen each frame by filling it with black (display.fill(BLACK)).
Object Updates:
Updates the positions of the cube and triangle based on velocity.
Rotates vertices of the cube and triangle.
Projects vertices into 2D space for rendering.
Collision Handling: Reverses velocity if objects hit the screen edges.
Color Update: Gradually changes the hue for dynamic color animation.
Rendering: Draws the cube and triangle by connecting their edges.
Frame Rate Control: Limits the frame rate to 60 FPS with clock.tick(60).
Output
3D Visuals:
A cube and a triangle rotate continuously around all three axes, creating a 3D effect.
Both objects bounce around the screen and change colors dynamically.
Dynamic Color Animation:
The edges of the objects smoothly transition through the color spectrum.
Key Features
3D Simulation:
Implements basic 3D transformations (rotation and perspective projection) for realistic rendering.
Dynamic Animation:
Combines rotation, bouncing, and color transitions for a visually engaging result.
Modular Design:
Functions (rotate_point, project_point) encapsulate transformations, making it easy to extend.
