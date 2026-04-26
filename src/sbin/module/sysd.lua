if #arg < 1 then
    print("Error: usage: run sysd <action> <service>")
    os.exit(1)
end

local action = arg[1]
local service = arg[2]

local cmd
if action == "on" then
    cmd = "systemctl --user enable " .. service
elseif action == "off" then
    cmd = "systemctl --user disable " .. service
else
    error("Error: unknown subcommand: " .. action)
end

local result = os.execute(cmd)

if result then
    print("[OK] " .. action .. " " .. service)
else
    print("[FAIL] " .. action .. " " .. service)
end
