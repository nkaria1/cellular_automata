#Authour: Niharika Karia
#Creation date: 31-Jan-2017
#Objective: Given a rule, we construct Next Row by applying the rule to the Prev Row. while at the same time saving information about the location of a pattern in the entire matrix which can be retrived later. 

import numpy as np

class Rule30Class:
	
	def __init__(self, left,center,right):
		self.l,self.c,self.r=left,center,right
	# using rule 30: http://www.wolframscience.com/nksonline/page-53
		if (self.l==1 and self.c==1 and self.r==1 ):
			self.v=0
		elif (self.l==1 and self.c==1 and self.r==0 ):	
			self.v=0
		elif (self.l==1 and self.c==0 and self.r==1 ):	
			self.v=0
		elif (self.l==0 and self.c==1 and self.r==1 ):	
			self.v=1
		elif (self.l==1 and self.c==0 and self.r==0 ):
			self.v=1	
		elif (self.l==0 and self.c==1 and self.r==0 ):
			self.v=1	
		elif (self.l==0 and self.c==0 and self.r==1 ):
			self.v=1	
		elif (self.l==0 and self.c==0 and self.r==0 ):
			self.v=0	
	

class SixValuePattern:
	
	def __init__(self, Tleft,Tcenter,Tright, Bleft,Bcenter,Bright):
		self.tl,self.tc,self.tr,self.bl,self.bc,self.br=Tleft,Tcenter,Tright,Bleft,Bcenter,Bright

class location:
	def __init__(self, pattern):
		self.pat=pattern
		self.pos=[]

	def set_pattern_occurrencies(self, pattern, coord):
		self.pos.append(coord)
	
def get_pattern_occurrencies(pattern, pattern_map):
		return pattern_map.pos

def check_pattern(pattern_1,next_row,prev_row):
	x,y=1,0
	return x,y

def new_row(instance_of_rule30, prev_row, pattern_map):
	next_row=[-1]*len(prev_row)
	for i in range(1,len(prev_row)-1):
		instance_of_rule30=Rule30Class(prev_row[i-1],prev_row[i],prev_row[i+1])
		next_row[i]=instance_of_rule30.v
	next_row[0],next_row[len(prev_row)-1]=next_row[len(prev_row)-2],next_row[1]
	
	for k in range (2,len(next_row)):
		#check pattern 1 and set coord into map
		x,y=check_pattern(pattern_1,next_row,prev_row)
		#print pattern_map.pat.tl, pattern_map.pat.tc, pattern_map.pat.tr, pattern_map.pat.bl, pattern_map.pat.bc, pattern_map.pat.br
		if (pattern_map.pat.tl==prev_row[k-2] and pattern_map.pat.tc==prev_row[k-1] and pattern_map.pat.tr==prev_row[k] and pattern_map.pat.bl==next_row[k-2] and pattern_map.pat.bc==next_row[k-1] and pattern_map.pat.br==next_row[k]):
			pattern_map.set_pattern_occurrencies(pattern_1, [k-1,j+1])
	return next_row,pattern_map


print ("Taking user input for the pattern to be searched")
TL=input("enter the Top Left value for pattern: ")
TC=input("enter the Top Center value for pattern: ")
TR=input("enter the Top Right value for pattern: ")
BL=input("enter the Bottom Left value for pattern: ")
BC=input("enter the Bottom Center value for pattern: ")
BR=input("enter the Bottom Right value for pattern: ")
pattern_1=SixValuePattern(TL,TC,TR,BL,BC,BR)
pattern_map=location(pattern_1)
fr=np.genfromtxt('first_row.csv',delimiter=",")
prev_row=fr.tolist()
print map(int, prev_row)
instance_of_rule30=Rule30Class(prev_row[1],prev_row[2],prev_row[3])
for j in range(0,99):
	next_row,pattern_map=new_row(instance_of_rule30, prev_row, pattern_map)
	print next_row
	prev_row=next_row
pattern_cord=get_pattern_occurrencies(pattern_1, pattern_map)
print ("Displaying the co-ordinates of the location where the pattern %d-%d-%d/%d-%d-%d was found:") %(TL,TC,TR,BL,BC,BR)
print pattern_cord

print ("Have a happy day")
