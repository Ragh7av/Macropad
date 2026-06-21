<h1 align="center">Macropad</h1> 
<div align="center">         
<p align="center">
A compact 6-key custom macropad featuring a rotary encoder, mechanical switches, a custom PCB, and a 3D-printed case to streamline your workflow.
</p>

<h1 align="center">Overview</h1>
        
<p align="center">This project is a custom desktop macropad built around the compact but powerful RP2040-Zero. It includes 6 Cherry MX Red mechanical switches for satisfying tactile inputs, a KY-040 rotary encoder for volume or scroll control, a custom-designed PCB, and a sleek 3D-printed two-part enclosure. 

<h1 align="center">Why am I even building this?</h1>
<p align="center">
 I built this project as a part of an event called <a href="https://fallout.hackclub.com">Fallout</a>, organized by a non-profit organization called <a href="https://hackclub.com">Hack Club</a>. We build and ship hardware projects, and for that, we get some cool gifts and grants to build it IRL. After building hardware projects for 60 hours, we get invited to Shenzhen, China for a Hardware Hackathon. I am building this project to work toward those 60 hours.
 </p>

<h1 align="center">Why Macropad?</h1>

So I spend a lot of time at my desk doing coding, editing, and general productivity tasks. I frequently need quick access to specific shortcuts, media controls, and repetitive keystrokes that are tedious to execute on a standard keyboard. I created this project (which is also my first custom PCB hardware project) to solve these problems and help myself get supercalifragilisticexpialidocious in building super cool hardware things while optimizing my workflow. 

<h1 align="center">The Features</h1>
</div>

1. **6 Programmable Keys**: Features 6 Cherry MX Red linear mechanical switches for smooth, fast, and customizable keystrokes (copy/paste, media navigation, macro strings, etc.).
2. **Rotary Encoder**: Includes a built-in KY-040 rotary encoder with a push-button function, perfect for controlling system volume, zooming, or scrolling through timelines.
3. **Custom PCB**: A clean, purpose-built printed circuit board routing the switches and encoder directly to the RP2040-Zero.
4. **RP2040-Zero Brains**: Powered by the compact Raspberry Pi RP2040-Zero microcontroller, ensuring fast response times and easy programmability.
5. **3D Printed Enclosure**: A custom-designed two-part (top and bottom) FDM 3D-printed case to keep the electronics safe and look great on a desk.

<div align="center">   
 
# Repository Contents

| Path | What it contains |
| --- | --- |
| [`3D_PRINTS`](https://github.com/Ragh7av/Macropad/tree/main/3D_PRINTS) | Editable CAD/STL files for 3D printing the top and bottom enclosure halves |
| [`ASSEMBLY`](https://github.com/Ragh7av/Macropad/tree/main/ASSEMBLY) | Files related to the mechanical assembly of the macropad |
| [`BOM`](https://github.com/Ragh7av/Macropad/tree/main/BOM) | Bill of materials details and cost breakdowns |
| [`FIRMWARE`](https://github.com/Ragh7av/Macropad/tree/main/FIRMWARE) | Firmware code (C++/CircuitPython/KMK) to program the keys and encoder |
| [`GERBERS`](https://github.com/Ragh7av/Macropad/tree/main/GERBERS) | Ready-to-manufacture Gerber files for fabricating the PCB |
| [`IMAGES`](https://github.com/Ragh7av/Macropad/tree/main/IMAGES) | Photos and screenshots of the project |
| [`PCB`](https://github.com/Ragh7av/Macropad/tree/main/PCB) | KiCad schematic and PCB layout files |
| [`ZINE`](https://github.com/Ragh7av/Macropad/tree/main/ZINE) | Project zine documentation |

</div>

# The Components Used

1. RP2040-Zero (Raspberry Pi Microcontroller)
2. KY-040 Rotary Encoder Module
3. Cherry MX RED mechanical switches (x6)
4. PBT DSA Blank Keycaps for MX Switches (x6)
5. Custom Printed Circuit Board (PCB)
6. 3D Printed Case (Top and Bottom halves)

# Bill of Materials

| Component Name | Quantity | Price (₹) | Total Cost (₹) | Shipping (₹) | Total Price (₹) |
| --- | --- | --- | --- | --- | --- |
| PCB (Robu PCB Manufacturing) | 1 | ₹180 | ₹900 | ₹49 | ₹949 |
| Keycaps for MX keys (ATORSE 12Pcs Blank) | 6 | ₹52.25 | ₹627 | Free | ₹627 |
| Cherry MX RED mechanical keys | 6 | ₹44.9 | ₹449 | Free | ₹449 |
| Raspberry Pi RP2040 Zero | 1 | ₹235 | ₹235 | ₹24.5 | ₹259.5 |
| KY-040 Rotary encoder | 1 | ₹59 | ₹59 | ₹24.5 | ₹83.5 |
| Case bottom half (at 40% infill) | 1 | ₹159 | ₹159 | ₹49.5 | ₹208.5 |
| Case top half (at 40% infill) | 1 | ₹90 | ₹90 | ₹49.5 | ₹139.5 |
| **Subtotal** | | | **₹2519** | **₹197** | **₹2716** |

# Wiring / Schematic
The wiring is heavily simplified thanks to the custom PCB! 
* **Switches (SW1 - SW6)** are connected directly to the RP2040-Zero GPIO pins. 
* **The Rotary Encoder (KY-040)** connects its Clock (CLK), Data (DT), and Switch (SW) pins to the designated GPIOs on the RP2040, utilizing the 3V3 power and GND lines. 

*(Check the `PCB` folder in the repository for the full KiCad schematic.)*

# How to Build it?

**To replicate, follow the steps below:**
1) First, grab the PCB Gerber files from the `GERBERS` folder and send them to your preferred PCB manufacturer (like Robu, JLCPCB, etc.).
2) Next, grab the 3D models from the `3D_PRINTS` folder and print the top and bottom case halves (recommended 40% infill for a solid feel).
3) Purchase the parts mentioned in the **BOM**.
4) Solder the RP2040-Zero, Cherry MX switches, and the rotary encoder onto your fabricated PCB.
5) Flash the firmware from the `FIRMWARE` folder onto your RP2040-Zero via USB-C.
6) Test the keys and encoder on your computer to ensure all keystrokes register. 
7) Assemble the PCB into the 3D-printed shell, pop on your keycaps, and secure everything together!

*Hurrahh!! You replicated the Macropad!*

## Firmware setup
 - Connect your RP2040-Zero to your computer via USB-C.
 - If using Arduino IDE: Select the appropriate RP2040 board under Tools > Board, select the Port, compile, and click Upload.
 - Customize your keybindings in the firmware code to map to your preferred macros, shortcuts, or media controls before uploading.

