"""
Python Certification freeCodeCamp
Chapter: Python Basics
Subchapter: Build a Travel Weather Planner (Lab)
"""

distance_mi = 7
is_raining = False

has_bike = True
has_car = False
has_ride_share_app = True

if not distance_mi:
    print(False)
elif not is_raining and distance_mi <= 1:
    print(True) 
elif is_raining == True and distance_mi <= 1:
    print(False)
elif not has_bike and is_raining == True and distance_mi > 1 and distance_mi <= 6:
    print(False)
elif has_bike and not is_raining and distance_mi > 1 and distance_mi <= 6:
    print(True)
elif distance_mi > 6 and (has_car or has_ride_share_app):
    print(True)
else:
    print(False)
