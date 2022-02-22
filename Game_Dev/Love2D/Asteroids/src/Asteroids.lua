local love = require('love')

ASTEROID_SPEED = MISSILE_SPEED/2
ASTEROID_SPAWN_THRESHOLD = 100
Asteroids = {}

function Asteroids:update(dt)
    for i=#Asteroids, 1, -1 do
        local asteroid = Asteroids[i]
        asteroid.x = asteroid.x + asteroid.speedX * dt
        asteroid.y = asteroid.y + asteroid.speedY * dt
        if Collisions:AABB(Player.x, Player.y, Player.size, Player.size, asteroid.x, asteroid.y, asteroid.r, asteroid.r) then
            love.event.quit(0)
        end
    end

    if math.random() < 0.05 then
        local asteroid = {}
        asteroid.r = 20
        asteroid.x = math.random(-ASTEROID_SPAWN_THRESHOLD, width + ASTEROID_SPAWN_THRESHOLD)
        if asteroid.x > 0 and asteroid.x < width then
            -- y must be out of bounds because x is in bounds
            if math.random() < 0.5 then
                asteroid.y = math.random(height, height + ASTEROID_SPAWN_THRESHOLD)
            else
                asteroid.y = math.random(-ASTEROID_SPAWN_THRESHOLD, 0)
            end
        else
            -- y can be anywhere because x is out of bounds
            asteroid.y = math.random(-ASTEROID_SPAWN_THRESHOLD, height + ASTEROID_SPAWN_THRESHOLD)
        end
        local theta_asteroid = math.atan((asteroid.y - Player.y) / (asteroid.x - Player.x))
        if asteroid.x < Player.x then
            asteroid.speedY = math.sin(theta_asteroid) * ASTEROID_SPEED
            asteroid.speedX = math.cos(theta_asteroid) * ASTEROID_SPEED
        else
            asteroid.speedY = math.sin(theta_asteroid) * -ASTEROID_SPEED
            asteroid.speedX = math.cos(theta_asteroid) * -ASTEROID_SPEED
        end

        table.insert(Asteroids, asteroid)
    end
end

function Asteroids:draw()
    love.graphics.setColor(love.math.colorFromBytes(100, 255, 100))
    for i=1, #Asteroids, 1 do
        local asteroid = Asteroids[i]
        love.graphics.circle("line", asteroid.x, asteroid.y, asteroid.r)
    end
end