import socket
import threading
import time

#thread class to read data from UDP port
class DataReadThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self);
    def run(self):
        while thread_stop != 1:
            #read data from socket
            data, addr = sock.recvfrom(1024); # buffer size is 1024 bytes
    
            #split incoming data
            splitdata = data.split(",");
            temperature = splitdata[0];
            pulse = splitdata[1];
            time = splitdata[2];
            
            #open file then write pulse
            pulse_file = open('/volume1/web/pulse.txt', 'w');
            pulse_file.write(pulse + "," + time);
            
            #close file
            pulse_file.close();

            #open file then write temperature
            temp_file = open('/volume1/web/temperature.txt', 'w');
            temp_file.write(temperature + "," + time);
    
            #close file
            temp_file.close();

#define port to listen to
UDP_PORT = 57683;

#define socket parameters
sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM); # UDP
#bind socket to listen port (don't care about incoming IP)
sock.bind(('', UDP_PORT));

#init the 'quitting' variables to zero
thread_stop = 0;
quit = 0;

#init the thread
DataRead = DataReadThread();    

DataRead.start();
        
#start the main loop - stop threads then quit on 'x'
while quit != 1:
    user_input = raw_input('to quit type "x": ');
    if user_input == 'x':
        thread_stop = 1;
        time.sleep(0.5);
        quit = 1;
