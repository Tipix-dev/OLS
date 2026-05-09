if #arg < 2 then
    print("Error: usage: run fs <type> <mountpoint>")
    os.exit(1)
end

local type = arg[1]
local mountpoint = arg[2]
local cmd

if type == "ext4" then
    cmd = "mkfs.ext4 " .. mountpoint
elseif type == "xfs" then
    cmd = "mkfs.xfs " .. mountpoint
elseif type == "btrfs" then
    cmd = "mkfs.btrfs " .. mountpoint
else
    print("Error: unknown subcommand: " .. type)
    os.exit(1)
end


local result = os.execute(cmd)

if result then
    print("[OK] " .. type .. " " .. mountpoint)
else
    print("[FAIL] " .. type .. " " .. mountpoint)
end
