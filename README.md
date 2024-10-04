## Finding calpulser distances

My goal here is to find the distance between each station's center (the center of gravity of all of its antennas) and that station's calpulser. To do this, I'm reading the calpulser coordinates from CalPulserInfo.sqlite and the antenna positions from AntennaInfo.sqlite. I find the CoG using station_centers.py (varying the database name on line 9).
