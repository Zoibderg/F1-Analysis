"""
This file is for exploring fastf1 package. It seems to offer us more options in terms 
of exploring and managing the data from the ergast API.
"""

"""
This is pretty advanced and there is a LOT that can be done. I will want to
keep exploring deeper to get more comfortable with this package. 
"""

import fastf1
from fastf1 import plotting
from matplotlib import pyplot as plt


# GITHUB EXAMPLE
plotting.setup_mpl()

fastf1.Cache.enable_cache('./F1_HE_Analysis/cache')  # optional but recommended

race = fastf1.get_session(2020, 'Turkish Grand Prix', 'R')
race.load()

lec = race.laps.pick_driver('LEC')
ham = race.laps.pick_driver('HAM')

# PLOTTING DATA
fig, ax = plt.subplots()
ax.plot(lec['LapNumber'], lec['LapTime'], color='red')
ax.plot(ham['LapNumber'], ham['LapTime'], color='cyan')
ax.set_title("LEC vs HAM")
ax.set_xlabel("Lap Number")
ax.set_ylabel("Lap Time")
# plt.show()

# SHOW 2022 RACES, INCLUDING TESTING
event = fastf1.get_event_schedule(2022)
#print(event)

miami_gp = fastf1.get_session(2022, 'Miami', 'R')
miami_gp.load()
results = miami_gp.results   # this is a pandas dataframe
print(results)