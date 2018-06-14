#!/usr/bin/env python

import argparse
import sys
import socket
import random
import struct

from scapy.all import sendp, send, hexdump, get_if_list, get_if_hwaddr
from scapy.all import Packet, IPOption
from scapy.all import Ether, IP, UDP
from scapy.all import IntField, FieldListField, FieldLenField, ShortField
from scapy.layers.inet import _IPOption_HDR

from time import sleep

def get_if():
    ifs=get_if_list()
    iface=None # "h1-eth3"
    for i in get_if_list():
        if "eth0" in i:
            iface=i
            break;
    if not iface:
        print "Cannot find eth0 interface"
        exit(1)
    return iface

def main():

    if len(sys.argv)<4:
        print 'pass 2 arguments: <destination> "<message>" <duration>'
        exit(1)

    addr = socket.gethostbyname(sys.argv[1])
    iface = get_if()

    pkt = Ether(src=get_if_hwaddr(iface), dst="3c:fd:fe:05:de:80") / IP(dst=10.10.2.2, tos=1) / UDP(dport=4321, sport=1234) / "0006ea6826337d05cfa8b38615d6ea7a"
    pkt.show2()
    #hexdump(pkt)
    try:
      for i in range(int(sys.argv[100])):
        sendp(pkt, iface=iface)
        sleep(1)
    except KeyboardInterrupt:
        raise


if __name__ == '__main__':
    main()