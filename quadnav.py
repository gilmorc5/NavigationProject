#CEC300 Navigation Project  
# Charles Gilmore
# Feb. 19, 2022
#
# A quadcopter is located at latitude 29.401325 and longitude -81.177222 the quadrotor is oriented so that the y axis is aligned with north/south and the x axis is aligned with east/west. 
# Positive accelerations on the y axis are towards the north and positive accelerations on the x axis are towards the east. Time is in seconds and the acceleration data units are cm/sec^2.
#
# The data is contained in the file quad_accel.xlsx  When the data starts, the quadrotor x velocity is -0.2 m/s and the y velocity is 0.44 m/s 
# The data was taken every 100ms. The accelerometer data is in the file quad_accel_data.xlsx.
#
# Using the acceleration data you are determine the position of the quadcopter at every measurement, convert the position to GPS coordinates, and then plot the flight path on a map of the earth so that the location of the flight is clearly visible. 

#####################################################################



## Global Defs
# Initial Conditions
lat_x = 29.401325   # (-) West -> (+) East X axis
long_y = -81.177222 # (-) South -> (+) North Y axis
init_x_vel = -0.2 # m/s
init_y_vel = 0.44 # m/s

# Accelerometer excel sheet
path = ("quad_accel.xlsx")
wb = openpyxl.load_workbook(path)
sheet = wb.active
max_col = sheet.max_column

for i in range(1, max_col +1):
    cell = sheet.cell(row = 1, column = i)
    print(cell.value)