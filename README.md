# watch-face-wearfit
 
 A collection of watch face binary files.

 ## Collection

 - [`dials/D18Max`](dials/D18Max/README.md)
 - [`dials/HW19`](dials/HW19/README.md)
 - [`dials/HW21`](dials/HW21/README.md)
 - [`dials/HW22`](dials/HW22/README.md)
 - [`dials/HW22+`](dials/HW22+/README.md)
 - [`dials/M16mini`](dials/M16mini/README.md)
 - [`dials/mibro_air`](dials/mibro_air/README.md)
 - [`dials/others`](dials/others/README.md)
 - [`dials/X5Pro`](dials/X5Pro/README.md)
 - [`dials/X8Ultra`](dials/X8Ultra/README.md)

## Other sources

- [`Chronos online watchfaces`](https:chronos.ke/dials)
- [`4PDA forum - Watch faces for the Chronos app`](https://4pda.to/forum/index.php?showtopic=1075503)


## Compatibilities 
- HW22+ and D18Max dials tested and working for HW57 Pro.
- Do not try to install X8Ultra dials in HW57 Pro; this will reboot your watch in loop.

## Installation
 
 They can be installed using Chronos app
 
 <a href='https://play.google.com/store/apps/details?id=com.fbiego.chronos'><img alt='Get it on Google Play' height="100px" src='https://play.google.com/intl/en_us/badges/static/images/badges/en_badge_web_generic.png'/></a>


> **Warning**
> Install faces at your own risk as they may not be compatible with your watch


## Tools

Chronos v2.4.0+ allows you to extract binary watchfaces. When extracting, the watchface resources will be saved as images. If you make any edits to these images, you can then pack them back into a binary watchface.

- Extract the resources to a folder
`java -jar imager.jar 24_2_dial.bin`

- Create a watch face preview image from a bin file
`java -jar watchface.jar 24_2_dial.bin`

- Resize the dial. Specify the original and final size (by width)
`py resizer.pyc 24_2_dial.bin 240 360`
