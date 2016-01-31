file = io.open("distance_RSSI_550centimeters.txt", "w")
rssiInfo = Field.new("radiotap.dbm_antsignal")
channelInfo=Field.new("radiotap.channel.freq")
    packets = 0;
    local function init_listener()
        local tap = Listener.new("frame","wlan.bssid eq 78:71:9c:a0:74:55")
        function tap.reset()
            packets = 0;
        end
        function tap.packet(pinfo,tvb,ip)
            packets = packets + 1

            local rssiStrengh = rssiInfo()
            local rssistr = tostring(rssiStrengh)
            print("packet Number " .. packets)
            print(rssistr)

                local channel = channelInfo()
                local channelString = tostring(channel)
                print(channelString)

                 -- local exp = (27.55 - (20 * math.log10(tonumber(channelString)) + math.abs(tonumber(rssiStrengh)))) / 20.0
                 -- local distance = math.pow(10.0, exp)
                 -- print("distance" .. distance)
                
                file:write( rssistr .. "          " .. channelString .. "\n")
                file:write()

        end
        function tap.draw()
            -- print("Packets to/from 78:71:9c:a0:74:55",packets)
            file:write("\n Number of Packets is " .. packets)
            file:close()
        end
    end
    init_listener()