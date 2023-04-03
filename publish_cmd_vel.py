import rospy
from geometry_msgs.msg import Twist

rospy.init_node('game_controller')
velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

print("Publishing data from joystick_data.txt")

file_path = 'joystick_data.txt' # Open the file containing the velocity values

linear_vel = 0
angular_vel = 0
Max_linear_vel = 3
Max_angular_vel = 2
 
while not rospy.is_shutdown():
   
    with open(file_path, 'r') as f:  # Open the file and read the velocities from the first line
        line = f.readline()
        values = line.split()
        #print("values are", values)
        if(len(values) == 14): #Sometime the file becomes empty for a berif moment
            throttle = (1 + float(values[5]))/2      # Throttle-Left trigger
            linear_vel = Max_linear_vel*throttle
            angular_vel = -1*Max_angular_vel*float(values[0]) # Turning rate-Right x axis
    
    #print(linear_vel, angular_vel, "\n")
    
    vel_msg = Twist() # Create a Twist message with the read linear and angular velocities
    vel_msg.linear.x = linear_vel  # meters per second
    vel_msg.angular.z = angular_vel  # radians per second
    velocity_publisher.publish(vel_msg) # Publish the Twist message to the /cmd_vel topic
    rospy.sleep(0.1)
