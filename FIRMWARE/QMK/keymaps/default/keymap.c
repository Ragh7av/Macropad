#include QMK_KEYBOARD_H

const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {
    [0] = LAYOUT(
        KC_MRWD, KC_MPLY, KC_MFFD,    
        KC_MSEL, KC_CALC, LCMD(KC_R), 
        KC_LEFT, KC_RGHT, LCMD(KC_L)  
    )
};

// Rotary Encoder Polling
bool encoder_update_user(uint8_t index, bool clockwise) {
    if (index == 0) {
        if (clockwise) {
            tap_code(KC_VOLU);
        } else {
            tap_code(KC_VOLD);
        }
    }
    return false;
}

// Encoder Button Mapping to RGB Engine
void matrix_scan_user(void) {
    static pin_t sw_pin = GP28;
    static bool last_state = true;

    bool current_state = gpio_read_pin(sw_pin);
    if (!current_state && last_state) {
        rgblight_step(); 
        wait_ms(50); // Simple mechanical debounce logic 
    }
    last_state = current_state;
}

void keyboard_post_init_user(void) {
    setPinInputHigh(GP28); // Force internal pull-up on the encoder switch
}
