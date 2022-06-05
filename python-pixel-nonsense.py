import PIL, random
import matplotlib.pyplot as pypl
import numpy as np
from PIL import Image, ImageDraw, ImageShow, ImageFilter



def createCanvas(x,y):
	canvas = np.zeros((x,y,3), dtype=np.uint8)
	return canvas


def makeArt(img):
	image_array = np.asarray(img)
	for i in range(0,canvas_y):
		for j in range(0,canvas_x):
			image_array[i,j] = rndColor(150,255,150,255,150,255)
	return image_array

def drawCircle(img,x,y):
	image_array = np.asarray(img)
	bg_col = rndColor(1,150,1,150,1,150)
	col_one = rndColor(100,255,100,255,100,255)
	for i in range(0,canvas_y):
		for j in range(0,canvas_x):
			image_array[i,j] = bg_col
			
	rpre = x/2
	cpre = y/2
	smax = x * 10
	SqDist= random.randrange(rpre,smax)
	r = int(random.randrange(1,rpre))
	c = int(random.randrange(1,cpre))
	for i in range(0,canvas_y):
		for j in range(0,canvas_x):
			if ((i/2 - r) ** 2 + (j/2 - c) ** 2 < SqDist):
				image_array[i,j] = col_one
	return image_array

def rndColor(rmin,rmax,gmin,gmax,bmin,bmax):
	randomColor = (random.randrange(rmin,rmax),random.randrange(gmin,gmax),random.randrange(bmin,bmax))
	return randomColor


def complexGen(img, x, y):
	image_array = np.asarray(img)
	bg_col = rndColor(1,150,1,150,1,150)
	col_one = rndColor(100,255,100,255,100,255)
	col_two = rndColor(1,255,1,255,1,255)
	for i in range(0,canvas_y):
		for j in range(0,canvas_x):
			image_array[i,j] = bg_col
	
	ysmall = int(y/2)
	xsmall = int(x/2)
	image_array[random.randrange(0,ysmall):random.randrange(ysmall,y),random.randrange(0,xsmall):random.randrange(xsmall,x)] = col_one
	
	image_array[random.randrange(0,ysmall):random.randrange(ysmall,y),random.randrange(0,xsmall):random.randrange(xsmall,x)] = col_two
	
	save_array = image_array[0,0]
	
	for i in range(0,canvas_y):
		for j in range(0,canvas_x):
			d = save_array != image_array
			if d.any():
				dif = image_array[i,j] - save_array
				image_array[i,j] = image_array[i,j] + dif
				save_array = image_array[i,j]
			
	
			
	return image_array


def complexGen2(img, x, y):
	image_array = np.asarray(img)
	bg_col = rndColor(1,150,1,150,1,150)
	col_one = rndColor(100,255,100,255,100,255)
	col_two = rndColor(1,255,1,255,1,255)
	for i in range(0,canvas_y):
		for j in range(0,canvas_x):
			image_array[i,j] = bg_col
			
	image_array = drawCircle(image_array,x,y)
	
	ysmall = int(y/2)
	xsmall = int(x/2)
	image_array[random.randrange(0,ysmall):random.randrange(ysmall,y),random.randrange(0,xsmall):random.randrange(xsmall,x)] = col_one
	
	
	image_array[random.randrange(0,ysmall):random.randrange(ysmall,y),random.randrange(0,xsmall):random.randrange(xsmall,x)] = col_two
	
	
	
	blurAmt = 5
	checkarray = 10
	for i in range(1,x):
		for j in range(1,y):
			i_max = random.randrange(-blurAmt,blurAmt)
			j_max = random.randrange(-blurAmt, blurAmt)
			check = i > checkarray or j > checkarray
			try:
				if check:
					image_array[i,j] = image_array[int(i-i_max),int(j-j_max)]
			except:
				i_max = random.randrange(0, blurAmt)
				j_max = random.randrange(0,blurAmt)
				check = i < checkarray and j < checkarray
				if check:
					image_array[i,j] = image_array[int(i-i_max),int(j-j_max)]
	
	
		
	return image_array


def barGen(img, x, y):
	image_array = np.asarray(img)
	bg_col = rndColor(1,150,1,150,1,150)
	col_one = rndColor(100,255,100,255,100,255)
	col_two = rndColor(1,255,1,255,1,255)
	for i in range(0,canvas_y):
		for j in range(0,canvas_x):
			image_array[i,j] = bg_col
	
	ysmall = int(y/2)
	xsmall = int(x/2)
	image_array[random.randrange(0,ysmall):random.randrange(ysmall,y),random.randrange(0,xsmall):random.randrange(xsmall,x)] = col_one
	
	image_array[random.randrange(0,ysmall):random.randrange(ysmall,y),random.randrange(0,xsmall):random.randrange(xsmall,x)] = col_two
	
	save_array = image_array[0,0]
	d = save_array != image_array
	for i in range(0,canvas_y):
		for j in range(0,canvas_x):
			if d.any():
				dif = image_array[i,j] + save_array
				image_array[i,j] = image_array[i,j] - dif
				save_array = image_array[i,j]
				d = save_array != image_array
			
			
	return image_array
	
	
def nextGen(img, x, y):
	image_array = np.asarray(img)
	bg_col = rndColor(1,150,1,150,1,150)
	col_one = rndColor(100,255,100,255,100,255)
	col_two = rndColor(1,255,1,255,1,255)
	for i in range(0,canvas_y):
		for j in range(0,canvas_x):
			image_array[i,j] = bg_col
	
	ysmall = int(y/2)
	xsmall = int(x/2)
	image_array[random.randrange(0,ysmall):random.randrange(ysmall,y),random.randrange(0,xsmall):random.randrange(xsmall,x)] = col_one
	
	image_array[random.randrange(0,ysmall):random.randrange(ysmall,y),random.randrange(0,xsmall):random.randrange(xsmall,x)] = col_two
				
	
	save_array = image_array[0,0]
	d = save_array != image_array
	for i in range(0,int(canvas_y)):
		for j in range(0,int(canvas_x)):
			if d.any():
				dif = image_array[i,j] - save_array
				image_array[i,j] = image_array[i,j] - dif 
				save_array = image_array[i,j]
				d = save_array != image_array
			#how do i iterate backwards? 
			
	return image_array
	
	

if __name__ == "__main__":
	canvas_x = 64
	canvas_y = 64
	canvas = createCanvas(canvas_y,canvas_x)
	#theArt = drawCircle(canvas,canvas_x,canvas_y)
	theArt = complexGen2(canvas,canvas_x,canvas_y)
	#theArt = makeArt(canvas)
	pypl.imshow(theArt,interpolation="nearest")
	pypl.show()
	
	####Use For Final Export####
	finalArt = Image.fromarray(theArt)
	ImageShow.show(finalArt)
