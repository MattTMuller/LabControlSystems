# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 09:23:46 2022

@author: Microprobe_Station
"""

import serial
import time

#frequency is units of Hz and has range of 10 to 2000000 (2MHz)
#voltage is units of V and has range of 0.02V to 5V
#current is units of A and has a range of 0.000250 microamps to 0.1 A


#%%
class IET7600Plus:
    def __init__(self, com_port:str='COM1'):
        
        """Attempt to make connection with device"""
        
        self.com_port = com_port
        
        print(f"Connecting to IET device at: {self.com_port}")
        self.ser = serial.Serial(com_port, 9600, timeout=1,
                                parity=serial.PARITY_NONE,
                                stopbits=serial.STOPBITS_ONE,
                                bytesize=serial.EIGHTBITS,
                                )
        print(f"Connected to IET device at: {self.com_port}")
            
        #self.measure_data() #prime the IET register with data
        # except:
        #     print(f"Failed to connect to host at: {self.com_port}")
        
        
    def __del__(self):
        
        """Destructor -- Close the port in after the program has finished running"""

        print(f"Closing IET7600 at: {self.com_port}")
        self.ser.close()
        print(f"Successfully Closed IET7600 at: {self.com_port}")
        
        
        
    def _send_command(self, command:str):
        
        """Send a telnet command to the IET"""
        
        message = command + "\n"
        self.ser.write(message.encode())
        
    def _read_data(self):
        
        """Reads serial response
        
        Note: this function should not be used for responseless commands as
        it will wait and read untill the device responds"""
        
        data = self.ser.read_until(b'\n').decode("utf-8")
        return data
    
    def measure_data(self,measurement_dalay:float = 1):
        
        """""Function:
            
            Send request for device to measure a value, send the value over
            the serial connection. Function will return 
            
            Parameters:
                measurement_delay: delay between read time, minimum of 0.5
                seconds is required."""
            
        time.sleep(measurement_dalay)
        self._send_command('MEAS')
        self._send_command('FETC?\n')
        return self._read_data()

    
    #configure
    def set_frequency(self, frequency:int):
        """Function:
            Set the frequency from 10 to 2000000 Hz
            
        Parameters:
            0000000.00 
                """
                
        self._send_command(f'conf:freq {frequency}')
        
    def set_primary_param(self,parameter:str):
        """Function:
            Set the primary parameter
            
        Parameters:
            A(auto) CS CP LS 
            LP RP RS DF Q Z Y 
            P(phase angle) ESR 
            GP XS BP
        """
        
        self._send_command(f'conf:ppar {parameter}')
            
    def set_secondary_param(self, parameter):
        
        """Function:
            Set the secondary parameter
            
        Parameters:
            N(none) CS CP LS 
            LP RP RS DF Q Z Y 
            P(phase angle) ESR 
            GP XS BP    
        """
        
        self._send_command(f'conf:spar {parameter}')
        
    def set_AC_test_type(self, test:str):
        
        """Function:
            Set the AC test signal type.
            
        Note: This should be set prior to setting the AC Value
        
        Parameters:
            
            test: Voltage (V) or Current (I)"""
            
        self._send_command(f'conf:acty {test}')
        
    def set_AC_signal_value(self, value:float):
        
        """Function:
            Set the AC signal toa specified value
            
        Parameters:
            floating point value, if AC test signal is set to 
            voltage then AC signal is between 0.02 and 5
            if AC signal is set to current then AC signal is between 
            0.000250 and 0.1"""

        self._send_command(f'conf:acv {value}')
            
    def set_bias(self, bias:str):
        """Function:
            Set the bias
            
        Parameters:
            INT EXT or OFF
            """
        
        self._send_command(f'conf:bias {bias}')
            
    def set_range(self, ran:str):
        """Function:
            Set the range
            
        Parameters:
            ATUTO HOLD or #(1-59)"""
        
        self._send_command(f'rang:conf {ran}')
        
    def set_meas_accuracy(self, accuracy:str):
        """Function:
            Set the measurement accuracy
        Parameters:
            SLO MED FAS
            """
            
        self._send_command(f'conf:mac {accuracy}')
        
    def set_meas_delay(self, delay:int):
        
        """Function:
            
        Parameters:
            
            """
        self._send_command(f'conf:tdel {delay}')
        
    def set_num_avg(self, average:int):
        
        """Function:
            
        Parameters:
            
            """
        self._send_command(f'conf:aver {average}')
        #self.measure_data()
        
    # def set_med_fncn(self):
                
    #     """Function:
            
    #     Parameters:
            
    #         """
    # def set_distortion(self):
                
    #     """Function:
            
    #     Parameters:
            
    #         """
    # def set_contact_check(self):
                
    #     """Function:
            
    #     Parameters:
            
    #         """
    # def set_disp_type(self):
                
    #     """Function:
            
    #     Parameters:
            
    #         """
    # def set_trigger(self):
                
    #     """Function:
            
    #     Parameters:
            
    #         """
    # def set_nominal(self):
                
    #     """Function:
            
    #     Parameters:
            
    #         """
    # #Binning
    
    # def set_bin_limit(self, bin_number, ):
                
    #     """Function:
            
    #     Parameters:
            
    #         """
    # def set_bin_tolerance(self, bin_number,):
                
    #     """Function:
            
    #     Parameters:
            
    #         """
    # def set_secondary_bin_limit(self, bin_number,):
                
    #     """Function:
            
    #     Parameters:
            
    #         """
    # def reset_bin(self, bin_number,):
                
    #     """Function:
            
    #     Parameters:
            
    #         """
    # def summary(self, bin_number,):
                
    #     """Function:
            
    #     Parameters:
            
    #         """
    # def set_bin_result_format(self):
                
    #     """Function:
            
    #     Parameters:
            
    #         """
    # def set_bin_handler_port(self):
                
    #     """Function:
            
    #     Parameters:
            
    #         """
    # def bin_print_result(self):
                
    #     """Function:
            
    #     Parameters:
            
    #         """
    # def bin_file_to_usb(self):
                
    #     """Function:
            
    #     Parameters:
            
    #         """
    # def bin_file_duplicate(self):
                
    #     """Function:
            
    #     Parameters:
            
    #         """
    # def bin_file_new(self):
                
    #     """Function:
            
    #     Parameters:
            
    #         """
    # def bin_file_append(self):
                
    #     """Function:
            
    #     Parameters:
            
    #         """
    # def bin_close(self):
                
    #     """Function:
            
    #     Parameters:
            
    #         """
    # def sweep_parameter(self):
                
    #     """Function:
            
    #     Parameters:
            
    #         """
    # def sweep_begin(self):
                
    #     """Function:
            
    #     Parameters:
            
    #         """
    # def sweep_end(self):
                
    #     """Function:
            
    #     Parameters:
            
    #         """
    # def sweep_step(self):
                
    #     """Function:
            
    #     Parameters:
            
    #         """
    # def sweep_display(self):
                
    #     """Function:
            
    #     Parameters:
            
    #         """
    # def sweep_enable(self):
                
    #     """Function:
            
    #     Parameters:
            
    #         """
    # def sweep_valid(self):
                
    #     """Function:
            
    #     Parameters:
            
    #         """
    
    # def file_save(self, method):
                
    #     """Function:
            
    #     Parameters:
            
    #         """
    # def file_recall(self):
                
    #     """Function:
            
    #     Parameters:
            
    #         """
    # def file_valid(self):
                
    #     """Function:
            
    #     Parameters:
            
    #         """
    # def sequence_ebable(self):
                
    #     """Function:
            
    #     Parameters:
            
    #         """
    # def sequence_test(self):
                
    #     """Function:
            
    #     Parameters:
            
    #         """
    # def sequence_frequency(self):
                
    #     """Function:
            
    #     Parameters:
            
    #         """
    # def sequence_primary_parameter(self):
                
    #     """Function:
            
    #     Parameters:
            
    #         """
    # def sequence_second_parameter(self):
                
    #     """Function:
            
    #     Parameters:
            
    #         """
        
        
        
 