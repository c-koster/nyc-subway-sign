from arrivals import Station

from UI import draw_trains

def run() -> None:
    s = Station("L11N","L",lowercase=False)
    draw_trains(s)


run()