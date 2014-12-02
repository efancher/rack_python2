#!/usr/bin/env python
#!*-* coding:utf-8 *-*
"""
Usage: 
    lab05_subprocess.py --commands COMMAND...

"""
import subprocess
import platform
import docopt

#a
print("a")
subprocess.call(["/usr/bin/ls", "-l"], stdout=None)

#b
print("b")
sp = subprocess.Popen(["/usr/bin/ls", "-l"], stdout=None)


#c
try:
    sp = subprocess.Popen(["/bogus/command"], stdout=None) 

    print("return code: {0}".format(sp.return_code))
except:
    pass


#d
if "centos" in (platform.platform()) or "redhat" in (platform.platform()):
    subprocess.call(["yum", "search", "gcc"], stdout=None)    
else:
    subprocess.call(["apt-get", "search", "gcc"], stdout=None)

#e
import pipes
t = pipes.Template()

sp = subprocess.Popen(["du", "/home/", "-h", "--max-depth=1"], 
                        stdout=subprocess.PIPE)
for line in sp.stdout.readlines():
    print "read line {0} from sub process".format(line)
#f
if __name__ == "__main__":
    arguments = docopt.docopt(__doc__)    
    print(arguments)
    for command in arguments["COMMAND"]:
        command = command.split()
        sp = subprocess.Popen(command, stdout=None)
    
