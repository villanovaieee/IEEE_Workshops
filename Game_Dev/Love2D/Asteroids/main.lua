local love = require('love')
require('src/Player')
require('src/Missiles')
require('src/Asteroids')
require('src/Collisions')

function love.load()
    -- love.graphics.setBackgroundColor(love.math.colorFromBytes(169, 169, 169))
    love.mouse.setVisible(false)
    math.randomseed(os.time())
    Player:load()
end

function love.update(dt)
    mouse_x, mouse_y = love.mouse.getPosition()
    theta = math.atan((mouse_y - Player.y) / (mouse_x - Player.x))
    width = love.graphics.getWidth()
    height = love.graphics.getHeight()

    Player:update(dt)
    Missiles:update(dt)
    Asteroids:update(dt)
    Collisions:update(dt)
end

function love.draw()
    Player:draw()
    Missiles:draw()
    Asteroids:draw()
end
