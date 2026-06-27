<h1 align="center">Macropad</h1> 
<div align="center">         
<p align="center">
        <img width="1227" height="609" alt="Screenshot 2026-06-27 155121" src="https://github.com/user-attachments/assets/6d557070-477f-4478-b6bc-b9d7981f9a5a" />


A custom 6-key custom macropad with a rotary encoder, Cherry MX red mechanical switches, a custom PCB, and a 3D-printed case to take your workflow to the next level.
</p>

<h1 align="center">Overview</h1>
        
<p align="center">This project is a custom desktop macropad built around the RP2040-Zero. It includes 6 Cherry MX Red mechanical switches for satisfying tactile sounds while clocking, a KY-040 rotary encoder for volume or scroll control, a custom-designed PCB, and a sleek 3D-printed two-part enclosure. 

# Repository Contents

| Path | What it contains |
| --- | --- |
| [`3D_PRINTS`](https://github.com/Ragh7av/Macropad/tree/main/3D_PRINTS) | STL files for quick access to 3D printing the top and bottom enclosure halves |
| [`ASSEMBLY`](https://github.com/Ragh7av/Macropad/tree/main/ASSEMBLY) | Files related to the mechanical assembly of the macropad |
| [`BOM`](https://github.com/Ragh7av/Macropad/tree/main/BOM) | Bill of materials details and cost breakdowns |
| [`FIRMWARE`](https://github.com/Ragh7av/Macropad/tree/main/FIRMWARE) | Firmware code (C++/CircuitPython/KMK) to program the keys and encoder |
| [`GERBERS`](https://github.com/Ragh7av/Macropad/tree/main/GERBERS) | Ready-to-manufacture Gerber files for fabricating the PCB |
| [`IMAGES`](https://github.com/Ragh7av/Macropad/tree/main/IMAGES) | Photos and screenshots of the project |
| [`PCB`](https://github.com/Ragh7av/Macropad/tree/main/PCB) | KiCad schematic and PCB layout files |
| [`ZINE`](https://github.com/Ragh7av/Macropad/tree/main/ZINE) | Project zine documentation |
| [`CAD`](CAD) | Project 3D models |


<h1 align="center">Why am I even building this?</h1>
<p align="center">
 I built this project as a part of an event called <a href="https://fallout.hackclub.com">Fallout</a>, organized by a non-profit organization called <a href="https://hackclub.com">Hack Club</a>. We build and ship hardware projects, and for that, we get some cool gifts and grants to build it IRL. After building hardware projects for 60 hours, we get invited to Shenzhen, China for a Hardware Hackathon. I am building this project to work toward those 60 hours.
 </p>

<h1 align="center">Why Macropad?</h1>

So I spend a lot of time at my desk doing coding, editing, and general productivity tasks. I frequently need quick access to specific shortcuts, media controls, and repetitive keystrokes that are tedious to execute on a standard keyboard. I created this project  to solve these problems and help myself get supercalifragilisticexpialidocious in building super cool hardware things while optimizing my workflow. 

# Printed Circuit Board (PCB)
<img width="971" height="743" alt="Screenshot 2026-06-26 000245" src="https://github.com/user-attachments/assets/02853779-7786-4a73-9b53-1997e27afc15" />
<img width="901" height="1218" alt="Screenshot 2026-06-19 184742" src="https://github.com/user-attachments/assets/74055cd5-8187-4b33-90cc-c5799737afd4" />
<img width="635" height="892" alt="Screenshot 2026-06-19 180719" src="https://github.com/user-attachments/assets/b1feaf1c-b280-45a0-a10d-3096bfab63ef" />



#  Schematic
<img width="1135" height="802" alt="Screenshot 2026-06-20 071409" src="https://github.com/user-attachments/assets/4cb8c0be-a65d-4fc0-900d-11ed79619b9e" />

# CAD
<img width="1048" height="717" alt="Screenshot 2026-06-20 013928" src="https://github.com/user-attachments/assets/cbfb144e-bc22-42ce-9304-baab9ddb0db8" />
<img width="1357" height="750" alt="Screenshot 2026-06-20 013915" src="https://github.com/user-attachments/assets/ee37f271-5a66-4c06-9d9b-6f265bb73e56" />
<img width="532" height="639" alt="Screenshot 2026-06-20 014014" src="https://github.com/user-attachments/assets/a207c6df-bf49-47ed-b726-340ad69b32f7" />
<img width="953" height="875" alt="Screenshot 2026-06-20 013951" src="https://github.com/user-attachments/assets/53e9352d-ee8c-4115-8e5f-156219ecaee2" />
<img width="901" height="511" alt="Screenshot 2026-06-20 013946" src="https://github.com/user-attachments/assets/4e2b0890-cb41-4b7c-aa72-2057185514b1" />
<img width="1032" height="737" alt="Screenshot 2026-06-20 013938" src="https://github.com/user-attachments/assets/f7d45607-529d-45dd-9afe-58fbaca4b5bd" />

<h1 align="center">The Features</h1>
</div>

1. **6 Programmable Keys**: Features 6 Cherry MX Red linear mechanical switches for smooth, fast, and customizable keystrokes (copy/paste, media navigation, macro strings, etc.).
2. **Rotary Encoder**: Includes a built-in KY-040 rotary encoder with a push-button function, perfect for controlling system volume, zooming, or scrolling through timelines.
3. **Custom PCB**: A printed circuit board routing the switches and encoder directly to the RP2040-Zero while looking beautiful with a custom silkscreen designs.
4. **RP2040-Zero Brains**: Powered by the compact Raspberry Pi RP2040-Zero microcontroller, ensuring fast response times and easy programmability.
5. **3D Printed Enclosure**: A custom-designed two-part (top and bottom) FDM 3D-printed case to keep the electronics safe and look great on a desk.

<div align="center">   


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

