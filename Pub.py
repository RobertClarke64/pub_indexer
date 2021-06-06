class Pub:
	
	def __init__(self, name, address, postcode, easting, northing):
		self.name = name
		self.address = address
		self.postcode = postcode
		self.easting = easting
		self.northing = northing
		
	def get_name(self):
		return self.name
		
	def get_address(self):
		return self.address
		
	def get_postcode(self):
		return self.postcode
		
	def get_easting(self):
		return self.easting
		
	def get_northing(self):
		return self.northing
		