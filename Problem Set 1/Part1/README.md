# Part 1: Wireshark setup and basic Lua programming (30 points)

Parser Directory 
============
A simple parser written in node.js to remove duplicate enteries from the captured packets and convert text file to JSON s that it is easier to draw graphs.

Installation 
============

`` cd nodejs_line_parsing && sudo npm install ``

Running  
============

`` node parse.js ``


Chart Directory 
============
Consists of the HTML file for graphs

Running Charts 
============
Spin off a Local Server server. Example `` npm install -g http-server && http-server ``

Running the Lua Listener 
============
`` tshark -X lua_script:myListener.lua ``