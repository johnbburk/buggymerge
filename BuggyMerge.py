import csv
import os

os.system('/Applications/googlecl-0.9.13/build/scripts-2.7/google docs get CVPMProgramResponses --format csv /Users/jburk/Dropbox/_archive/_Teaching/_SAS\ Teaching/Courses/Honors\ Physics\ 13-14/01-CVPM/Python')
reader = csv.reader(open("CVPMProgramResponses.csv", 'U'))
data=[]

rowcount=0
for row in reader:
	data.append(row)
	rowcount=rowcount+1

colors=["red","green","blue","yellow","orange","magenta"]
	
i=1

f = open("block1.py")

g = open("merge.py","w")
h = open("mergerace.py","w")

g.write(f.read())
f.seek(0)
h.write(f.read())

#put in code to add buggy objects here

while i < rowcount:
	g.write("car"+str(i)+"=box(size=(.3,.1,.2), color = color."+colors[i]+")\n")
	h.write("car"+str(i)+"=box(size=(.3,.1,.2), color = color."+colors[i]+")\n")
	i=i+1

i=1
	
f = open("block2.py")
g.write(f.read().replace("%count",str(rowcount-1)))
f.seek(0)
h.write(f.read().replace("%count",str(rowcount-1)))

#compute z offset
offsetStart=-(rowcount-1)/2*0.3

while i<rowcount:
	g.write("\ncar"+str(i)+".m=1\n") #set mass
	h.write("\ncar"+str(i)+".m=1\n")
	
	posprompt="car"+str(i)+".pos"+data[i][1][8:]+"\n"
	pospromptZs=posprompt.find(",0,")+3
	pospromptZf=posprompt.find(")")
	
	posprompt=posprompt[:pospromptZs]+str(offsetStart+(i)*0.3)+posprompt[pospromptZf:]
	
	g.write(posprompt) #set position
	
	#rewrite position prompt so that starting x position is 0
	pospromptS=posprompt.find("vector(")+7
	pospromptE=posprompt.find(",")
	
	h.write(posprompt[:pospromptS]+"0"+posprompt[pospromptE:])#change the x position to 0
	
	vprompt="car"+str(i)+".v"+data[i][2][6:]+"\n"
	g.write(vprompt)#set velocity
	h.write(vprompt.replace("-",""))  #make all velocities positive
	
	i=i+1


i=1
f = open("block3.py")
g.write(f.read())
f.seek(0)
h.write(f.read())

#loop stuff here



while i< rowcount:
	g.write("    car"+str(i)+".v = car"+str(i)+".v + Fnet/"+"car"+str(i)+".m * deltat\n")#velocity update
	h.write("    car"+str(i)+".v = car"+str(i)+".v + Fnet/"+"car"+str(i)+".m * deltat\n")#velocity update
	i=i+1


g.write("\n    #Position update \n")
h.write("\n    #Position update \n")
i=1	
while i< rowcount:
	g.write("    car"+str(i)+".pos = car"+str(i)+".pos+"+"car"+str(i)+".v * deltat\n")#position update
	h.write("    car"+str(i)+".pos = car"+str(i)+".pos+"+"car"+str(i)+".v * deltat\n")#position update
	i=i+1
i=1

#loop
f = open("block4.py")
g.write(f.read())
f.seek(0)
h.write(f.read())

#graph update here
string ="t"
while i<rowcount:
	string=string+",car"+str(i)+".pos.x"
	i=i+1

i=1

tstring="    positiongraph.plot("+string+")\n"
g.write(tstring)	
h.write(tstring)


f = open("block5.py") 
g.write(f.read())
f.seek(0)
h.write(f.read())
g.close()
h.close()
