from arrivals import Station
from UI import draw_trains
from dotenv import load_dotenv
import os

load_dotenv()


def run() -> None:
    station_to_track = os.getenv("STATION_TO_TRACK", "638N")  # (name, default value)
    lines_to_track = os.getenv("LINES_TO_TRACK", "6")

    s = Station(station_to_track, lines_to_track, lowercase=False)
    draw_trains(s)


run()
