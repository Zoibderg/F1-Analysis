"""
This file is for exploring fastf1 package. It seems to offer us more options in terms
of exploring and managing the data from the ergast API.
"""

import fastf1

class Data:
    """
    class for grabbing ddata from the ergast API
    """
    def __init__(self):
        fastf1.Cache.enable_cache('./cache')  # optional but recommended
        self.winners22 = {}
        self.events = fastf1.get_event_schedule(2022, include_testing=False)
        self.eventnames = [f"Round.{round}: \
-- {self.events[self.events['RoundNumber'] == round]['Location'].values[0]} -- \
{self.events[self.events['RoundNumber'] == round]['OfficialEventName'].values[0]}"
for round in self.events['RoundNumber']]

    def get_gp_winners(self):
        """
        grab winners, hardcoded for testing purposes
        """
        # GRAB WINNERS
        for name in self.eventnames:
            gp_data = fastf1.get_session(2022, name, 'R')
            gp_data.load()
            result = gp_data.results
            # print(result)
            try:
                winner = result['BroadcastName'].iloc[0]
                self.winners22[name] = winner
            except IndexError:
                self.winners22[name] = 'TBD'  # if no winner, set to TBD

data = Data()
data.get_gp_winners()

print("\nFORMULA 1 2022 GP WINNERS")
print("----------------------------")
for key, value in data.winners22.items():
    print(f"\n{key} : {data.winners22[value]}")
    print("\n-----------------------------")


# miami_gp = fastf1.get_session(2022, 'Miami', 'R')
# miami_gp.load()
# results = miami_gp.results   # this is a pandas dataframe
# print(results)

# # SHOW ALL COLUMNS IN RESULTS
# print(results.columns)
