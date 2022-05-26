# fixedwing-mangrove
Code for the mangrove fixed wing UAV sensors


Added functionality of Raspberry Pi based camera control which allows the script to run at startup and create a new folder each time to store pictures.
Modified rc.local file on Raspberry Pi to autorun at boot

The file name now consists of longtitude, latitude and altitude information as well as time. Longtitude, latitude and altitude come from pixhawk
