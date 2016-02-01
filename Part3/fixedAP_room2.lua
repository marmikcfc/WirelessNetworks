file = io.open("distanceStats_fixed_room1.txt", "w")
rssiInfo = Field.new("radiotap.dbm_antsignal")
rssiNoise=Field.new("radiotap.db_antnoise")
channelInfo=Field.new("radiotap.channel.freq")
    packets = 0
    sumDistance =0
    sumStrength=0
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

                 local rssiInt= tonumber(rssistr)
                 local chInt= tonumber(channelString)

                 local distance = math.pow(10,(27.55 - 20*math.log10(chInt)+math.abs(rssiInt))/20)
                 print("distance" .. distance)
                 
                 sumDistance=sumDistance + tonumber(distance)
                 sumStrength=sumStrength+rssiInt
                
                if(distance < 1.5000) then
                    room= "Living Room"
                end

                if(distance > 2.10 ) then
                    room= "Kitchen"
                end

                if(distance > 1.8 && distance < 2.10 ) then
                    room= "Bedroom 2"
                end

                if(distance > 1.500 && distance < 1.8 ) then
                    room= "Bedroom 1"
                end

                file:write( rssistr ..  "          " .. channelString .. "          " .. distance.. " ".. room .. "\n")
                file:write()

        end
        function tap.draw()
            -- print("Packets to/from 78:71:9c:a0:74:55",packets)
            file:write("\n Number of Packets is " .. packets)
            local avgStrength = sumStrength/packets
            local avgDistance = sumDistance/packets
            file:write("\n Average Strength " .. avgStrength .. " Average Distance " .. avgDistance)
            file:close()
        end
    end
    init_listener()