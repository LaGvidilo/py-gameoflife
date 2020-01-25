#coding: utf-8

from PIL import Image
from copy import copy

class gol(object):
	def __init__(self,size=(512,512),name="gol_img/TEST"):
		self.size = size
		self.plan = [0] * (size[0]*size[1])
		self.posindx = {}
		i=0
		for x in range(0,size[0]):
			self.posindx[x] = {}
			for y in range(0,size[1]):
				self.posindx[x][y] = i
				i+=1
		self.itt = 1
		self.name = name

	def cutpart(self,posx,posy):
		cubepos = [self.posindx[posx-1][posy-1],self.posindx[posx-1][posy],self.posindx[posx][posy-1],self.posindx[posx+1][posy],self.posindx[posx+1][posy+1],self.posindx[posx][posy+1],self.posindx[posx+1][posy-1],self.posindx[posx-1][posy+1]]
		pl = []
		for j in cubepos:
			pl.append(self.plan[j])

		actual = self.plan[self.posindx[posx][posy]]

		if actual == 0:
			if pl.count(1) == 3:
				self.setter_diff(posx,posy)#born
				#print("born")
		else:
			#print(pl.count(1),"--")
			if (pl.count(1) == 2) or (pl.count(1) == 3):
				self.setter_diff(posx,posy)#survive
				#print("survive")
			else:
				self.setter_diff(posx,posy,0)
				#print("death")

	def display(self):
		image = Image.new("RGB", self.size)
		for x in range(0,self.size[0]):
			for y in range(0,self.size[1]):
				if self.plan[self.posindx[x][y]] == 1:
					image.putpixel((x,y), (0,255,0))
		image.save(self.name+"_"+str(self.itt)+".png", "PNG")


	def setter(self,posx,posy,value=1):
		self.plan[self.posindx[posx][posy]] = value


	def setter_diff(self,posx,posy,value=1):
		self.plan_diff[self.posindx[posx][posy]] = value

	def ok_diff(self):
		self.plan = copy(self.plan_diff)

	def turn(self):
		self.plan_diff = copy(self.plan)
		for x in range(1,self.size[0]-1):
			for y in range(1,self.size[1]-1):
				self.cutpart(x,y)
		self.ok_diff()
		self.itt+=1

"""
#IS  AN EXAMPLE
nb_gen = 300

g = gol((512,512))

g.setter(200,200)
g.setter(201,200)
g.setter(202,200)
g.setter(203,200)
g.setter(202,201)
g.setter(203,201)
g.setter(202,203)
g.setter(203,203)
g.setter(202,200)
g.setter(202,201)

g.setter(30,20)
g.setter(31,20)
g.setter(32,20)


for r in range(0,nb_gen):
	print((r/(1.0*nb_gen))*100.0,"%")
	g.display()
	g.turn()

"""
"""
nb_gen = 300

g = gol((1296,1306))

from PIL import Image 
image_file = Image.open("assets/1-1.png")

for y in range(0,1306):
	for x in range(0,1296):
		if image_file.getpixel((x,y)) != 0:
			g.setter(x,y)


for r in range(0,nb_gen):
	print((r/(1.0*nb_gen))*100.0,"%")
	g.display()
	g.turn()
"""
