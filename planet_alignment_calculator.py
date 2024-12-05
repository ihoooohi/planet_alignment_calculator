import numpy as np

periods = [88, 225, 365.25]

# Daily position change 
daily_motion = [360 / p for p in periods]

angles = [0, 0, 0]

tolerance = 1

day = 0
while True:
    day += 1
    # Update angular position for each planet
    angles = [(angle + daily_motion[i]) % 360 for i, angle in enumerate(angles)]
    
    # Calculate maximum angle difference
    max_angle_diff = max(np.abs(np.diff(sorted(angles))))
    
    # Check if all planets are within 1 degree
    if max_angle_diff <= tolerance:
        break

print(f"After approximately {day} days, Mercury, Venus and Earth will nearly align again.")