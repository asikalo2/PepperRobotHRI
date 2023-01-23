import time

class Touch:
    def __init__(self, memory_service):
        self.memory_service = memory_service
        self.sensors = {'HeadMiddle': 'Device/SubDeviceList/Head/Touch/Middle/Sensor/Value' ,
                        'LHand':      'Device/SubDeviceList/LHand/Touch/Back/Sensor/Value' ,
                        'RHand':      'Device/SubDeviceList/RHand/Touch/Back/Sensor/Value' }

        
    def isTouched(self, sensor):
        try:
            sensor_key = self.sensors[sensor]
            print("Touching %s ..." %sensor)
            self.memory_service.insertData(sensor_key,1.0)
            time.sleep(2)
            self.memory_service.insertData(sensor_key,0.0)
            print("Touching %s ... done" %sensor)
            return True
        except:
            print("ERROR: Sensor %s unknown" %sensor)
            return False