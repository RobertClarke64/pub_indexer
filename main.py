from Pub import Pub
import csv

def read_pubs(path):
	pubs = []
	
	with open(path, 'r') as file:
		reader = csv.reader(file)
		for row in reader:
			pubs.append(Pub(row[1], row[2], row[3], row[4], row[5]))
				
	return pubs


if __name__ == "__main__" :

	pubs = read_pubs("open_pubs.csv")
	
	print(pubs[3].get_name())
	
	
