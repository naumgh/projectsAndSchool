#Naum Hoffman
#VOO927502

from base64 import decode
from importlib.util import MAGIC_NUMBER
from multiprocessing import connection
from re import L
from sqlite3 import connect
import struct
import sys
import packet_struct

#here is our first class, we need to grab the header from what ever we just revieved from pcap file

endian = ">"

class a2:
    def __init__(self, Globheader = (), 
    pkt_header = (), pkt_data = (), packet = {}, packetDetails = {}, startTime = 0, endTime = 0, status = ""
    ,duration_connection = 0, PacketsEast = 0, PacketsWest = 0, totalPackets = 0, dataBytesEast = 0,
    dataBytesWest = 0, recetTcp = 0, openTcp = 0, count = 0, incl_len = 0, sourceip = 0, sourceport=0, destip = 0, destport=0):
        self.Globheader = Globheader
        self.pkt_header = pkt_header
        self.status = status
        self.pkt_data = pkt_data
        self.packet = packet
        self.count = count
        self.incl_len = incl_len
        self.startTime = startTime
        self.endTime = endTime
        self.duration_connection = duration_connection
        self.PacketsEast = PacketsEast
        self.PacketsWest = PacketsWest
        self.totalPackets = totalPackets
        self.dataBytesEast = dataBytesEast
        self.dataBytesWest = dataBytesWest
        self.recetTcp = recetTcp
        self.openTcp = openTcp
        self.sourceip = sourceip
        self.sourceport = sourceport
        self.destip = destip
        self.destport = destport
        self.packetDetails = packetDetails
         

    def unpackHead(self,globalHead):
        ''' 
        Global Header
    typedef struct pcap_hdr_s {
            guint32 magic_number;   /* magic number  4 bytes*/
            guint16 version_major;  /* major version number 2 bytes */
            guint16 version_minor;  /* minor version number 2 bytes */
            gint32  thiszone;       /* GMT to local correction 4 bytes */
            guint32 sigfigs;        /* accuracy of timestamps 4 bytes */
            guint32 snaplen;        /* max length of captured packets, in octets 4 bytes */
            guint32 network;        /* data link type 4 bytes*/
    } pcap_hdr_t;
        '''

        if globalHead[:2] == b"\xa1\xb2":
            endian = ">"      #BIG ENDIAN
        elif globalHead[:2] == b"\xd4\xc3":
            endian = "<"      #LITTLE ENDIAN

        cap_head = struct.unpack(endian+ "IHHIIII", globalHead[:24])
        magic_number = cap_head[0]
        version_major = cap_head[1]
        version_minor = cap_head[2]
        thiszone = cap_head[3]
        #print("this zone ",thiszone)
        sigfigs = cap_head[4]
        snaplen = cap_head[5]
        network = cap_head[6]

        self.Globheader = cap_head

        return(cap_head)

    '''
    Packet Header
    •typedef struct pcaprec_hdr_s {
    •        guint32 ts_sec;         /* timestamp seconds */
    •        guint32 ts_usec;        /* timestamp microseconds */
    •        guint32 incl_len;       /* number of octets of packet saved 
    in file */
    •        guint32 orig_len;       /* actual length of packet */
    •} pcaprec_hdr_t;
    '''
    def unpackPackHead(self,packet_head):
        #print(packet_head)
        if packet_head == b'':
            return "END"
        unpacked_head = struct.unpack("IIII", packet_head[:16])
        #print(unpacked_head)
        ts_sec = unpacked_head[0]
        ts_usec = unpacked_head[1]
        incl_len = unpacked_head[2]
        orig_len = unpacked_head[3]

        self.incl_len = incl_len
        #print("timestamp seconds ", ts_sec)
        #print("timestapm micro ", ts_usec)
        #print("actual length packet ", orig_len)

        self.pkt_header = unpacked_head
        return self.pkt_header
        


    '''
    Ethernet Header
    bytesName
    6 Destination MAC address
    6 Source MAC address
    2 Ethernet Type


    IPV4 Header     (minimum 20 bytes)
    4 bits IP Version Number (4)
    4 bits IHL (IP HEADER LENGTH)
    8 bits Type of Service
    16 bits Total Length
    16 bits Identification
    4 bits Flags
    12 bits Fragment Offset
    8 bits Time to Live
    8 bits Protocol
    16 bits Header Checksum
    32 bits Source Address
    32 bits Destination Address
    '''


    def getPackData(self,packData):
        #print("here is pack data ",packData)
        etherHead = struct.unpack("!6s6sH", packData[:14]) #I dont think we care about this
        #print()
        #print(etherHead)

        #we only wannt tcp so we only get tcp
        
        ip_head = struct.unpack('!BBHHHBBHII', packData[14:14+20]) #minimum 20 byte for iphead
        #print("here is ip head ",ip_head)

        if ip_head[6] != 6:                                         #we assume only tcp
         #   print("this is not tcp, we dont count it")
            #I HAVE TO HANDLE THIS LATER, WE ARE ONLY LOOKING AT TCP!
            return

        #print(ip_head[7])

        source_ip = ip_head[8]                                              #now, we need to get the source and dest ips       
        dest_ip = ip_head[9]
        #something is wrong here we dont get ip
        source_ip = self.convertIP(source_ip)
        dest_ip = self.convertIP(dest_ip)

        IHL = (ip_head[0] & 0x0f) * 4        
        #print(IHL)
        data_offset = 14 + IHL
        tcp_head = struct.unpack('!HHIIBBHHH', packData[data_offset:data_offset+20])
        tcp_size = ((tcp_head[4] & 0xf0) >> 4) * 4
        #print("here is tcp head ", tcp_head)
        #print(tcp_size)
        #print(source_ip)
        #print(dest_ip)
        self.sourceip = source_ip
        self.sourceport = tcp_head[0]
        self.destip = dest_ip
        self.destport = tcp_head[1]
        
        flag = True
        

    def convertIP(self, source_ip):
        source_ip = "%d.%d.%d.%d" % ((source_ip & 0xff000000) >> 24, (source_ip & 0x00ff0000) >> 16, (source_ip & 0x0000ff00) >> 8, source_ip & 0x000000ff)
        #print(source_ip)
        return source_ip

    #first, we open the binary file using rb, and read first 24 byes of data

    def printAll(self):
        sourceaddra = []
        sourceportarr = []
        destionationaddra = []
        destinationportarr = []


        #for key in self.packet:
         #   print("here is the dicitonary ", key, " ",self.packet[key])



        #for key in self.packetDetails:
          #  print("here is packetDetails ", key, " ",self.packetDetails[key])

        #HERE WE PRINT TOTAL NUMBER OF CONNECTIONS:
        print("A) Total Number of connections: ", int(self.count/2))
        print("______________________________________________________")
        print("B) Connection details\n")

        
        #for x in range(1, int((self.count)/2) + 1):
         #   print("Connection ", x,":")

        


    def main(self):
        filename = sys.argv[1]
        try:
            with open(filename, "rb") as f:
                globalHead = f.read(24)
               # print(globalHead)
                cap_head = self.unpackHead(globalHead)
                #print(cap_head)

                
                while True:
                    packet_head = f.read(16)
                    end = self.unpackPackHead(packet_head)
                 #   print(end)
                    if end == "END":
                        return self.printAll()
                    packData = f.read(self.incl_len)
                    self.getPackData(packData)
                    connectionTuple = (self.sourceip,self.sourceport,self.destip,self.destport)
                    if connectionTuple not in self.packet.values():    
                        self.count += 1
                        self.packet[self.count] = connectionTuple   
                    else:
                        if connectionTuple not in self.packetDetails:    
                            self.packetDetails[connectionTuple]=1
                        else:
                            self.packetDetails[connectionTuple] += 1

                    

                        
        except FileNotFoundError:
            print("please provide a real file")
            return

        


pcap = a2()
pcap.main()
















'''
def openAndParse(self):
        print(self.fp)
        with open(self.fp, 'rb') as f:
            byte = f.read(1)
            while byte:
                print(byte)
                byte = f.read(1)




class GlobalHeader:
    magic_number = None
    version_major = None
    version_minor = None
    thiszone = None
    sigfigs = None 
    snaplen = None
    network = None
    
    def __init__(self, magic_number, version_major, timezone, sigfigs, snaplen, network):
        self.magic_number = magic_number
        self.version_major=version_major
        self.timezone = timezone
        self.sigfigs=sigfigs
        self.snaplen=snaplen
        self.network=network
'''


