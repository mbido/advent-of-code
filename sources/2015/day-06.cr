require "../utiles"

data = get_input(2015, 6)

def part1(data)
  grid = Array.new(1000) { Array(Bool).new(1000, false) }
  data.each_line do |line|
    if line =~ /(\d+),(\d+) through (\d+),(\d+)/
      x1, y1, x2, y2 = $1.to_i, $2.to_i, $3.to_i, $4.to_i
      action = case line
               when /turn on/
                 ->(x : Int32, y : Int32) { grid[x][y] = true }
               when /turn off/
                 ->(x : Int32, y : Int32) { grid[x][y] = false }
               when /toggle/
                 ->(x : Int32, y : Int32) { grid[x][y] = !grid[x][y] }
               else
                 raise "Unknown action"
               end
      (x1..x2).each do |x|
        (y1..y2).each do |y|
          action.call(x, y)
        end
      end
    end
  end
  grid.flatten.count(true)
end

puts part1 data

def part2(data)
  grid = Array.new(1000) { Array(Int32).new(1000, 0) }
  data.each_line do |line|
    if line =~ /(\d+),(\d+) through (\d+),(\d+)/
      x1, y1, x2, y2 = $1.to_i, $2.to_i, $3.to_i, $4.to_i
      action = case line
               when /turn on/
                 ->(x : Int32, y : Int32) { grid[x][y] += 1 }
               when /turn off/
                 ->(x : Int32, y : Int32) { grid[x][y] -= 1 }
               when /toggle/
                 ->(x : Int32, y : Int32) { grid[x][y] += 2 }
               else
                 raise "Unknown action"
               end
      (x1..x2).each do |x|
        (y1..y2).each do |y|
          action.call(x, y)
        end
      end
    end
  end
  grid.flatten.sum
end

puts part2 data
