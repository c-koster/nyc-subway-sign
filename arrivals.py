from dataclasses import dataclass,field
from typing import List, Dict
from datetime import datetime
from underground import SubwayFeed
from dotenv import load_dotenv
import os


load_dotenv()

API_KEY = os.getenv("MTA_API_KEY")


@dataclass(frozen=True)
class Arrival:
    # these are train ids that correspond with a station name and a direction
    station_id: int

    # these are both single character linenames. they rarely
    # differ although sometimes the 23 runs on the green line, etc
    line_name: str
    train_name: str 
    # when does the train arrive (dt object)
    arrival_time: datetime = field(compare=True)


    def get_name(self) -> Dict[str,str]:
        return {}




def get_arrivals(train_url: str) -> List[Arrival]:
    #station_name: int to speciify specific station
    feed = SubwayFeed.get(train_url, api_key = API_KEY).extract_stop_dict()
    for c in feed["L"]["L11"]:
        print(c)

    # return sorted(arrs)
    return []


# get_arrivals("https://api-endpoint.mta.info/Dataservice/mtagtfsfeedds/nyct%2Fgtfs-l")