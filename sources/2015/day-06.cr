require "../utiles"

data = get_input(2015, 6)

def turn_on(grid, x_from, y_from, x_to, y_to)
  (x_from..x_to).each do |x|
    (y_from..y_to).each do |y|
      grid[x][y] = 1
    end
  end
end

def turn_off(grid, x_from, y_from, x_to, y_to)
  (x_from..x_to).each do |x|
    (y_from..y_to).each do |y|
      grid[x][y] = 0
    end
  end
end

def toggle(grid, x_from, y_from, x_to, y_to)
  (x_from..x_to).each do |x|
    (y_from..y_to).each do |y|
      grid[x][y] = grid[x][y] == 1 ? 0 : 1
    end
  end
end

def part1(data)
  grid = Array.new(1000) { Array.new(1000, 0) }
  data.split("\n").each do |line|
    if line.includes?("turn on")
      x_from, y_from = line.split(" ")[2].split(",").map(&.to_i)
      x_to, y_to = line.split(" ")[4].split(",").map(&.to_i)
      turn_on(grid, x_from, y_from, x_to, y_to)
    elsif line.includes?("turn off")
      x_from, y_from = line.split(" ")[2].split(",").map(&.to_i)
      x_to, y_to = line.split(" ")[4].split(",").map(&.to_i)
      turn_off(grid, x_from, y_from, x_to, y_to)
    else
      x_from, y_from = line.split(" ")[1].split(",").map(&.to_i)
      x_to, y_to = line.split(" ")[3].split(",").map(&.to_i)
      toggle(grid, x_from, y_from, x_to, y_to)
    end
  end
  grid.flatten.sum
end

puts part1 data

def turn_on_2(grid, x_from, y_from, x_to, y_to)
  (x_from..x_to).each do |x|
    (y_from..y_to).each do |y|
      grid[x][y] += 1
    end
  end
end

def turn_off_2(grid, x_from, y_from, x_to, y_to)
  (x_from..x_to).each do |x|
    (y_from..y_to).each do |y|
      grid[x][y] = [grid[x][y] - 1, 0].max
    end
  end
end

def toggle_2(grid, x_from, y_from, x_to, y_to)
  (x_from..x_to).each do |x|
    (y_from..y_to).each do |y|
      grid[x][y] += 2
    end
  end
end

def part2(data)
  grid = Array.new(1000) { Array.new(1000, 0) }
  data.split("\n").each do |line|
    if line.includes?("turn on")
      x_from, y_from = line.split(" ")[2].split(",").map(&.to_i)
      x_to, y_to = line.split(" ")[4].split(",").map(&.to_i)
      turn_on_2(grid, x_from, y_from, x_to, y_to)
    elsif line.includes?("turn off")
      x_from, y_from = line.split(" ")[2].split(",").map(&.to_i)
      x_to, y_to = line.split(" ")[4].split(",").map(&.to_i)
      turn_off_2(grid, x_from, y_from, x_to, y_to)
    else
      x_from, y_from = line.split(" ")[1].split(",").map(&.to_i)
      x_to, y_to = line.split(" ")[3].split(",").map(&.to_i)
      toggle_2(grid, x_from, y_from, x_to, y_to)
    end
  end
  grid.flatten.sum
end

puts part2 data
