from modules.solar import solar
from rich.console import Console

rc = Console()

rc.log(solar.pv_daily(5,1000), "kWh")

rc.log(solar.tilt_angle("summer", 34), "degrees")

rc.log(round(solar.tilt_angle2("winter", 34), 2), "degrees")

energy_consumption = {
	'jan': 87,
	'dec': 78,
	'nov': 113,
	'oct': 170,
	'sep': 176,
	'aug': 165,
	'jul': 215,
	'jun': 429,
	'may': 504,
	'apr': 510,
	'mar': 267,
	'feb': 195
}


