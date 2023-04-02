# Xbox-ROS-WSL

A simple way to bypass the need to share USB devices like Xbox controller with Linux in WSL.

- `print_script.py` simply writes a single line text file with values of the current state of Xbox Controller. Run this script under Windows OS

- `publish_cmd_vel.py` can be run in Linux to publish ROS topic `/cmd_vel`


I have also included the .exe is that does the same thing as `print_script.py`

Keep all the files in the same folder.

## Control scheme
- Right trigger is published as `linear.x` in `/cmd_vel` topic
- Left joystick x axis is published as `angular.z` in `/cmd_vel` topic


