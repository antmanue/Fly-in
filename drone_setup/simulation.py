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

	def _parse_zone_line(self, line_content: str) -> Zone:
		metadata_str = ""
		if "[" in line_content:
			line_content, raw_meta = line_content.split("[")
			metadata_str = raw_meta.replace("]", "").strip()

		info = line_content.split()
		name = info[0]
		x = int(info[1])
		y = int(info[2])

		zone_type = ZoneType.NORMAL
		color = "none"
		max_drones = 1

		if metadata_str:
			for item in metadata_str.split():
				if "=" in item:
					key, value = item.split("=")
					if key == "zone":
						zone_type = ZoneType(value)
					elif key == "color":
						color = value
					elif key == "max_drones":
						max_drones = int(value)
						
		return Zone(name, (x, y), zone_type, color, max_drones)
					
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
					
					elif clean_line.startswith("start_hub"):
						content = clean_line.replace("start_hub:", "").strip()
						start_zone = self._parse_zone_line(content)
						self.start_hub = start_zone
						self.zone[start_zone.name] = start_zone

					elif clean_line.startswith("end_hub"):
						content = clean_line.replace("end_hub:", "").strip()
						end_zone = self._parse_zone_line(content)
						self.end_hub = end_zone
						self.zone[end_zone.name] = end_zone

					elif clean_line.startswith("hub:"):
						content = clean_line.replace("hub:", "").strip()
						new_zone = self._parse_zone_line(content)
						self.zone[new_zone.name] = new_zone
					
					elif clean_line.startswith("connection:"):
						content = clean_line.replace("connection:", "").strip()
						metadata_str = ""
						if "[" in content:
							content, raw_meta = content.split("[")
							metadata_str = raw_meta.replace("]", "").strip()

						zone_names = content.strip().split("-")
						zone_a_name = zone_names[0]
						zone_b_name = zone_names[1]

						zone_a = self.zone[zone_a_name]
						zone_b = self.zone[zone_b_name]

						max_link_capacity = 1

						if metadata_str:
							for item in metadata_str.split():
								if "=" in item:
									key, value = item.split("=")
									if key == "max_link_capacity": 
										max_link_capacity = int(value)
						
						new_connection = Connection(zone_a, zone_b, max_link_capacity)
						self.connection.append(new_connection)
			for i in range(1, self.nb_drones + 1):
				drone_id = f"D{i}"
				new_drone = Drone(drone_id, self.start_hub)
				self.drone.append(new_drone)
		
		except Exception as error:
			print (f"Error while reading file: {error}")
