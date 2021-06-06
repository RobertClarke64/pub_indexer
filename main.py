from Pub import Pub
import csv
import math

def read_pubs(path):
	pubs = []
	
	with open(path, 'r', encoding='utf-8') as file:
		reader = csv.reader(file)
		for row in reader:
			pubs.append(Pub(row[1], row[2], row[3], row[4], row[5]))
				
	return pubs


if __name__ == "__main__" :

	pubs = read_pubs("open_pubs.csv")
	
	route = []
	
	for pub in pubs:
		if "MILLER" in pub.get_name().upper():
			route.append(pub)
			
	distances = []
	
	for start in route:
		row = []
		for end in route:
			start_x = int(start.get_easting())
			start_y = int(start.get_northing())
			end_x = int(end.get_easting())
			end_y = int(end.get_northing())
			
			distance = math.sqrt(abs((start_x - end_x)^2 + (start_y - end_y)^2))
			row.append(distance)
			
		distances.append(row)
		
		
	print(distances)
			
	
	
