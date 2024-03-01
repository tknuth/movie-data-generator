from movie_data_generator import Simulation
from loguru import logger
import sys

custom_format = "<fg #888>{time:YYYY-MM-DD HH:mm:ss}</fg #888> {level} {message}"
logger.configure(handlers=[{"sink": sys.stderr, "format": custom_format}])

simulation = Simulation()
simulation.run()
