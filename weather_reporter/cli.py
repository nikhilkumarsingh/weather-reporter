import argparse
from .utils import *


def main():
	# create argument parser object 
	parser = argparse.ArgumentParser(description = "Weather Reporter") 
  
	parser.add_argument("-q", "--query", type = str, nargs = 1, 
	                    metavar = "location", default = None, help = "Location") 

	parser.add_argument("-d", "--days", type = int, nargs = 1, 
	                    metavar = "days", default = [1], help = "Number of days") 

	# parse the arguments from standard input 
	args = parser.parse_args()

	weather_data = get_weather(args.query, args.days[0])
	print_weather_details(weather_data)


if __name__ == "__main__":
	main()