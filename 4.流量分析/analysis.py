from scapy.all import *

if __name__ == "__main__":
    pcap = rdpcap('./aim.pcap')
    for item in pcap:
        if ('TCP' in item) and ('IP' in item):
            src = item['IP'].fields['src']
            dst = item['IP'].fields['dst']
            sport = item['TCP'].fields['sport']
            dport = item['TCP'].fields['dport']
            if (src == "192.0.123" and sport == 80) or (dst == "192.168.0.123" and dport == 80):
                print(repr(item))

flag-{YKLTGULRGB}