from dataclasses import dataclass,field
from typing import List, Dict
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
    # these are both single character linenames. they rarely
    # differ although sometimes the 23 runs on the green line, etc
    line_name: str = field(compare=False)

    # when does the train arrive (dt object)
    arrival_ts: datetime = field(compare=True)



    def get_name(self) -> str:

        return  id2names[self.station_id]
    


def get_arrivals(line_names: str, station_id: str) -> List[Arrival]:
    """
    
    
    
    """

    # output me later 
    arrivals = []

    # get all relevant URLs for a given request. e.g. if I wanted 4 and 5 trains then I would only have to make one query
    
    dedup_urls = set([metadata.resolve_url(c) for c in line_names])
    # feed = SubwayFeed.get(line_names[0], api_key = API_KEY)
    for url in dedup_urls:
        feed = SubwayFeed.get(url).extract_stop_dict()
        for route in feed:
            if route in line_names:
                arrivals += [
                    Arrival(station_id=station_id,line_name=route, arrival_ts = ts)
                    for ts in feed[route][station_id]
                ]
        
    # print(c,v)
    return sorted(arrivals)