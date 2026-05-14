if #arg < 2 then
    print("Error: usage: run ahk <binding> <script.sh>")
    print("Hint: run ahk ^T terminal.sh")
    os.exit(1)
end

local bindings = {}

function parseBinding(bindStr)
    local result = {
        ctrl = false,
        alt = false,
        shift = false,
        key = nil
    }

    -- ^T
    if bindStr:sub(1, 1) == "^" then
        result.ctrl = true
        result.key = bindStr:sub(2)
        return result
    end

    -- M-E / C-X / S-Q
    for part in bindStr:gmatch("[^-]+") do
        if part == "C" then
            result.ctrl = true
        elseif part == "M" then
            result.alt = true
        elseif part == "S" then
            result.shift = true
        else
            result.key = part
        end
    end

    return result
end

local bind = arg[1]
local script = arg[2]

function isScript()
    return script:match("%.sh$") ~= nil
end

if bindings[bind] then
    print(bind .. " already exists")
    os.exit(1)
end

bindings[bind] = function()
    local parsed = parseBinding(bind)

    print("Binding:")
    print("CTRL:", parsed.ctrl)
    print("ALT:", parsed.alt)
    print("SHIFT:", parsed.shift)
    print("KEY:", parsed.key)

    if isScript() then
        os.execute("bash " .. script)
    else
        print("Invalid script")
    end
end

bindings[bind]()
