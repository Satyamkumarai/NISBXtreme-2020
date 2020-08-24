'''NOTE :
	THIS TEST CASE GENERATOR STILL NEEDS SOME MANUAL WORK TO MAKE IT USABLE AS A HACKERRANK TEST CASE 
	WE NEED TO FIND THE INCLUSIVE POINT BY HAND AS I WANTED AN EVEN DISTRIBUTION OF YES AND NO SOLUTIONS.
'''

import math, random,numpy

origin = [30,30]
refvec = [0, 0]


def clip(x, min, max):
	if( min > max ):
		return x    
	elif( x < min ):  
		return min
	elif( x > max ):  
		return max
	else:
		return x

def generatePolygon( ctrX, ctrY, aveRadius, irregularity, spikeyness, numVerts ) :
	'''Start with the centre of the polygon at ctrX, ctrY, 
	then creates the polygon by sampling points on a circle around the centre. 
	Randon noise is added by varying the angular spacing between sequential points,
	and by varying the radial distance of each point from the centre.

	Params:
	ctrX, ctrY - coordinates of the "centre" of the polygon
	aveRadius - in px, the average radius of this polygon, this roughly controls how large the polygon is, really only useful for order of magnitude.
	irregularity - [0,1] indicating how much variance there is in the angular spacing of vertices. [0,1] will map to [0, 2pi/numberOfVerts]
	spikeyness - [0,1] indicating how much variance there is in each vertex from the circle of radius aveRadius. [0,1] will map to [0, aveRadius]
	numVerts - self-explanatory

	Returns a list of vertices, in CCW order.
	'''

	irregularity = clip( irregularity, 0,1 ) * 2*math.pi / numVerts
	spikeyness = clip( spikeyness, 0,1 ) * aveRadius

	# generate n angle steps
	angleSteps = []
	lower = (2*math.pi / numVerts) - irregularity
	upper = (2*math.pi / numVerts) + irregularity
	sum = 0
	for i in range(numVerts):
		tmp = random.uniform(lower, upper)
		angleSteps.append( tmp )
		sum = sum + tmp

	# normalize the steps so that point 0 and point n+1 are the same
	k = sum / (2*math.pi)
	for i in range(numVerts):
		angleSteps[i] = angleSteps[i] / k

	# now generate the points
	points = []
	angle = random.uniform(0, 2*math.pi)
	for i in range(numVerts):
		r_i = clip( random.gauss(aveRadius, spikeyness), 0, 2*aveRadius )
		x = ctrX + r_i*math.cos(angle)
		y = ctrY + r_i*math.sin(angle)
		points.append( (int(x),int(y)) )

		angle = angle + angleSteps[i]

	return points


def clockwiseangle_and_distance(point):
    # Vector between point and the origin: v = p - o
    vector = [point[0]-origin[0], point[1]-origin[1]]
    # Length of vector: ||v||
    lenvector = math.hypot(vector[0], vector[1])
    # If length is zero there is no angle
    if lenvector == 0:
        return -math.pi, 0
    # Normalize vector: v/||v||
    normalized = [vector[0]/lenvector, vector[1]/lenvector]
    dotprod  = normalized[0]*refvec[0] + normalized[1]*refvec[1]     # x1*x2 + y1*y2
    diffprod = refvec[1]*normalized[0] - refvec[0]*normalized[1]     # x1*y2 - y1*x2
    angle = math.atan2(diffprod, dotprod)
    # Negative angles represent counter-clockwise angles so we need to subtract them 
    # from 2*pi (360 degrees)
    if angle < 0:
        return 2*math.pi+angle, lenvector
    # I return first the angle because that's the primary sorting criterium
    # but if two vectors have the same angle then the shorter distance should come first.
    return angle, lenvector


if __name__ == "__main__":
	n=int(input())
	for i in range(n):
		N = numpy.random.randint(1,10)
		with open(f"test{i}.txt",'w') as file:
			file.write(f"{N}\n")
			for j in range(N):
				sides = numpy.random.randint(3,10)
				file.write(f"{sides}\n")
				center = numpy.random.randint(0,100,2)
				irregular = numpy.random.random()
				spkie = numpy.random.random()
				a=generatePolygon(center[0],center[1],10,irregular,spkie,sides)
				for item in a:
					file.write(str(item)[1:-1].replace(",","")+"\n")
