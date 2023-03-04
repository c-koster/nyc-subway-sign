from arrivals import Station

from UI import draw_trains

def run() -> None:
    s = Station("638N","6",lowercase=False)
    # s = Station("R19S","RW",lowercase=True)
    draw_trains(s)


run()