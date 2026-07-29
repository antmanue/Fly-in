from zone import Zone
from connection import Connection
from drone import Drone

class Simulation:
	def __init__(self, zone: dict[str, Zone], connection: list[Connection], drone: list[Drone], nb_drones: int, start_hub: Zone, end_hub: Zone) -> None:
		self.zone = zone
		self.connection = connection
		self.drone = drone
		self.nb_drones = nb_drones
		self.start_hub: Zone = start_hub
		self.end_hub: Zone = end_hub

	def parse_map(self, filepath: str) -> None:
		try:
			with open(filepath, 'r') as file:
				for line in file:
					
					clean_line = line.strip()
					if not clean_line or clean_line.startswith('#'):
						continue
					if "nb_drones" in clean_line:
						parts = clean_line.split(":")
						[text, number] = parts
						self.nb_drones = int(number)
		
			
		except Exception as error:
			print (f"Error while reading file: {error}")