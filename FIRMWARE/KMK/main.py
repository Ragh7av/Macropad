import board
import time
import math
import digitalio
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.rotary_encoder import RotaryEncoderHandler

keyboard = KMKKeyboard()

# Core Modules
keyboard.modules.append(Layers())
encoder_handler = RotaryEncoderHandler()
keyboard.modules.append(encoder_handler)

# Base Keymap (Linear list matching GP0 to GP8)
keyboard.keymap = [
    [
        KC.MRWD, KC.MPLY, KC.MFFD,         # Row 1: GP0, GP1, GP2
        KC.MSEL, KC.CALC, KC.LGUI(KC.R),   # Row 2: GP3, GP4, GP5
        KC.LEFT, KC.RIGHT, KC.LGUI(KC.L),  # Row 3: GP6, GP7, GP8
    ]
]

# Encoder Configuration
encoder_handler.pins = (board.GP26, board.GP27)
encoder_handler.divisor = 4
encoder_handler.map = [KC.VOLD, KC.VOLU]

# Encoder Switch Configuration
encoder_button = digitalio.DigitalInOut(board.GP28)
encoder_button.switch_to_input(pull=digitalio.Pull.UP)

# Lighting Engine Engine State
led_modes = ["Solid Pulse", "Rainbow Spectrum", "Wave Motion", "Sunlight Ripple"]
current_mode = 0
last_button_state = True
last_led_tick = 0
led_frame_rate = 0.03  # Locks animations to ~33 FPS to prioritize keystroke latency

def calculate_lighting_effects():
    timestamp = time.monotonic()
    
    if led_modes[current_mode] == "Solid Pulse":
        speed = timestamp * 1.5
        for i, (x, y) in enumerate(keyboard.led_positions):
            pulse = int((math.sin(speed + x * 0.5 + y * 0.5) + 1) * 127)
            keyboard.leds[i] = (0, 0, pulse, pulse // 2)
            
    elif led_modes[current_mode] == "Rainbow Spectrum":
        shift = int(timestamp * 45) % 255
        for i in range(keyboard.num_leds):
            hue = (i * 18 + shift) % 255
            if hue < 85:
                keyboard.leds[i] = (hue * 3, 255 - hue * 3, 0, 0)
            elif hue < 170:
                hue -= 85
                keyboard.leds[i] = (255 - hue * 3, 0, hue * 3, 0)
            else:
                hue -= 170
                keyboard.leds[i] = (0, hue * 3, 255 - hue * 3, 0)
                
    elif led_modes[current_mode] == "Wave Motion":
        wave_speed = timestamp * 2.0
        for i, (x, y) in enumerate(keyboard.led_positions):
            intensity = int((math.sin(wave_speed + (x * 0.8) + (y * 0.5)) + 1) * 127)
            keyboard.leds[i] = (0, intensity // 2, intensity, 0)
            
    elif led_modes[current_mode] == "Sunlight Ripple":
        shimmer = timestamp * 1.2
        for i, (x, y) in enumerate(keyboard.led_positions):
            glow = int((math.sin(shimmer + x + y) + 1) * 80)
            keyboard.leds[i] = (0, glow // 2, glow, 0)

    keyboard.leds.show()

def process_hardware_events():
    global current_mode, last_button_state
    button_now = encoder_button.value
    
    if not button_now and last_button_state:
        current_mode = (current_mode + 1) % len(led_modes)
        keyboard.leds.fill((0, 0, 0, 0))
        keyboard.leds.show()
        time.sleep(0.04) # Hardware debounce
        
    last_button_state = button_now

if __name__ == "__main__":
    while True:
        keyboard.go()
        process_hardware_events()
        
        # Non-blocking render loop
        current_tick = time.monotonic()
        if current_tick - last_led_tick > led_frame_rate:
            calculate_lighting_effects()
            last_led_tick = current_tick
