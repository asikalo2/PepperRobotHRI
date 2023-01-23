import time

class Gesture:
    def __init__(self, ALMotion, doGesture, tts_service):
        self.ALMotion = ALMotion
        self.doGesture = doGesture
        self.tts_service = tts_service
   
    def gestureSearching(self):
        for i in range(1):
            jointNames = ["HeadYaw", "HeadPitch"]
            angles = [0.5, -0.07]
            times  = [2.0, 2.0]
            isAbsolute = True
            self.ALMotion.angleInterpolation(jointNames, angles, times, isAbsolute)

            jointNames = ["HeadYaw", "HeadPitch"]
            angles = [-0.5, -0.07]
            times  = [2.0, 2.0]
            isAbsolute = True
            self.ALMotion.angleInterpolation(jointNames, angles, times, isAbsolute)

        return
   
    def doCat(self):
        names = list()
        times = list()
        keys = list()
        
        names.append("LShoulderPitch")
        times.append([1.0, 2.0, 3.0])
        keys.append([1.0, -0.2, 0.8])
        
        names.append("RShoulderPitch")
        times.append([1.0, 2.0, 3.0])
        keys.append([1.0, -0.2, 0.8])
        
        self.ALMotion.angleInterpolation(names, keys, times, True)
        return
    
    def doDog(self):
        names = list()
        times = list()
        keys = list()
        
        names.append("LShoulderPitch")
        times.append([3.0, 1.0, 3.0])
        keys.append([-1.0, 0.2, -0.8])
        
        names.append("RShoulderPitch")
        times.append([3.0, 1.0, 3.0])
        keys.append([1.0, 0.4, -0.8])
        
        self.ALMotion.angleInterpolation(names, keys, times, True)
        return

    def stand(self):
        self.posture_service.goToPosture("Stand", 0.5)
        print("Robot is in default position")

    def rest(self):
        self.posture_service.goToPosture("Crouch", 0.5)
        print("Robot is in resting position")
    
    def doDance(self):
        names = list()
        times = list()
        keys = list()
        
        names.append("HeadPitch")
        times.append([1.52, 2.36, 3.32, 4.16, 5.08, 5.92, 6.88, 7.72, 8.16, 8.84, 9.68, 10.64, 11.48, 12.4, 13.24, 14.2, 15.04, 16.24])
        keys.append([-0.476475, 0.338594, -0.476475, 0.338594, -0.476475, 0.338594, -0.476475, 0.338594, 0.0680678, -0.476475, 0.338594, -0.476475, 0.338594, -0.476475, 0.338594, -0.476475, 0.338594, -0.17185])

        names.append("HeadYaw")
        times.append([1.52, 2.36, 3.32, 4.16, 5.08, 5.92, 6.88, 7.72, 8.16, 8.84, 9.68, 10.64, 11.48, 12.4, 13.24, 14.2, 15.04, 16.24])
        keys.append([-0.745256, 0.0411095, -0.745256, 0.0411095, -0.745256, 0.018508, -0.745256, 0.289725, 0.425684, 0.745256, -0.0411095, 0.745256, -0.0411095, 0.745256, -0.018508, 0.745256, -0.289725, 0.00916195])

        names.append("HipPitch")
        times.append([0.68, 1.52, 2.36, 3.32, 4.16, 5.08, 5.92, 6.88, 7.72, 8.84, 9.68, 10.64, 11.48, 12.4, 13.24, 14.2, 15.04, 16.24])
        keys.append([-0.376033, -0.036954, -0.344024, -0.0404086, -0.339835, -0.038321, -0.341769, -0.0367355, -0.34817, -0.035085, -0.341769, -0.0382761, -0.339629, -0.0396041, -0.341605, -0.0362713, -0.343065, -0.0495279])

        names.append("HipRoll")
        times.append([1.52, 2.36, 3.32, 4.16, 5.08, 5.92, 6.88, 7.72, 8.84, 9.68, 10.64, 11.48, 12.4, 13.24, 14.2, 15.04, 16.24])
        keys.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

        names.append("KneePitch")
        times.append([0.68, 1.52, 2.36, 3.32, 4.16, 5.08, 5.92, 6.88, 7.72, 8.84, 9.68, 10.64, 11.48, 12.4, 13.24, 14.2, 15.04, 16.24])
        keys.append([0.166965, -0.00379234, 0.185949, -0.0129339, 0.180821, -0.00320919, 0.187035, -0.00931236, 0.182162, -0.0111253, 0.187035, -0.00683206, 0.184441, -0.0119436, 0.179202, -0.0114876, 0.187691, -0.013167])

        names.append("LElbowRoll")
        times.append([0.68, 1.04, 1.48, 2.32, 3.28, 4.12, 5.04, 5.88, 6.84, 7.68, 8.12, 8.48, 8.8, 9.2, 9.64, 10.12, 10.6, 11, 11.44, 11.92, 12.36, 12.76, 13.2, 13.68, 14.16, 14.56, 15, 15.6, 16.2, 16.4])
        keys.append([-1.37289, -1.12923, -0.369652, -0.202446, -0.369652, -0.202446, -0.369652, -0.202446, -0.369652, -0.202446, -0.820305, -0.23305, -0.138102, -1.309, -0.257754, -1.4591, -0.138102, -1.309, -0.257754, -1.4591, -0.138102, -1.309, -0.257754, -1.4591, -0.138102, -1.309, -0.257754, -0.984366, -0.513992, -0.424876])

        names.append("LElbowYaw")
        times.append([0.68, 1.48, 2.32, 3.28, 4.12, 5.04, 5.88, 6.84, 7.68, 8.12, 8.48, 8.8, 9.2, 9.64, 10.12, 10.6, 11, 11.44, 11.92, 12.36, 12.76, 13.2, 13.68, 14.16, 14.56, 15, 15.6, 16.2, 16.4])
        keys.append([-0.65506, -0.380475, -0.618244, -0.380475, -0.618244, -0.380475, -0.618244, -0.380475, -0.618244, 0.410152, 0.818273, 0.851412, 0.0750492, 0.00157596, 0.460767, 0.851412, 0.0750492, 0.00157596, 0.460767, 0.851412, 0.0750492, 0.00157596, 0.460767, 0.851412, 0.0750492, 0.00157596, -1.34565, -1.22484, -1.21037])

        names.append("LHand")
        times.append([0.68, 1.04, 1.48, 2.32, 3.28, 4.12, 5.04, 5.88, 6.84, 7.68, 8.48, 8.8, 9.2, 9.64, 10.12, 10.6, 11, 11.44, 11.92, 12.36, 12.76, 13.2, 13.68, 14.16, 14.56, 15, 15.6, 16.2, 16.4])
        keys.append([0.2, 0.6, 0.2648, 0.264, 0.2648, 0.264, 0.2648, 0.264, 0.2648, 0.264, 0.663802, 0.928, 0.3, 0.0283999, 0.75, 0.928, 0.3, 0.0283999, 0.75, 0.928, 0.3, 0.0283999, 0.75, 0.928, 0.3, 0.5284, 0.936396, 0.950347, 0.2968])

        names.append("LShoulderPitch")
        times.append([0.68, 1.48, 2.32, 3.28, 4.12, 5.04, 5.88, 6.84, 7.68, 8.12, 8.48, 8.8, 9.64, 10.6, 11.44, 12.36, 13.2, 14.16, 15, 16.4])
        keys.append([0.97784, 1.29573, 1.40466, 1.29573, 1.40466, 1.29573, 1.40466, 1.29573, 1.40466, 0.172788, -1.04904, -1.19188, 0.995607, -1.19188, 0.995607, -1.19188, 0.995607, -1.19188, 0.995607, 1.47106])

        names.append("LShoulderRoll")
        times.append([0.68, 1.48, 2.32, 3.28, 4.12, 5.04, 5.88, 6.84, 7.68, 8.48, 8.8, 9.2, 9.64, 10.12, 10.6, 11, 11.44, 11.92, 12.36, 12.76, 13.2, 13.68, 14.16, 14.56, 15, 15.6, 16.2])
        keys.append([0.500047, 0.401871, 0.35585, 0.401871, 0.35585, 0.401871, 0.35585, 0.401871, 0.35585, 0.886453, 0.966481, 1.23332, 0.324005, 1.23332, 0.966481, 1.23332, 0.324005, 1.23332, 0.966481, 1.23332, 0.324005, 1.23332, 0.966481, 1.23332, 0.324005, 0.407503, 0.146991])

        names.append("LWristYaw")
        times.append([0.68, 1.04, 1.48, 2.32, 3.28, 4.12, 5.04, 5.88, 6.84, 7.68, 8.48, 8.8, 9.64, 10.6, 11.44, 12.36, 13.2, 14.16, 15, 16.2, 16.4])
        keys.append([0.11961, -0.289725, -0.395814, -0.420357, -0.395814, -0.420357, -0.395814, -0.420357, -0.395814, -0.420357, -0.122946, -0.107338, -0.400331, -0.107338, -0.400331, -0.107338, -0.400331, -0.107338, -0.400331, 0.000370312, 0.0827939])

        names.append("RElbowRoll")
        times.append([0.68, 1.08, 1.52, 1.92, 2.36, 2.84, 3.32, 3.72, 4.16, 4.64, 5.08, 5.48, 5.92, 6.4, 6.88, 7.28, 7.72, 8.52, 8.84, 9.68, 10.64, 11.48, 12.4, 13.24, 14.2, 15.04, 15.64, 16.24, 16.44])
        keys.append([1.34689, 1.1205, 0.138102, 1.309, 0.257754, 1.4591, 0.138102, 1.309, 0.257754, 1.4591, 0.138102, 1.309, 0.257754, 1.4591, 0.138102, 1.309, 0.257754, 0.372085, 0.369652, 0.202446, 0.369652, 0.202446, 0.369652, 0.202446, 0.369652, 0.202446, 0.82205, 0.519567, 0.429562])

        names.append("RElbowYaw")
        times.append([0.68, 1.08, 1.52, 1.92, 2.36, 2.84, 3.32, 3.72, 4.16, 4.64, 5.08, 5.48, 5.92, 6.4, 6.88, 7.28, 7.72, 8.52, 8.84, 9.68, 10.64, 11.48, 12.4, 13.24, 14.2, 15.04, 15.64, 16.24, 16.44])
        keys.append([0.59515, 0.567232, -0.851412, -0.0750492, -0.00157596, -0.460767, -0.851412, -0.0750492, -0.00157596, -0.460767, -0.851412, -0.0750492, -0.00157596, -0.460767, -0.851412, -0.0750492, -0.00157596, 0.352279, 0.380475, 0.618244, 0.380475, 0.618244, 0.380475, 0.618244, 0.380475, 0.618244, 1.26711, 1.23132, 1.21028])

        names.append("RHand")
        times.append([0.68, 1.08, 1.52, 1.92, 2.36, 2.84, 3.32, 3.72, 4.16, 4.64, 5.08, 5.48, 5.92, 6.4, 6.88, 7.28, 7.72, 8.52, 8.84, 9.68, 10.64, 11.48, 12.4, 13.24, 14.2, 15.04, 16.24, 16.44])
        keys.append([0.2, 0.95, 0.928, 0.3, 0.0283999, 0.75, 0.928, 0.3, 0.0283999, 0.75, 0.928, 0.3, 0.0283999, 0.75, 0.928, 0.3, 0.5284, 0.271478, 0.2648, 0.264, 0.2648, 0.264, 0.2648, 0.264, 0.2648, 0.264, 0.596785, 0.2976])

        names.append("RShoulderPitch")
        times.append([0.68, 1.52, 2.36, 3.32, 4.16, 5.08, 5.92, 6.88, 7.72, 8.52, 8.84, 9.68, 10.64, 11.48, 12.4, 13.24, 14.2, 15.04, 16.24])
        keys.append([0.915841, -1.19188, 0.995607, -1.19188, 0.995607, -1.19188, 0.995607, -1.19188, 0.995607, 1.281, 1.29573, 1.40466, 1.29573, 1.40466, 1.29573, 1.40466, 1.29573, 1.40466, 1.47268])

        names.append("RShoulderRoll")
        times.append([0.68, 1.08, 1.52, 1.92, 2.36, 2.84, 3.32, 3.72, 4.16, 4.64, 5.08, 5.48, 5.92, 6.4, 6.88, 7.28, 7.72, 8.52, 8.84, 9.68, 10.64, 11.48, 12.4, 13.24, 14.2, 15.04, 15.64, 16.44])
        keys.append([-0.905123, -1.30837, -0.966481, -1.23332, -0.324005, -1.23332, -0.966481, -1.23332, -0.324005, -1.23332, -0.966481, -1.23332, -0.324005, -1.23332, -0.966481, -1.23332, -0.324005, -0.397371, -0.401871, -0.35585, -0.401871, -0.35585, -0.401871, -0.35585, -0.401871, -0.35585, -0.310669, -0.174533])

        names.append("RWristYaw")
        times.append([0.68, 1.52, 2.36, 3.32, 4.16, 5.08, 5.92, 6.88, 7.72, 8.52, 8.84, 9.68, 10.64, 11.48, 12.4, 13.24, 14.2, 15.04, 16.24, 16.44])
        keys.append([-0.401949, 0.107338, 0.400331, 0.107338, 0.400331, 0.107338, 0.400331, 0.107338, 0.400331, 0.391888, 0.395814, 0.420357, 0.395814, 0.420357, 0.395814, 0.420357, 0.395814, 0.420357, 0.00501826, 0.108872])

        self.ALMotion.angleInterpolation(names, keys, times, True)

    def doHello(self):
        jointNames = ["RShoulderPitch", "RShoulderRoll", "RElbowRoll", "RWristYaw", "RHand", "HipRoll", "HeadPitch"]
        angles = [-0.141, -0.46, 0.892, -0.8, 0.98, -0.07, -0.07]
        times  = [2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0]
        isAbsolute = True
        self.ALMotion.angleInterpolation(jointNames, angles, times, isAbsolute)

        for i in range(2):
            jointNames = ["RElbowYaw", "HipRoll", "HeadPitch"]
            angles = [1.7, -0.07, -0.07]
            times  = [0.8, 0.8, 0.8]
            isAbsolute = True
            self.ALMotion.angleInterpolation(jointNames, angles, times, isAbsolute)

            jointNames = ["RElbowYaw", "HipRoll", "HeadPitch"]
            angles = [1.3, -0.07, -0.07]
            times  = [0.8, 0.8, 0.8]
            isAbsolute = True
            self.ALMotion.angleInterpolation(jointNames, angles, times, isAbsolute)


        return
    
    def blink_eyes(self, rgb):
        self.led_service.fadeRGB('AllLeds', rgb[0], rgb[1], rgb[2], 1.0)
        
    def setSpeed(self, lin_vel, ang_vel, dtime, sonar):
        self.ALMotion.move(lin_vel, 0, ang_vel)
        time.sleep(dtime)
        self.ALMotion.stopMove()
        return 

    def shutdown_robot(self):
        print("Turning off the robot")
        self.system_service.shutdown()

    def forward(self, sonar, s, lin_vel=0.2, ang_vel=0):
        print("Sonar Values", sonar.sonarValues)
        self.setSpeed(lin_vel, ang_vel, abs((s-0.5)/lin_vel), sonar)
    
    def detect_person(self, sonar):
        for i in range(len(sonar.sonarValues)):
            if sonar.sonarValues[i] <= 0.75:
                if i==0:
                    print("Person detected")
                return True
        return False

    def selectMinDistance(self, distances):
        min_distance = float("inf")
        index = 0

        for i in range(len(distances)):
            if distances[i] < min_distance:
                min_distance = distances[i]
                index = i

        return min_distance, index
    
    def move_head_down(self):
        """Look down"""
        self.ALMotion.setAngles("HeadPitch", 0.46, 0.2)