local love = require('love')
local math = require('math')

function love.load()
    MISSILE_SPEED = 200
    MOUSE_DEBOUNCE = false
    -- love.graphics.setBackgroundColor(love.math.colorFromBytes(169, 169, 169))
    -- love.mouse.setVisible(false)
    Player = {}
    Player.size = 20
    Player.x = 400
    Player.y = 400
    Player.polygon = {}
    Player.maxSpeed = 2000
    Player.throttle = 10
    Player.speedX = 0
    Player.speedY = 0

    Missiles = {}
end

function love.update(dt)
    local ds = 4
    local mouse_x, mouse_y = love.mouse.getPosition()
    local theta = math.atan((mouse_y - Player.y) / (mouse_x - Player.x))
    if love.keyboard.isDown('up', 'w') and Player.speedY > -Player.maxSpeed then
        Player.speedY = Player.speedY - Player.throttle
    elseif Player.speedY < 0 then
        Player.speedY = Player.speedY + Player.throttle
    end
    if love.keyboard.isDown('down', 's') and Player.speedY < Player.maxSpeed then
        Player.speedY = Player.speedY + Player.throttle
    elseif Player.speedY > 0 then
        Player.speedY = Player.speedY - Player.throttle
    end
    if love.keyboard.isDown('right', 'd') and Player.speedX < Player.maxSpeed then
        Player.speedX = Player.speedX + Player.throttle
    elseif (Player.speedX > 0) then
        Player.speedX = Player.speedX - Player.throttle
    end
    if love.keyboard.isDown('left', 'a') and Player.speedX > -Player.maxSpeed then
        Player.speedX = Player.speedX - Player.throttle
    elseif Player.speedX < 0 then
        Player.speedX = Player.speedX + Player.throttle
    end

    -- if (math.abs(Player.speedX) > Player.throttle) then
    --     Player.speedX = 0
    -- end
    -- if (math.abs(Player.speedY) < Player.throttle) then
    --     Player.speedY = 0
    -- end

    Player.x = Player.x + Player.speedX * dt
    Player.y = Player.y + Player.speedY * dt

    if Player.x > love.graphics.getWidth() then
        Player.x = 0
    elseif Player.x < 0 then
        Player.x = love.graphics.getWidth() - Player.size
    end
    if Player.y > love.graphics.getHeight() then
        Player.y = 0
    elseif Player.y < 0 then
        Player.y = love.graphics.getHeight() - Player.size
    end

    if mouse_x > Player.x then
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

    for i=#Missiles, 1, -1 do
        local missile = Missiles[i]
        missile.x = missile.x + missile.speedX * dt
        missile.y = missile.y + missile.speedY * dt
        if  missile.x > love.graphics.getWidth() or missile.x < 0 or
            missile.y > love.graphics.getHeight() or missile.y < 0 or
            AABB(Player.x, Player.y, Player.size, Player.size, missile.x, missile.y, missile.r, missile.r) then
           table.remove(Missiles, i)     
        end
    end

    if love.mouse.isDown(1) and not MOUSE_DEBOUNCE then
        MOUSE_DEBOUNCE = true
        local missile = {}
        missile.x = Player.polygon[1]
        missile.y = Player.polygon[2]
        missile.r = 3
        if mouse_x > Player.x then
            missile.speedY = math.sin(theta) * MISSILE_SPEED
            missile.speedX = math.cos(theta) * MISSILE_SPEED
        else
            missile.speedY = math.sin(theta) * -MISSILE_SPEED
            missile.speedX = math.cos(theta) * -MISSILE_SPEED
        end

        table.insert(Missiles, missile)
    elseif MOUSE_DEBOUNCE and not love.mouse.isDown(1) then
        MOUSE_DEBOUNCE = false
    end
end

function love.draw()
    love.graphics.setColor(love.math.colorFromBytes(255, 100, 100))
    love.graphics.polygon("fill", Player.polygon)
    love.graphics.setColor(love.math.colorFromBytes(255, 255, 255))
    for i=1, #Missiles, 1 do
        local missile = Missiles[i]
        love.graphics.circle("fill", missile.x, missile.y, missile.r)
    end
end

function AABB(x1, y1, w1, h1, x2, y2, w2, h2)
    return  x1 < x2 + w2 and
            x1 + w1 > x2 and
            y1 < y2 + h2 and
            y1 + h1 > y2
end
