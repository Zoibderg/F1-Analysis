"""
This file is for exploring fastf1 package. It seems to offer us more options in terms 
of exploring and managing the data from the ergast API.
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
plt.show()