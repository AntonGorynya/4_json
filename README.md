# Prettify JSON

Convert json output to pretty json output

# Quickstart
Script need installed json library
You can download and run it directly through console

Example of script launch on Linux, Python 3.5:

```#!bash

$ python pprint_json.py <path to file>
Content of input file: {'Comment': 'My comment', 'Count': 10, 'DiskParam': {'DB': 10.0, 'DBAngle': 1.234}, 'Range': True, 'Blades': [{'Caption': 'A', 'Value': 65}, {'Caption': 'B', 'Value': 66}, {'Caption': 'C', 'Value': 67}], 'Slots': [0, 1, 2, 3]}

Console output:
 {
	 "Comment":		 "My comment",
	 "Count":		 "10",
	 "DiskParam":	 {
		 "DB":			 "10.0",
		 "DBAngle":			 "1.234"
	 },
	 "Range":		 "True",
	 "Blades":	 [
	 {
		 "Caption":			 "A",
		 "Value":			 "65"
	 },
	 {
		 "Caption":			 "B",
		 "Value":			 "66"
	 },
	 {
		 "Caption":			 "C",
		 "Value":			 "67"
	 }
	 ],
	 "Slots":	 [
		 "0",
		 "1",
		 "2",
		 "3"
	 ]
 }

```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
