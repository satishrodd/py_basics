import psutil

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
        nets = psutil.net_connections(kind = 'inet4')
        for n in nets:
            if n.pid == proc.pid and n.status == 'LISTEN':
                #get the ports
                print(n.pid, p.name())
