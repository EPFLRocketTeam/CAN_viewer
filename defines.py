"""
	
	Following constants present:
	CAN IDs
	CAN messages data types
	
"""

# BOARD CAN IDs
CAN_ID_MAIN_BOARD	 		= 0
CAN_ID_GPS_BOARD			= 1
CAN_ID_TELEMETRY_BOARD	 	= 2
CAN_ID_AIBRAKE_BOARD 		= 3
CAN_ID_DEBUG_BOARD  		= 6
CAN_ID_DEFAULT				= 7
CAN_ID_PROPULSION_BOARD 	= 5

# CAN frame data IDs
DATA_ID_PRESSURE			= 0		# hPa
DATA_ID_ACCELERATION_X		= 1 	# milli-g
DATA_ID_ACCELERATION_Y	 	= 2		# milli-g
DATA_ID_ACCELERATION_Z	 	= 3		# milli-g
DATA_ID_GYRO_X	 			= 4		# mrps
DATA_ID_GYRO_Y	 			= 5		# mrps
DATA_ID_GYRO_Z	 			= 6		# mrps

DATA_ID_GPS_HDOP	      	= 7		# mm
DATA_ID_GPS_LAT		     	= 8		# udeg
DATA_ID_GPS_LONG	    	= 9		# udeg
DATA_ID_GPS_ALTITUDE 		= 10	# cm
DATA_ID_GPS_SATS	   		= 11	# [-]

DATA_ID_TEMPERATURE			= 12	# cDegC
DATA_ID_CALIB_PRESSURE 		= 13	# Pa

DATA_ID_AB_STATE 			= 16	# enum
DATA_ID_AB_INC 				= 17	# [-]
DATA_ID_AB_AIRSPEED 		= 18	# mm/s
DATA_ID_AB_ALT 				= 19	# m

DATA_ID_KALMAN_STATE 		= 38	# enum
DATA_ID_KALMAN_X 			= 40	# m
DATA_ID_KALMAN_Y 			= 41	# m
DATA_ID_KALMAN_Z 			= 42	# m
DATA_ID_KALMAN_VX 			= 43	# mm/s
DATA_ID_KALMAN_VY 			= 44	# mm/s
DATA_ID_KALMAN_VZ 			= 45	# mm/s
DATA_ID_KALMAN_YAW 			= 46	# mrad
DATA_ID_KALMAN_PITCH 		= 47	# mrad
DATA_ID_KALMAN_ROLL 		= 48	# mrad

DATA_ID_STATE 				= 50 	# enum

#TODO which DATA_ID is the correct one for the ignition?
DATA_ID_ORDER 				= 51	# same as DATA_ID_IGNITION
DATA_ID_IGNITION 			= 51	# secret number = 0x22 (TODO check number)

DATA_ID_MOTOR_PRESSURE 		= 55	# float