import csv

class FlightSchedule:

	def __init__(self):
		self.flights = None
		self.plane_identifiers = None

	def read_data_from_file(self):
		self.flights = []
		self.plane_identifiers = []

		with open("flight_data.csv", encoding='utf-8') as f:
			reader = csv.reader(f)
			for line in reader:
				self.flights.append(line)
				if line[1] not in self.plane_identifiers:
					self.plane_identifiers.append(line[1])

	def determine_longest_flight(self):
		longest_flight = None
		longest_flight_miles = 0

		for flight in self.flights:
			if longest_flight_miles < float(flight[4]):
				longest_flight = flight[0]
				longest_flight_identifier = flight[1]
				longest_flight_origin = flight[2]
				longest_flight_destination = flight[3]
				longest_flight_miles = float(flight[4])
				longest_flight_passengers = float(flight[5])

		return longest_flight 