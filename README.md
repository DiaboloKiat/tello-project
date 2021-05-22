# tello-project

# Clone repo
```
$ git clone https://github.com/DiaboloKiat/tello-project.git
$ cd tello-project
```

# Setting Anaconda environment
- Install Anaconda
```
$ bash Anaconda3-2020.11-Linux-x86_64.sh
$ reboot
```
### Basic Instruction
- Create a new anaconda environment
```
$ conda create --name “Name of environment” python=3.7
```
- Delete environment
```
$ conda remove --name “Name of environment” 
```
- Enter to the anaconda environment
```
$ conda activate “Name of environment”
```
- Quit to the anaconda environment
```
$ conda deactivate
```
# Tello setup
- Install pip packages
```
$ pip3 install djitellopy2
$ pip3 install -r requirements.txt
```

- List of packages
```
ConfigArgParse == 1.2.3
djitellopy == 1.5
numpy == 1.20.3
opencv_python == 4.5.1.48
tensorflow == 1.15.2(jupyter notebook) /  2.4.1(hand_gesture_control.py)
mediapipe == 0.8.2
```

- Connect Tello

Confirm connection status
```
$ cd ~/tello-project
$ python3 basic_system/connection_test.py
```
On successful connection
```
1. Connection test:
Send command: command
Response: b'ok'


2. Video stream test:
Send command: streamon
Response: b'ok'


Send command: streamoff
Response: b'ok'
```
If you get such output, you may need to check your connection with the drone
```
1. Connection test:
Send command: command
Timeout exceed on command command
Command command was unsuccessful. Message: False


2. Video stream test:
Send command: streamon
Timeout exceed on command streamon
Command streamon was unsuccessful. Message: False
```



# Keyboard control
Basic to control the drone with your keyboard
```
$ cd ~/tello-project
$ python3 basic_system/basic_test.py
```
| keys    | action   |
|:-------:|:--------:|
| Space   | Take off drone(if landed) **OR** Land drone(if in flight) |
| w       | Move forward |
| s       | Move back |
| a       | Move left |
| d       | Move right |
| e       | Rotate clockwise |
| q       | Rotate counter-clockwise |
| r       | Move up |
| f       | Move down |
| Esc     | End program and land the drone |







# Reference
- [Tello API](https://djitellopy.readthedocs.io/en/latest/tello/)
- [MediaPipe](https://github.com/google/mediapipe)
- [MediaPipe Hand gesture recognition (by Kazuhito00)](https://github.com/Kazuhito00/hand-gesture-recognition-using-mediapipe)
- [Tello SDK python interface](https://github.com/damiafuentes/DJITelloPy)
- [tello-gesture-control by kinivi](https://github.com/kinivi/tello-gesture-control)