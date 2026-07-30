class ZoneType(Enum):
	NORMAL = "normal"
	BLOCKED = "blocked"
	RESTRICTED = "restricted"
	PRIORITY = "priority"


class Zone():
	def __init__(self, name: str, coordinates: tuple[int, int], type: ZoneType, color: str, max_drones: int) -> None:
		self.name: str = name
		self.coordinates: tuple[int, int] = coordinates
		self.type: ZoneType = type
		self.max_drones: int = max_drones
		self.color: str = color
		self.capacity_counter: int = 0
