local love = require('love')

Missiles = {}
MISSILE_SPEED = 200
MOUSE_DEBOUNCE = false

function Missiles:update(dt)
    for i=#Missiles, 1, -1 do
        local missile = Missiles[i]
        missile.x = missile.x + missile.speedX * dt
        missile.y = missile.y + missile.speedY * dt
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

function Missiles:draw()
    love.graphics.setColor(love.math.colorFromBytes(255, 255, 255))
    for i=1, #Missiles, 1 do
        local missile = Missiles[i]
        love.graphics.circle("fill", missile.x, missile.y, missile.r)
    end
end