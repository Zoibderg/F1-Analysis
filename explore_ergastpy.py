"""
This file is for exploring fastf1 package. It seems to offer us more options in terms 
of exploring and managing the data from the ergast API.
"""


from unittest import result
import matplotlib.pyplot as plt
import pandas as pd
import pprint as pp
from timple.timedelta import strftimedelta
import fastf1
import fastf1.plotting as plotting
from fastf1.core import Laps


# GITHUB EXAMPLE
plotting.setup_mpl()

fastf1.Cache.enable_cache('./cache')  # optional but recommended

# race = fastf1.get_session(2020, 'Turkish Grand Prix', 'R')
# race.load()

# lec = race.laps.pick_driver('LEC')
# ham = race.laps.pick_driver('HAM')

# # PLOTTING DATA
# fig, ax = plt.subplots()
# ax.plot(lec['LapNumber'], lec['LapTime'], color='red')
# ax.plot(ham['LapNumber'], ham['LapTime'], color='cyan')
# ax.set_title("LEC vs HAM")
# ax.set_xlabel("Lap Number")
# ax.set_ylabel("Lap Time")
# plt.show()

# SHOW 2022 RACES, EXCLUDING TESTING
events = fastf1.get_event_schedule(2022, include_testing=False)
# print(events)


winners22 = {}

eventnames = [f"Round.{round}: \
-- {events[events['RoundNumber'] == round]['Location'].values[0]} -- \
{events[events['RoundNumber'] == round]['OfficialEventName'].values[0]}" 
for round in events['RoundNumber']]

# print(eventnames)


# GRAB WINNERS
for name in eventnames:
    gp = fastf1.get_session(2022, name, 'R')
    gp.load()
    result = gp.results
    # print(result)
    try:
        winner = result['BroadcastName'].iloc[0]
        winners22[name] = winner
    except Exception:
        winners22[name] = 'TBD'

print(f"\nFORMULA 1 2022 GP WINNERS")
print("----------------------------")
for entry in winners22:
    print(f"\n{entry.title()} : {winners22[entry]}")
    print(f"\n-----------------------------")


# miami_gp = fastf1.get_session(2022, 'Miami', 'R')
# miami_gp.load()
# results = miami_gp.results   # this is a pandas dataframe
# print(results)

# # SHOW ALL COLUMNS IN RESULTS
# print(results.columns)
