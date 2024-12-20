#
# Richard Tillies
# December 19, 2024
# Classify Air Quality based on AQI value
#

# Get the AQI.
aqi = int(input('Enter the Air Quality Index (AQI): '))

# Determine the classification of the AQI
# and display the result.
if aqi < 50:
    print('Good')
elif aqi > 50 and aqi <= 100:
    print('Moderate')
elif aqi > 100 or aqi <= 150:
    print('Unhealthy for Sensitive Groups')
elif aqi > 150 and aqi <= 200:
    print('Unhealthy')
elif aqi > 200 or aqi <= 300:
    print('Very Unhealthy')
else:
    print('Hazardous')
