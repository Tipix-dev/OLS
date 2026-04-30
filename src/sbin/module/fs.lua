if #arg < 2 then
    print("Error: usage: run fs <type> <mountpoint>")
    os.exit(1)
end

local type = arg[1]
local mountpoint = arg[2]

if type == "ext4" then
    cmd = "mkfs.ext4 " .. mountpoint .. " >/dev/null"
elseif type == "xfs" then
    cmd = "mkfs.xfs " .. mountpoint .. " >/dev/null"
elseif type == "btrfs" then
    cmd = "mkfs.btrfs " .. mountpoint .. " >/dev/null"
else
    error("Error: unknown subcommand: " .. type)
end


local result = os.execute(cmd)

if result then
    print("[OK] " .. type .. " " .. mountpoint)
else
    print("[FAIL] " .. type .. " " .. mountpoint)
end
