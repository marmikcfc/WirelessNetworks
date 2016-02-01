# Part 3: Indoor Localization & Motion+Presence Detection (40 points)

nearbyAccesspoints.lua 
============
Shows the nearby Access Points. It can be executed by using 
`` tshark -X lua_script:nearbyAccesspoints.lua ``

noBeamforming.lua
================
Filters out all the packets in traffic sent with beamforming. Since, the beamformer follows the NDP Announcement with a null data packet filter wlan.fc.type_subtype != 0x15 is used to filter out packets sent with beamforming.

Running
=========
`` tshark -X lua_script:noBeamforming.lua ``

Motion + Presence Detection
=================
Motion + Presence Detection depends upon the formula 
`` distance = 10 ^ ((27.55 - (20 * log10(frequency)) + signalLevel)/20) ``
