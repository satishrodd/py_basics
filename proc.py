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

sock_proc = [[0,1],[0,2],[0,3],[0,4],[0,5],[0,6],[0,7],[0,8],[0,9],[0,10]]
proc_count = 0
msg = [0,0]
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
                        to_port = output[1]
                        if from_port.split('.')[1] == str(n.raddr[1]):
#                            print from_port.split('.')[1] 
                            msg[0] = 0
                            msg[1] = 0
                            for i in sock_proc:
                                if i[0] == from_port.split('.')[1]:
                                    msg[0] = i[0]
                                    msg[1] = i[1]
                            if msg[0] == 0:
                                sock_proc[proc_count][0] = from_port.split('.')[1]
                                sock_proc[proc_count][1] = "python"
                                proc_count +=1
#                                print sock_proc[proc_count]
                            print msg
                            print sock_proc

                            
