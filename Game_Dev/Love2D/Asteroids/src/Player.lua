local love = require('love')

Player = {}

function Player:load()
    Player.size = 20
    Player.x = 400
    Player.y = 400
    Player.polygon = {}
    Player.maxSpeed = 2000
    Player.throttle = 10
    Player.speedX = 0
    Player.speedY = 0
end

function Player:update(dt)
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

    Player.x = Player.x + Player.speedX * dt
    Player.y = Player.y + Player.speedY * dt

    if Player.x > width then
        Player.x = 0
    elseif Player.x < 0 then
        Player.x = width - Player.size
    end
    if Player.y > height then
        Player.y = 0
    elseif Player.y < 0 then
        Player.y = height - Player.size
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
end

function Player:draw()
    love.graphics.setColor(love.math.colorFromBytes(255, 100, 100))
    love.graphics.polygon("fill", Player.polygon)
end