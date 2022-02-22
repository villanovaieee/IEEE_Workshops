
Collisions = {}

function Collisions:update(dt)
    for i=#Missiles, 1, -1 do
        local missile = Missiles[i]
        if Collisions:outOfBounds(missile, width, 0, height, 0) then
            table.remove(Missiles, i)
            goto continue
        end
        for j=#Asteroids, 1, -1 do
            local asteroid = Asteroids[j]
            if Collisions:circle(missile, asteroid) then
                table.remove(Missiles, i)    
                table.remove(Asteroids,j)
                break 
            end
            if Collisions:outOfBounds(asteroid, width + ASTEROID_SPAWN_THRESHOLD, -ASTEROID_SPAWN_THRESHOLD,
                    height + ASTEROID_SPAWN_THRESHOLD, -ASTEROID_SPAWN_THRESHOLD) then
                table.remove(Asteroids, j)
            end
        end
        ::continue::
    end
end

function Collisions:outOfBounds(object, xMax, xMin, yMax, yMin)
    return object.x > xMax or object.x < xMin or
        object.y > yMax or object.y < yMin
end

function Collisions:circle(circle1, circle2)
    return math.sqrt((circle2.x-circle1.x)^2 + (circle2.y-circle1.y)^2) <= (circle1.r + circle2.r)
end

function Collisions:AABB(x1, y1, w1, h1, x2, y2, w2, h2)
    return  x1 < x2 + w2 and
            x1 + w1 > x2 and
            y1 < y2 + h2 and
            y1 + h1 > y2
end