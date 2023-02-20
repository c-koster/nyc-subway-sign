import time


from typing import List, Dict, Any
from RGBMatrixEmulator import RGBMatrix, RGBMatrixOptions, graphics


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
Purple  = graphics.Color(169,3,252)


colormap = {
    "L": Gray,
    "7": Purple
    # "B": ,
    # "D":
    # "F":
    # "M":
}

font = graphics.Font()
font.LoadFont("fonts/6x9.bdf")


def drawTrainCircle(x: int, y: int, char: str) -> None:
    assert len(char) < 2
    Color = colormap[char]

    graphics.DrawLine(canvas,x+2, y+0, x+6, y+0, Color)
    graphics.DrawLine(canvas,x+1, y+1, x+7, y+1, Color)
    graphics.DrawLine(canvas,x+0, y+2, x+8, y+2, Color)
    graphics.DrawLine(canvas,x+0, y+3, x+8, y+3, Color)
    graphics.DrawLine(canvas,x+0, y+4, x+8, y+4, Color)
    graphics.DrawLine(canvas,x+0, y+5, x+8, y+5, Color)
    graphics.DrawLine(canvas,x+0, y+6, x+8, y+6, Color)
    graphics.DrawLine(canvas,x+1, y+7, x+7, y+7, Color)
    graphics.DrawLine(canvas,x+2, y+8, x+6, y+8, Color)

    graphics.DrawText(canvas, font, x+2, y+7, Erase, char)
   
    

def drawRunningText(x: int, y: int, text: str) -> int:
    len = graphics.DrawText(canvas, font, x, y, Mint, text)


    return len
    


def drawMinsLeft(x: int, y: int, minutes: int) -> None:
    assert minutes < 100
    l = graphics.DrawText(canvas, font, x, y, Orange, "{m}".format(m=minutes))
    l = graphics.DrawText(canvas, font, x + l + 1, y, Mint,"min")



def draw_trains(train_cursor) -> None:


    assert hasattr(train_cursor,"print_trains")
    global canvas

    LPAD = 3
    COL_1 = 3
    COL_2 = 19

    
    while True:
        arriving_trains = train_cursor.print_trains()
        A = arriving_trains[0] 
        B = arriving_trains[1]
        print("redrawing canvas with:\n",A,"\n",B)


        canvas.Clear()
        # "line_name"
        # "destination"
        # "mins_to_arrive"

        # draw the first train    
        drawTrainCircle(LPAD,3, A["line_name"])
        drawRunningText(LPAD + 12,COL_1 + font.height - 1, A["destination"])
        drawMinsLeft(canvas.width - 30, COL_1 +font.height - 1, minutes=A["mins_to_arrive"])


        # and the second
        drawTrainCircle(LPAD,COL_2,B["line_name"]) 
        drawRunningText(LPAD + 12,COL_2 + font.height - 1, B["destination"])
        drawMinsLeft(canvas.width - 30, COL_2 + font.height - 1, minutes=B["mins_to_arrive"])
        

        # redraw canvas
        canvas = matrix.SwapOnVSync(canvas)
        time.sleep(30)


