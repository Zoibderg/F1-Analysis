"""
This file is for exploring fastf1 package. It seems to offer us more options in terms 
of exploring and managing the data from the ergast API.
"""



from unittest import result
import matplotlib.pyplot as plt
import pandas as pd
import pprint
from timple.timedelta import strftimedelta
import fastf1
import fastf1.plotting as plotting
from fastf1.core import Laps


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
events = fastf1.get_event_schedule(2022)
print(events)

eventnames = []
winners22 = {}
for event in events['OfficialEventName']:
    eventname = str(event)
    eventnames.append(eventname)

for name in eventnames:
    gp = fastf1.get_session(2022, name, 'R')
    gp.load()
    result = gp.results
    print(result)
    try:
        winner = result['BroadcastName'].iloc[0]
        winners22[name] = winner
    except Exception:
        winners22[name] = 'TBD'

pprint.pprint(winners22)

# FOR EACH EVENT, SHOW THE RACE RESULTS


# miami_gp = fastf1.get_session(2022, 'Miami', 'R')
# miami_gp.load()
# results = miami_gp.results   # this is a pandas dataframe
# print(results)

# # SHOW ALL COLUMNS IN RESULTS
# print(results.columns)
