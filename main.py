from arrivals import Station

from UI import draw_trains

def run() -> None:


    s = Station("L","L11N")
    
    try:    
        draw_trains(
            train_info = s.print_trains()
        )
    except KeyboardInterrupt:
        pass

run()