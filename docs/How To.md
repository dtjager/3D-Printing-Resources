---
Title: How To's (updates pending)
---
#### Building
- Voron [Sourcing and Buying FAQ](https://docs.vorondesign.com/sourcing_faq.html) - super helpful for buying anything that will be used for 3d printer parts/builds
- voron mechanical assembly [tips](https://docs.vorondesign.com/build/mechanical/) - helpful tips for building, and general considerations for maintenance time

#### Software
- [Kiauh](https://github.com/dw-0/kiauh) - simplified install of multiple services
- [SSH](https://github.com/VoronDesign/Voron-Documentation/blob/main/build/software/ssh.md) - basics and setup (TIP: Use a memorable hostname when flashing SD card such as "voron", you can ssh into it then at "voron.local" without needing to know the IP adress
- [Boot raspberry pi from SSD](https://www.makeuseof.com/how-to-boot-raspberry-pi-ssd-permanent-storage/) - if you already have a setup running off of SD, you can clone the SSD from that.
- [KlipperScreen](https://klipperscreen.github.io/KlipperScreen/Installation/) installation (can be done via Kiauh) - installation and setup of klipperscreen, also includes directions for installing on an android phone
- [Raspberry Pi Camera Module](https://www.raspberrypi.com/documentation/accessories/camera.html)
- Webcam in [Fluidd](https://docs.fluidd.xyz/features/cameras) - supports most USB webcams (may require [crowsnest](https://docs.fluidd.xyz/features/cameras#crowsnest-support))
- Webcam in [Mainsail](https://docs.mainsail.xyz/overview/settings/webcams) - supports most USB webcams (may require [crowsnest](https://crowsnest.mainsail.xyz/))
      
#### Tuning
- [USB input shaper](https://www.youtube.com/watch?v=W_VHbT_tsZw&t=584s)
- [Sensorless Homing](https://github.com/VoronDesign/Voron-Documentation/blob/main/community/howto/clee/sensorless_xy_homing.md)

#### Klipper / Moonraker Integrations
- Integrate other servies with [Moonraker](https://moonraker.readthedocs.io/en/latest/configuration/)
- [Klipper-Backup](https://staubgeborener.github.io/klipper-backup/) - backup your printer config to a repo. Helpful if you need to go back to a working state.
- Klipper [KAMP](https://github.com/kyleisah/Klipper-Adaptive-Meshing-Purging) - Klipper Adaptive Meshing Purging, bed mesh of only where printed parts will be.
- Install [Klipper](https://www.obico.io/blog/install-klipper-ender-3/) on a non-klipper printer - Ender 3 in this guide, basics will be the same
- Use [WLED](https://kno.wled.ge/) within Klipper - [Tutorial 1](https://github.com/dtjager/3D-Printing-Resources/blob/main/misc%20pages/WLED.md), [Tutorial 2](https://github.com/Gliptopolis/WLED_Klipper)
- Use [Moonraker Timelapse](https://github.com/mainsail-crew/moonraker-timelapse) to get timelapse footage of prints using a camera connected to your printer
- Use Raspberry Pi GPIO with [Klipper](https://www.klipper3d.org/RPi_microcontroller.html)

#### Youtube Resources
Many build streams in the below for many different printers. Also a great resource for specific how to videos.
- [CNC Kitchen](https://www.youtube.com/@CNCKitchen) - 3d printer technology research, comparison and testing
- [Made with Layers](https://www.youtube.com/@MadeWithLayers) - a few build streams, comparison and testing
- [Makers Muse](https://www.youtube.com/@MakersMuse) - general 3d printing applications, how to
- [Mandic Really](https://www.youtube.com/@MandicReally) - modifications, builds, applications of 3D prints
- [Maple Leaf Makers](https://www.youtube.com/@MapleLeafMakers/featured) - short, to the point video's of modifications and build's/how to's
- [Modbot](https://www.youtube.com/@ModBotArmy) - modifications, how to videos, reviews
- [Nero3D](https://www.youtube.com/@CanuckCreator) - modifications, how to videos, reviews, build streams
- [Steve Builds](https://www.youtube.com/@SteveBuilds) - build and modification streams
- [Teaching Tech](https://www.youtube.com/@TeachingTech) - Build logs, how to videos. Great resrouce for all skill levels.
