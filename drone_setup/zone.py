from enum import Enum

class ZoneType(Enum):
	NORMAL = "normal"
	BLOCKED = "blocked"
	RESTRICTED = "restricted"
	PRIORITY = "priority"


class Zone():
	def __init__(
		self,
		name: str,
		coordinates: tuple[int, int],
		type: ZoneType,
		color: str,
		max_drones: int
	) -> None:
		if not name or "_" in name or " " in name:
			raise ValueError(
				f"Invalid zone name '{name}'. Cannot contain dashes or spaces.")
		if max_drones <= 0:
			raise ValueError(
				f"Invalid max drones '{max_drones}'for zone '{name}': "
				"must be a positive integer.")
	
		self.name: str = name
		self.coordinates: tuple[int, int] = coordinates
		self.type: ZoneType = zone_type
		self.color: str = color
		self.max_drones: int = max_drones
		self.is_start: bool = is_start
		self.is_end: bool = is_end
