import board
import neopixel
from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners.keypad import KeysScanner, RotaryEncoder

class KMKKeyboard(_KMKKeyboard):
    def __init__(self):
        super().__init__()

        # Direct-to-GND GPIO mapping (Diode-less design)
        self.matrix = KeysScanner(
            pins=(
                board.GP0, board.GP1, board.GP2,  # Row 1
                board.GP3, board.GP4, board.GP5,  # Row 2
                board.GP6, board.GP7, board.GP8   # Row 3
            ),
            value_when_pressed=False,  
            pull=True                  
        )

        # EC11 Rotary Encoder
        self.rotary_encoder = RotaryEncoder(
            pin_a=board.GP26,
            pin_b=board.GP27,
            divisor=4,
        )
        self.encoder_button_pin = board.GP28

        # Underglow / Switch Lighting
        self.num_leds = 14  
        self.leds = neopixel.NeoPixel(
            board.GP29, 
            self.num_leds, 
            brightness=0.4, 
            auto_write=False, 
            pixel_order=neopixel.GRBW
        )

        # Spatial coordinates for fluid rendering effects
        self.led_positions = [
            (11, 0.5),
            (2, 27.5), (2, 46.5), (2, 65.5),
            (20.475, 27.5), (220.475, 46.5), (20.475, 65.5),
            (39.525, 27.5), (39.525, 46.5), (39.525, 65.5),
            (58, 27.5), (58, 46.5), (58, 65.5),
            (49.25, 0.5)
        ]
