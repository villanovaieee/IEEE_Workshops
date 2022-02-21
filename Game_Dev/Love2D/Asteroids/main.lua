local love = require('love')
local math = require('math')

function love.load()
    -- love.graphics.setBackgroundColor(169, 169, 169)
    -- love.mouse.setVisible(false)
    Player = {}
    Player.size = 20
    Player.x = 400
    Player.y = 400
    Player.polygon = {}
end

function love.update(dt)
    local ds = 4
    local mouse_x, mouse_y = love.mouse.getPosition()
    local theta = math.atan((mouse_y - Player.y) / (mouse_x - Player.x))

    if (love.keyboard.isDown('up', 'w')) then
        Player.y = Player.y - ds
    elseif (love.keyboard.isDown('down', 's')) then
        Player.y = Player.y + ds
    end
    if (love.keyboard.isDown('right', 'd')) then
        Player.x = Player.x + ds
    elseif (love.keyboard.isDown('left', 'a')) then
        Player.x = Player.x - ds
    end

    if (mouse_x > Player.x) then
        Player.polygon = {
            Player.x + Player.size * math.cos(theta), Player.y + Player.size * math.sin(theta),
            Player.x + Player.size * math.cos(theta + 2 * math.pi / 3), Player.y + Player.size * math.sin(theta + 2 * math.pi / 3),
            Player.x + Player.size * math.cos(theta - 2 * math.pi / 3), Player.y + Player.size * math.sin(theta - 2 * math.pi / 3)
        }
    else
        Player.polygon = {
            Player.x - Player.size * math.cos(theta), Player.y - Player.size * math.sin(theta),
            Player.x - Player.size * math.cos(theta + 2 * math.pi / 3), Player.y - Player.size * math.sin(theta + 2 * math.pi / 3),
            Player.x - Player.size * math.cos(theta - 2 * math.pi / 3), Player.y - Player.size * math.sin(theta - 2 * math.pi / 3)
        }
    end
end

function love.draw()
    love.graphics.setColor(love.math.colorFromBytes(255, 100, 100))
    -- love.graphics.rectangle("fill", Player.x, Player.y, Player.width, Player.height)
    love.graphics.polygon("fill", Player.polygon)
end
