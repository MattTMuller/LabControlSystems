# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 15:45:46 2023

@author: Microprobe_Station
"""

from IET7600PlusControl import IET7600Plus
import numpy as np
import time
from PTC10Control import PTC10Control
from EZTControl import EZTControl
import re
from KeithleyControl import Series2400SourceMeter




class PID:
    def __init__(self, Kp, Ki, Kd):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.error_sum = 0
        self.last_error = 1 #error used for delta error
        self.prev_error = 0 #error used in steady state

    def update(self, current_value, set_value, dt):
        error = set_value - current_value
        self.error_sum += (self.Ki *error) * dt
        derivative = self.Kd * (error - self.last_error) / dt
        output = (self.Kp *error) + self.error_sum + derivative
        self.prev_error = self.last_error
        self.last_error = error
        
        return output

def regulate_temperature(current_temperature, set_temperature):
    pid = PID(Kp=1, Ki=0, Kd=0)
    ptc10 = PTC10Control('169.254.106.21')
    ezt = EZTControl('169.254.106.15')
    dt = 0.1
    tolerance = 0.1  # temperature tolerance
    new_temperature = 0;
    ptc10.temperature_setpoint(set_temperature)
    ptc10.enable_output()
    ezt.enable_temperature_manual_mode()
    max_iteration = 2000
    iteration = 0
    
    while iteration < max_iteration:
        pid_output = pid.update(current_temperature, set_temperature, dt)
        # Apply the PID output to regulate the temperature
        ezt.set_temperature_SP(pid_output)
        # Get the new temperature
        ptc10.update_outputs()
        new_temperature = ptc10.outputs[1]
        current_temperature = new_temperature
        if abs((set_temperature - current_temperature)*dt) < tolerance:
            break
        time.sleep(dt)
        iteration += iteration
    


regulate_temperature(0,20)

# ptc10.temperature_setpoint(20)
# iteration = 0

# for x in range(20):
#     ptc10.update_outputs()
#     if ptc10.outputs[1] != 20:
#         print('Temp is', ptc10.outputs[1], 'at time =', time.ctime())
#         time.sleep(5)
#         iteration = iteration + 1;
#     else:
#         break


    
# ptc10.enable_output()
# ptc10.update_outputs()
# ezt.enable_temperature_manual_mode()
# ptc10.disable_output()


