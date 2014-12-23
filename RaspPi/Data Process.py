import serial
from time import gmtime, strftime
from datetime import datetime
import socket
from detect_peaks import detect_peaks
import numpy as np

data = [];
#list_length = 400;
list_length = 1500;
pulse = 60;
newpulse = 0;
distances = 0;
peaks = 0;
filt_dist = 0;

#setup remote address and port
UDP_IP = 'oliverbonner.myds.me';
UDP_PORT = 57683;

# ser = serial.Serial('/dev/ttyACM0', 9600);
ser = serial.Serial('/dev/tty.usbmodem1451', 9600);

#init UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM);

#return the latest byte of data from serial port (in number form)
def GetSerial():
    return ord(ser.read());

while 1:
    #check for packet header = 65535
    if GetSerial() == 255:
        if GetSerial() == 255:
            CurTempVoltage = (GetSerial() * 256) + GetSerial();

            CurPulse = (GetSerial() * 256) + GetSerial();
            
            if len(data) > list_length:
                data.pop(0);
    
            data.append(CurPulse);
            
            #apply calibration fit (round to 1 DP)
            CurTemp = round(((0.0476 * CurTempVoltage) - 3.5764),1);
                        
            if len(data) > (list_length - 1):
                data_processed = np.asarray(data);
                peaks = detect_peaks(data_processed, show=False, mpd=10);
                
                if len(peaks) > 4:
                    distances = np.diff(peaks);
                    filt_dist = filter(lambda x: 20 < x < 60, distances);
                    strip(filt_dist);
                    mean = np.mean(filt_dist);
                    newpulse = 60 / (mean * 0.025);
            
            if newpulse < 140 and newpulse > 40:
                pulse = newpulse;
            
            print str(filt_dist) + " ; " + str(pulse);
            
            ToWrite = str(CurTemp) + ',' + str(int(pulse)) + ',' + strftime("%H:%M:%S", gmtime()) + '.' + str(datetime.now().microsecond / 10000);            
                
            sock.sendto(ToWrite, (UDP_IP, UDP_PORT));
                
            ser.flushInput();
            
