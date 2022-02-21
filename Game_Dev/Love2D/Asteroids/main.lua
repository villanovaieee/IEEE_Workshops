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
    Player.maxSpeed = 2000
    Player.throttle = 10
    Player.friction = 20
    Player.speedX = 0
    Player.speedY = 0
end

function love.update(dt)
    local ds = 4
    local mouse_x, mouse_y = love.mouse.getPosition()
    local theta = math.atan((mouse_y - Player.y) / (mouse_x - Player.x))
    -- still slides gently due to say speed being -10 and adding friction of 20 leads to speed of 10
    if (love.keyboard.isDown('up', 'w') and Player.speedY < Player.maxSpeed) then
        Player.speedY = Player.speedY - Player.throttle
        -- Player.y = Player.y - ds
    elseif (Player.speedY < 0) then
        Player.speedY = Player.speedY + Player.friction
    end
    if (love.keyboard.isDown('down', 's') and Player.speedY > -Player.maxSpeed) then
        Player.speedY = Player.speedY + Player.throttle
        -- Player.y = Player.y + ds
    elseif (Player.speedY > 0) then
        Player.speedY = Player.speedY - Player.friction
    end
    if (love.keyboard.isDown('right', 'd') and Player.speedX < Player.maxSpeed) then
        Player.speedX = Player.speedX + Player.throttle
        -- Player.x = Player.x + ds
    elseif (Player.speedX > 0) then
        Player.speedX = Player.speedX - Player.friction
    end
    if (love.keyboard.isDown('left', 'a') and Player.speedX > -Player.maxSpeed) then
        Player.speedX = Player.speedX - Player.throttle
        -- Player.x = Player.x - ds
    elseif (Player.speedX < 0) then
        Player.speedX = Player.speedX + Player.friction
    end

    -- if (Player.speedX ~= 0 or Player.speedY ~= 0) then
    --     if (Player.speedY > 0) then
    --         Player.speedY = Player.speedY - Player.friction
    --     else
    --         Player.speedY = Player.speedY + Player.friction
    --     end
    --     if (Player.speedX > 0) then
    --         Player.speedX = Player.speedX - Player.friction
    --     else
    --         Player.speedX = Player.speedX + Player.friction
    --     end
    -- end

    if (math.abs(Player.speedX) > Player.throttle) then
        Player.speedX = 0
    end
    if (math.abs(Player.speedY) < Player.throttle) then
        Player.speedY = 0
    end

    Player.x = Player.x + Player.speedX * dt
    Player.y = Player.y + Player.speedY * dt

    if (Player.x + Player.size > love.graphics.getWidth()) then
        Player.x = love.graphics.getWidth() - Player.size
        Player.speedX = 0
    elseif (Player.x -Player.size <= 0) then
        Player.x = Player.size
        Player.speedX = 0
    end
    if (Player.y + Player.size > love.graphics.getHeight()) then
        Player.y = love.graphics.getHeight() - Player.size
        Player.speedY = 0
    elseif (Player.y - Player.size <= 0) then
        Player.y = Player.size
        Player.speedY = 0
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
    love.graphics.print(Player.speedX, 10, 10)
    love.graphics.print(Player.speedY, 10, 30)
end
