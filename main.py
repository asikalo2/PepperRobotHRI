from __future__ import division

import os
import qi
import sys
import time
import random
import argparse
import operator
from cd import *
from sonar import *
from touch import Touch
from gestures import Gesture
from numpy.random import choice


try:
    sys.path.insert(0, os.getenv('MODIM_HOME')+'/src/GUI')
except Exception as e:
    print ("Please set MODIM_HOME environment variable to MODIM folder.")
    print (e)
    sys.exit(1)
    
import ws_client
from ws_client import *

tablet = "./tablet/"
scripts = "scripts/"

global session
global index
global database
index = 1

global ALDialog
global topic_name
global topic_path
global doGesture
global name
global inputs_list


doGesture = True
name = ""
mws = ModimWSClient()
global running
running = False
inputs_list = []
        
def handleLastInput(lastInput):
    global audio_player_service
    global game_player_service
    global video_player_service
    global name
    global doGesture
    global index
    global topic_name
    global inputs_list
    print("last input: ", lastInput)
    inputs_list.append(lastInput)
    
    audio_player_service = session.service("ALAudioPlayer")
    game_player_service = session.service("ALTouch")
    selected_index = str(random.choice([1,2,3]))
    
    if "hi" in lastInput.lower():
        mws.run_interaction(test_interaction)  
        
    if len(inputs_list) >= 3:
        print(inputs_list)
        if "no" in inputs_list[-1] and "hi" in inputs_list[-3]:
            print("start over")
            ALDialog.unsubscribe('pepper_assistant')
            ALDialog.deactivateTopic(topic_name)
            ALDialog.unloadTopic(topic_name) 
            topic_path = project_path + "/topicFiles/main.top"
            # Loading the topic given by the user (absolute path is required)
            topf_path = topic_path.decode('utf-8')
            topic_name = ALDialog.loadTopic(topf_path.encode('utf-8'))
            print(topic_name)

            # Activate loaded topic
            ALDialog.activateTopic(topic_name)

            # Start dialog
            ALDialog.subscribe('pepper_assistant')
            gesture.stand()
            tts_service.say("Hello! I'm Pepper.\nI'm here to have some fun with you.\nYou can talk with me or interact by clicking the tablet."+" "*5, _async=True)
            
        if "stop" in inputs_list[-3] and "no" in inputs_list[-2] and "yes" in inputs_list[-1]:
            print("go to story")
            ALDialog.unsubscribe('pepper_assistant')
            ALDialog.deactivateTopic(topic_name)
            ALDialog.unloadTopic(topic_name) 
            topic_path = project_path + "/topicFiles/story.top"
            # Loading the topic given by the user (absolute path is required)
            topf_path = topic_path.decode('utf-8')
            topic_name = ALDialog.loadTopic(topf_path.encode('utf-8'))
            print(topic_name)

            # Activate loaded topic
            ALDialog.activateTopic(topic_name)

            # Start dialog
            ALDialog.subscribe('pepper_assistant')
            tts_service.say("Let's find out about your mood."+" "*5, _async=True)
            
    
    
    if "cats" in lastInput.lower():               
        gesture.doGesture = True
        print("doing cat motion...")
        #gesture.stand()
        gesture.doCat()
        #gesture.rest()
        
    if "dance" in lastInput.lower():               
        gesture.doGesture = True
        print("doing dance motion...")
        #gesture.stand()
        gesture.doDance()
        #gesture.rest()

    elif "stop" in lastInput.lower():
        for i in range(1000):
            audio_player_service.stop(i)
        gesture.doGesture = False
        index += 1    


def lauch_application(app):
    return


def main(session):
    stop_flag = False

    # Get ALDialog service
    
    robot_position = (0,0)

    sonar = Sonar(ALMemory, robot_position)
    sonar.set_sonar()
    #motion = Motion(ALMotion)
    
    tts_service.setLanguage("English")
    tts_service.setVolume(1.0)
    tts_service.setParameter("speed", 1.0)
    tts_service.say("Searching for children..."+" "*5, _async=True)
    gesture.gestureSearching()
    time.sleep(2)

    distances = sonar.get_distances()
    print("Distances: ", distances)
    min_distance, id = gesture.selectMinDistance(distances) #id is the person id
    print("Min distance: ", min_distance)
    gesture.forward(sonar, min_distance)
    print("Robot position", sonar.robot_position)
    sonar.robot_position = tuple(map(operator.sub, sonar.humans_positions[id], (0.5, 0)))
    print("Robot position", sonar.robot_position)

    tts_service.say("Hello! I'm Pepper.\nI'm here to have some fun with you.\nYou can talk with me or interact by clicking the tablet."+" "*5, _async=True)
    gesture.doHello()
    time.sleep(2)

    
    ALDialog.activateTopic(topic_name)
    ALDialog.subscribe('pepper_assistant')

    lastInput = ALMemory.subscriber("Dialog/LastInput")
    lastInput.signal.connect(handleLastInput)
    
    while not stop_flag:
        try:
            value = raw_input("Talk to robot / write in the console (insert stop to finish the conversation):")

        except KeyboardInterrupt:

            stop_flag = True
            # Stop the dialog engine
            ALDialog.unsubscribe('pepper_assistant')
            # Deactivate and unload the main topic
            ALDialog.deactivateTopic(topic_name)
            ALDialog.unloadTopic(topic_name)   
            
            return 0
        
        if value == "stop":
            
            stop_flag = True
            # Stop the dialog engine
            ALDialog.unsubscribe('pepper_assistant')
            # Deactivate and unload the main topic
            ALDialog.deactivateTopic(topic_name)
            ALDialog.unloadTopic(topic_name)     

    return 0

def test_interaction():
    im.init()
    lan = im.ask('choose-activity')
    print(lan)
    im.execute('goodbye')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="127.0.0.1",
                        help="Robot's IP address. If on a robot or a local Naoqi - use '127.0.0.1' (this is the default value).")
    parser.add_argument("--port", type=int, default=9559,
                        help="port number, the default value is OK in most cases")
    parser.add_argument("--project-path", type=str, required=True,
                        help="path of the project folder, for instance: /home/pepper")
   
    args = parser.parse_args()
    session = qi.Session()

    project_path = args.project_path

    try:
        session.connect("tcp://{}:{}".format(args.ip, args.port))
    except RuntimeError:
        print ("\nCan't connect to Naoqi at IP {} (port {}).\nPlease check your script's arguments."
               " Run with -h option for help.\n".format(args.ip, args.port))
        sys.exit(1)

    
    ALDialog = session.service('ALDialog')
    ALMemory = session.service('ALMemory')
    ALMotion = session.service("ALMotion")
    tts_service = session.service("ALTextToSpeech")
    ALDialog.setLanguage('English')  
    topic_path = project_path + "/topicFiles/main.top"
    topf_path = topic_path.decode('utf-8')
    topic_name = ALDialog.loadTopic(topf_path.encode('utf-8'))
    ALDialog.activateTopic(topic_name)
    ALDialog.subscribe('pepper_assistant')
    gesture = Gesture(ALMotion, doGesture, tts_service, )
    touch = Touch(ALMemory)     

    main(session)