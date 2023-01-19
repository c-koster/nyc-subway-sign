from dataclasses import dataclass,field
from typing import List, Dict, Any
from datetime import datetime
from underground import SubwayFeed, metadata
from dotenv import load_dotenv
import os
import pandas as pd 

load_dotenv()

API_KEY = os.getenv("MTA_API_KEY","")

df = pd.read_csv("data/stops.txt")
df = df.set_index("stop_id")
id2names = df["stop_name"].to_dict()
del df


@dataclass(frozen=True, order=True)
class Arrival:
    # these are train ids that correspond with a station name and a direction
    station_id: str = field(compare=False)
    destination_station_id: str = field(compare=False)

    line_name: str = field(compare=False) # single character line name

    # when does the train arrive (dt object)
    arrival_ts: datetime = field(compare=True)



    def as_printable_dict(self, now_ts: datetime) -> Dict[str, Any]:


        return {
            "line_name": self.line_name,
            "destination": id2names[self.destination_station_id],
            "mins_to_arrive": (self.arrival_ts - now_ts).seconds // 60,
        }

    

@dataclass()
class Station:
    # instatiate one of these objects with station_id and line names
    # and call it repeatedly.

    station_id: str
    line_names: str # or char array


    def get_name(self) -> str:
        return id2names[self.station_id]
    

    def print_trains(self) -> List[Dict[str,Any]]:
        """
        Prints out next two trains to arrive. can add time-to-station logic here later.
        """

        arrivals = self.get_arrivals()
        now = datetime.now().astimezone()
        return [ a.as_printable_dict(now)  for a in arrivals[:2] ]


    def get_arrivals(self) -> List[Arrival]:
        """
        Gets all of the arrivals for the given station and line names.
        Returns them as a list of Arrival objects sorted by arrival time.        
        """

        # output me later 
        arrivals = []

        # get all relevant URLs for a given request. e.g. if I wanted 4 and 5 trains then I would only have to make one query
        
        dedup_urls = set([metadata.resolve_url(c) for c in self.line_names])
        # feed = SubwayFeed.get(line_names[0], api_key = API_KEY)
        for url in dedup_urls:
            feed = SubwayFeed.get(url).extract_stop_dict()
            for route in feed:
                if route in self.line_names:
                    arrivals += [
                        Arrival(
                            station_id=self.station_id,
                            destination_station_id="8 AV",
                            line_name=route,
                            arrival_ts = ts
                        )
                        for ts in feed[route][self.station_id]
                    ]
        
        return sorted(arrivals)