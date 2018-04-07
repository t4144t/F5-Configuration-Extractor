global file_name
file_name="list.txt"

global lines_numbers
lines_numbers= []

def node_ip () :
    file = open(file_name,"r")
    lines = file.readlines()
    #print lines[26]
    file.close()

    # look fot patterns
    count = 0
    
    print ("====================================")
    print ("Nodes IPs:")
    print ("====================================")
    
    for num, line in enumerate(lines, 1):

        if "ltm node" in line:

            lines_numbers.append(num)
    
    i=0
    while i < len(lines_numbers):
        z=lines_numbers[i]
        m=lines[z].split()
        print m[1]
        i=i+1

    
        
def node_name () :
    print ("====================================")
    print ("Nodes Names:")
    print ("====================================")
    file = open(file_name,"r")
    lines = file.readlines()
    #print lines[26]
    file.close()
    count =0
    for line in lines:

            if "ltm node" in line:
                line=line.split("node")[1]
                x=line.split(" ")[1]
                count = count + 1
                print x
    print count

def vip_name () :
    print ("====================================")
    print ("Virtual Servers Names:")
    print ("====================================")
    file = open(file_name,"r")
    #global lines
    lines = file.readlines()
    #print lines[26]
    #file.close()
    counter=0
    
    for num, line in enumerate(lines, 1):

            if "ltm virtual" in line:
                
                line=line.split("virtual")[1]
                x=line.split(" ")[1]
                lines_numbers.append(num)
                counter=counter+1
                print x
                #print counter

def vip_ip () :

    print ("====================================")
    print ("Virtual ServerS IPs:")
    print ("====================================")
    file = open(file_name,"r")
    lines = file.readlines()
    i= 0
    z=0
    n=0
    k=0
    counter=0
    while i < len(lines_numbers):
        z=lines_numbers[i]
        #print z
        i=i+1
        m=lines[z].split()
        if m[0] == "destination":
            q=m[1]
            q=q.split(":")
            print q[0]
        if m[0] == "description":
            z=z+1
            d=lines[z].split("destination")[1]
            u=d.split(":")
            
            print u[0]


node_ip()
node_name()
vip_name()
vip_ip()

