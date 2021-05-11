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
- Connect Tello




# Reference
* [MediaPipe](https://github.com/google/mediapipe)
* [MediaPipe Hand gesture recognition (by Kazuhito00)](https://github.com/Kazuhito00/hand-gesture-recognition-using-mediapipe)
* [Tello SDK python interface](https://github.com/damiafuentes/DJITelloPy)