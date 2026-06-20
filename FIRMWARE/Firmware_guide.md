### Option A: KMK Firmware 
KMK is interpreted dynamically, allowing you to edit your keymaps on the fly by simply saving a text file.
1. Install [CircuitPython for the RP2040-Zero](https://circuitpython.org/board/waveshare_rp2040_zero/).
2. Copy the `kmk` folder from the [official KMK firmware repo](https://github.com/KMKfw/kmk_firmware) to the root of your mounted `CIRCUITPY` drive.
3. Drop the `kb.py` and `main.py` files from the `/KMK` folder in this repository directly onto the drive.

### Option B: QMK Firmware 
QMK provides lower-level hardware control, utilizing data-driven JSON configurations.
1. Copy the `qmk` folder into your local `qmk_firmware/keyboards/` directory.
2. Compile the firmware from your terminal:
   ```bash
   qmk compile -kb macropad -km default
