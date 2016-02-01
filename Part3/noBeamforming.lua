file = io.open("noBeamforming.txt", "w")

ssidInfo = Field.new("wlan_mgt.ssid")




-- create a listener tap.  By default it creates one for "frame", but we're tapping IP layer.
-- Valid values can be any protocol with tapping support, but to get something useful in the
-- "extractor" argument of the tap's 'apcket' function callback (the third argument passed by
-- wireshark into it), it has to be one of the following currently: 
-- "actrace", "ansi_a", "ansi_map", "bacapp", "eth", "h225", "http", "ip", "ldap", 
-- "smb", "smb2", "tcp", "udp", "wlan", and "frame"
local tap = Listener.new("wlan",("wlan.fc.type_subtype != 0x15 && wlan.fc.type_subtype != 0x0e")) 


-- we will be called once for every IP Header.
-- If there's more than one IP header in a given packet we'll dump the packet once per every header
function tap.packet(pinfo,tvb,tapdata)
    print(" ")
  --  print("In packets")
    
    -- local flags = radiotap_present();
    -- if(flags) then
    --     print("Radiotap SSI present")
    -- end

    -- local rssiStrengh = rssiInfo()
    -- local rssistr = tostring(rssiStrengh)
    -- print(rssistr)

    -- local channel = channelInfo()
    -- local channelString = tostring(channel)
    -- print(channelString)

    local ssid = ssidInfo()
    local ssidString = tostring(ssid)
    print(ssidString)
    print(" ")

    if(ssidString) then
        file:write(ssidString .. "\n")
        file:write()
    end

end

function tap.draw()
--    print("draw called")

     file:close()
end

-- a listener tap's reset function is called at the ned of a live capture run,
-- when a file is opened, or closed.  Tshark never appears to call it.
function tap.reset()
--    print("reset called")

end