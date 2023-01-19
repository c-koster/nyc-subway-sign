import time


from typing import List, Dict, Any
from RGBMatrixEmulator import RGBMatrix, RGBMatrixOptions,graphics


# setup_matrix() # Configuration for the matrix
options = RGBMatrixOptions()
options.rows = 32
options.cols = 128
options.chain_length = 1 # options.chain_length = 2 # or 2
options.parallel = 1
options.hardware_mapping = 'regular'  # If you have an Adafruit HAT: 'adafruit-hat'

matrix = RGBMatrix(options = options)
canvas = matrix.CreateFrameCanvas()



# consts
Mint    = graphics.Color(152,255,152)
Gray    = graphics.Color(140,153,166)
Orange  = graphics.Color(245,114,0)
Erase   = graphics.Color(0,0,0)



font = graphics.Font()
font.LoadFont("fonts/6x9.bdf")


def drawTrainCircle(x: int, y: int, char: str) -> None:
    assert len(char) < 2

    graphics.DrawLine(canvas,x+2, y+0, x+6, y+0, Gray)
    graphics.DrawLine(canvas,x+1, y+1, x+7, y+1, Gray)
    graphics.DrawLine(canvas,x+0, y+2, x+8, y+2, Gray)
    graphics.DrawLine(canvas,x+0, y+3, x+8, y+3, Gray)
    graphics.DrawLine(canvas,x+0, y+4, x+8, y+4, Gray)
    graphics.DrawLine(canvas,x+0, y+5, x+8, y+5, Gray)
    graphics.DrawLine(canvas,x+0, y+6, x+8, y+6, Gray)
    graphics.DrawLine(canvas,x+1, y+7, x+7, y+7, Gray)
    graphics.DrawLine(canvas,x+2, y+8, x+6, y+8, Gray)

    graphics.DrawText(canvas, font, x+2, y+7, Erase, char)
   
    

def drawRunningText(x: int, y: int, text: str) -> int:
    len = graphics.DrawText(canvas, font, x, y, Mint, text)


    return len
    


def drawMinsLeft(x: int, y: int, minutes: int) -> None:
    assert minutes < 100
    l = graphics.DrawText(canvas, font, x, y, Orange, "{m}".format(m=minutes))
    l = graphics.DrawText(canvas, font, x + l + 1, y, Mint,"min")






def draw_trains(train_info: List[Dict[str,Any]]) -> None:
    # this can loop forever
    pass


while True:


    draw_trains([])
    drawTrainCircle(5,3,"L")
    drawRunningText(18,11,"ROCKAWAY PKWY")
    drawMinsLeft(canvas.width - 25, 11,minutes=9)
    
    canvas = matrix.SwapOnVSync(canvas)
    time.sleep(5)
