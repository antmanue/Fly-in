from zone import Zone
from connection import Connection

class Drone():
	def __init__ (self, drone_id: str, start_hub: Zone) -> None:
		self.drone_id: str = drone_id
		self.current_position: Zone = start_hub
		self.turn_remaining: int = 0