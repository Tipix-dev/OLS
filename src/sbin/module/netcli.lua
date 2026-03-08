if #arg < 1 then
    print("Error: Please specify at least one argument")
    os.exit(1)
end


if arg[1] == "ping" then
    if not arg[2] then
        print("Error: please specify a host")
        os.exit(1)
    end
    os.execute('ping -c 5 ' .. arg[2])
elseif arg[1] == "ip" then
    os.execute("curl -s ifconfig.me")
elseif arg[1] == "route" then
    os.execute("ip route | awk '/default/ {print $3}'")
else
    print("Unknown target: " .. arg[1])
    os.exit(1)
end
    
