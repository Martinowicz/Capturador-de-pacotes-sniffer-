 
import pyshark
i = 1 
cap = pyshark.LiveCapture(interface = 'Ethernet') 
cap.sniff (packet_count = 10) 
for pkt in cap:
	print(pkt) 

        
