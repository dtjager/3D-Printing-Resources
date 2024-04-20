Here is my little tutorial on WLED with Klipper.
  1. Check out the WLED [getting started](https://kno.wled.ge/basics/getting-started/) page. Check the LED's you have, and the control board you want to use is compatible (ESP32, ESP8266, D1 Mini are supported. Others are experimental).
  2. You can install it onto your board using the online install tool. (https://install.wled.me/)
  3. Wire your LED's to your board. For a small amount of LEDs, you can power them from the board if you have sufficient power. If you have a lot, you can run a buck converter off of your PSU if necessary to inject power to the LEDs. My buck converter has power out, and a usb. I use the USB to power the D1, and the power out goes to power the LEDs.
At this point, you should have functioning LED's off of your control board via the web interface or phone app. Now we can interface with Moonraker/Klipper.
  4. In your moonraker.conf file, add the following:
     ```
        [wled controller]          #you can name your contoller here, I just made mine controller. I am not creative
        type: http
        address: 192.168.68.77     # IP of your WLED controller.
        initial_preset: 1          # the preset you want it to default to after it starts up
        chain_count: 120           # Number of LEDs you have in your string
     ```
  5. From here, lets jump back to the WLED interface. You can make and save presets for your lights. You can make them however you want, colors for status, whatever. When you save them, make sure you also use the "save to ID" and set them to a number. My default ("1" that we used above as preset) just turns on the chamber lights to white, and sets my skirt lights to green in a twinkle pattern. Set up the presets you want, then move on to the next part. In the settings tab, you can pick a default startup preset. (This is seems to be the easiest way, although there are otherways to set a startup configuration.)
  6. Now we have working LED's, presets, and (hopefully) a correct setup with moonraker. We can now add them into our printer config. Here is How I set mine up, what works best for you may be totally different. For my example, I have 4 presets. I'll add comments to the first preset so you can see what is happening, and include the others as reference.
     ```
      [gcode_macro WLED_ON]            #setup a macro that just turns on my leds, chamber lights are on and skirt is set to twinkle in preset #1
      description: Turn WLED strip on using optional preset and resets led colors
        gcode:
        {% set strip = params.STRIP|default("controller")|string %}
        {% set preset = params.PRESET|default(1)|int %}        #reference number of the preset that I made

        {action_call_remote_method("set_wled_state",
                             strip=strip,
                             state=True,
                             preset=preset)}

      [gcode_macro WLED_OFF]
      description: Turn WLED strip off using optional preset and resets led colors
        gcode:
        {% set strip = params.STRIP|default("controller")|string %}
        {% set preset = params.PRESET|default(2)|int %}

        {action_call_remote_method("set_wled_state",
                             strip=strip,
                             state=True,
                             preset=preset)}

      [gcode_macro chamber_on]
      description: Turn WLED strip in chamber on
      gcode:
        {% set strip = params.STRIP|default("controller")|string %}
        {% set preset = params.PRESET|default(3)|int %}

        {action_call_remote_method("set_wled_state",
                             strip=strip,
                             state=True,
                             preset=preset)}

      [gcode_macro skirt_on]
      description: Turn WLED strip in skirt on
      gcode:
        {% set strip = params.STRIP|default("controller")|string %}
        {% set preset = params.PRESET|default(4)|int %}

        {action_call_remote_method("set_wled_state",
                             strip=strip,
                             state=True,
                             preset=preset)}
      ```
  7. With this, you should now have macro buttons on your machine that will do what the preset is. If you set other functions, you can add them into your Print Start/End, QGL, homing macros or whatever you want.

Here is the [moonraker](https://moonraker.readthedocs.io/en/latest/configuration/#wled) reference for WLED.

Here is another writeup by [Gliptopolis](https://github.com/Gliptopolis/WLED_Klipper) on Github.

Here is my start/end code. It just calls WLED_ON and WLED_OFF. If you got fancy, you can put WLED_Homing or WLED_QGL, whatever. If you made a preset for it and added the gcode macro, you can call it where ever you want. I'm not the best with klipper so you might know a better way.
```
[gcode_macro PRINT_START]
gcode:
  # This part fetches data from your slicer. Such as bed temp, extruder temp, chamber temp and size of your printer.
  {% set target_bed = params.BED|int %}
  {% set target_extruder = params.EXTRUDER|int %}
  {% set target_chamber = params.CHAMBER|default("40")|int %}
  {% set x_wait = printer.toolhead.axis_maximum.x|float / 2 %}
  {% set y_wait = printer.toolhead.axis_maximum.y|float / 2 %}

  # Homes the printer, sets absolute positioning and updates the Stealthburner leds.
  STATUS_HOMING         # Sets SB-leds to homing-mode
  WLED_ON
  G28                   # Full home (XYZ)
  G90                   # Absolut position

  ##  Uncomment for bed mesh (1 of 2)
  BED_MESH_CLEAR       # Clears old saved bed mesh (if any)

  # Checks if the bed temp is higher than 90c - if so then trigger a heatsoak.
  {% if params.BED|int > 90 %}
    SET_DISPLAY_TEXT MSG="Bed: {target_bed}c"           # Displays info
    STATUS_HEATING                                      # Sets SB-leds to heating-mode
    M106 S255                                           # Turns on the PT-fan

    ##  Uncomment if you have a Nevermore.
    #SET_PIN PIN=nevermore VALUE=1                      # Turns on the nevermore

    G1 X{x_wait} Y{y_wait} Z15 F9000                    # Goes to center of the bed
    M190 S{target_bed}                                  # Sets the target temp for the bed
    SET_DISPLAY_TEXT MSG="Heatsoak: {target_chamber}c"  # Displays info
    TEMPERATURE_WAIT SENSOR="temperature_sensor chamber" MINIMUM={target_chamber}   # Waits for chamber to reach desired temp

  # If the bed temp is not over 90c, then it skips the heatsoak and just heats up to set temp with a 5min soak
  {% else %}
    SET_DISPLAY_TEXT MSG="Bed: {target_bed}c"           # Displays info
    STATUS_HEATING                                      # Sets SB-leds to heating-mode
    G1 X{x_wait} Y{y_wait} Z15 F9000                    # Goes to center of the bed
    M190 S{target_bed}                                  # Sets the target temp for the bed
    SET_DISPLAY_TEXT MSG="Soak for 5min"                # Displays info
  #  G4 P300000                                          # Waits 5 min for the bedtemp to stabilize
  {% endif %}

  # Heating nozzle to 150 degrees. This helps with getting a correct Z-home
  SET_DISPLAY_TEXT MSG="Hotend: 150c"          # Displays info
  M109 S150                                    # Heats the nozzle to 150c

  ##  Uncomment for V2 (Quad gantry level AKA QGL)
  SET_DISPLAY_TEXT MSG="QGL"      # Displays info
  STATUS_LEVELING                 # Sets SB-leds to leveling-mode
  quad_gantry_level               # Levels the buildplate via QGL
  G28 Z                           # Homes Z again after QGL

  ##  Uncomment for bed mesh (2 of 2)
  SET_DISPLAY_TEXT MSG="Bed mesh"    # Displays info
  STATUS_MESHING                     # Sets SB-leds to bed mesh-mode
  bed_mesh_calibrate                 # Starts bed mesh

  # Heats up the nozzle up to target via data from slicer
  SET_DISPLAY_TEXT MSG="Hotend: {target_extruder}c"             # Displays info
  STATUS_HEATING                                                # Sets SB-leds to heating-mode
  G1 X{x_wait} Y{y_wait} Z15 F9000                              # Goes to center of the bed
  M107                                                          # Turns off partcooling fan
  M109 S{target_extruder}                                       # Heats the nozzle to printing temp

  # Gets ready to print by doing a purge line and updating the SB-leds
  SET_DISPLAY_TEXT MSG="Printer goes brr"          # Displays info
  STATUS_PRINTING                                  # Sets SB-leds to printing-mode
  G0 X{x_wait - 50} Y4 F10000                      # Moves to starting point
  G0 Z0.4                                          # Raises Z to 0.4
  G91                                              # Incremental positioning 
  G1 X100 E20 F1000                                # Purge line
  G90                                              # Absolut position

[gcode_macro PRINT_END]
#   Use PRINT_END for the slicer ending script - please customise for your slicer of choice
gcode:
    # safe anti-stringing move coords
    {% set th = printer.toolhead %}
    {% set x_safe = th.position.x + 20 * (1 if th.axis_maximum.x - th.position.x > 20 else -1) %}
    {% set y_safe = th.position.y + 20 * (1 if th.axis_maximum.y - th.position.y > 20 else -1) %}
    {% set z_safe = [th.position.z + 2, th.axis_maximum.z]|min %}
    
    SAVE_GCODE_STATE NAME=STATE_PRINT_END

    M400                           ; wait for buffer to clear
    G92 E0                         ; zero the extruder
    G1 E-5.0 F1800                 ; retract filament
    
    TURN_OFF_HEATERS

    G90                                      ; absolute positioning
    G0 X{x_safe} Y{y_safe} Z{z_safe} F20000  ; move nozzle to remove stringing
    G0 X{th.axis_maximum.x//2} Y{th.axis_maximum.y - 2} F3600  ; park nozzle at rear
    M107                                     ; turn off fan
    
    BED_MESH_CLEAR
    WLED_OFF

    # The purpose of the SAVE_GCODE_STATE/RESTORE_GCODE_STATE
    # command pair is to restore the printer's coordinate system
    # and speed settings since the commands above change them.
    # However, to prevent any accidental, unintentional toolhead
    # moves when restoring the state, explicitly set MOVE=0.
    RESTORE_GCODE_STATE NAME=STATE_PRINT_END MOVE=0
```