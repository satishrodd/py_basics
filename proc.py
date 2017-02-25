import psutil
import socket
import subprocess
import ast

#proc is a class,which will store the 
#process name, id and the ports associated with it
class proc:
    def __init__(self):
        self.name = 'default'
        self.pid = 0;

for proc in psutil.process_iter():
    #get the process
    p  = psutil.Process(proc.pid)
    if p.name() == 'python':
        #get all the network connections
        while True:
            nets = psutil.net_connections(kind = 'inet4')
            for n in nets:
                if n.pid == proc.pid and n.status == 'ESTABLISHED':
                    #get the ports
                    print(n)
                    pr = subprocess.Popen(['tcpdump', '-q', '-l', '-i', 'lo', 'port', str(n.laddr[1])],
                                          stdout=subprocess.PIPE)
                    for row in iter(pr.stdout.readline, b''):
                        output =  row.rstrip().split(' ')
                        from_port = output[2]
                        if from_port.split('.')[1] == str(n.raddr[1]):
                            print from_port.split('.')[1]
#                    out = p.commnicate()
#                    print out
