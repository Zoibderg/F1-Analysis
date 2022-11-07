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

class Data:
    def __init__(self):
        fastf1.Cache.enable_cache('./cache')  # optional but recommended
        self.winners22 = {}
        self.events = fastf1.get_event_schedule(2022, include_testing=False)
        self.eventnames = [f"Round.{round}: \
-- {self.events[self.events['RoundNumber'] == round]['Location'].values[0]} -- \
{self.events[self.events['RoundNumber'] == round]['OfficialEventName'].values[0]}" 
for round in self.events['RoundNumber']]

    def get_gp_winners(self):
        # GRAB WINNERS
        for name in self.eventnames:
            gp = fastf1.get_session(2022, name, 'R')
            gp.load()
            result = gp.results
            # print(result)
            try:
                winner = result['BroadcastName'].iloc[0]
                self.winners22[name] = winner
            except Exception:
                self.winners22[name] = 'TBD'  # if no winner, set to TBD

data = Data()
data.get_gp_winners()

print(f"\nFORMULA 1 2022 GP WINNERS")
print("----------------------------")
for entry in data.winners22:
    print(f"\n{entry.title()} : {data.winners22[entry]}")
    print(f"\n-----------------------------")


# miami_gp = fastf1.get_session(2022, 'Miami', 'R')
# miami_gp.load()
# results = miami_gp.results   # this is a pandas dataframe
# print(results)

# # SHOW ALL COLUMNS IN RESULTS
# print(results.columns)
