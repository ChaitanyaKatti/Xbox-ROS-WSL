import pygame

# Initialize Pygame
pygame.init()

# Initialize the joystick
pygame.joystick.init()

# Check if a joystick is connected
if pygame.joystick.get_count() == 0:
    print("No joystick connected.")
    quit()
else:
    print("Connected. Writing to joystick_data.txt")
    
# Get the first joystick
joystick = pygame.joystick.Joystick(0)
joystick.init()

# Create a file to store the joystick data
filename = "joystick_data.txt"

# Main loop
while True:
    # Process Pygame events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    # Get the joystick buttons
    left_x_axis = '%.3f'%(joystick.get_axis(0))
    left_y_axis = '%.3f'%(joystick.get_axis(1))
    right_x_axis = '%.3f'%(joystick.get_axis(2))
    right_y_axis = '%.3f'%(joystick.get_axis(3))
    left_trigger = '%.3f'%(joystick.get_axis(4))
    right_trigger = '%.3f'%(joystick.get_axis(5))

    a_button = joystick.get_button(0)
    b_button = joystick.get_button(1)
    x_button = joystick.get_button(2)
    y_button = joystick.get_button(3)

    left_bumper_button = joystick.get_button(4)
    right_bumper_button = joystick.get_button(5)

    hat_x = joystick.get_hat(0)[0]
    hat_y = joystick.get_hat(0)[1]

    #print(left_x_axis, left_y_axis, right_x_axis, right_y_axis, left_trigger, right_trigger, hat_x, hat_y, "\n" )
    
    # Write the joystick data to the file
    with open(filename, "w") as f:
        f.write(f"{left_x_axis} {left_y_axis} {right_x_axis} {right_y_axis} {left_trigger} {right_trigger} {a_button} {b_button} {x_button} {y_button} {left_bumper_button} {right_bumper_button} {hat_x} {hat_y}\n")

    # Wait for a short time
    pygame.time.wait(50)