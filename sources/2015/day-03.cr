require "../utiles"

data = get_input(2015, 3)

def part1(data)
  x = 0
  y = 0
  houses = [[0, 0]]
  data.each_char do |c|
    case c
    when '^'
      y += 1
    when 'v'
      y -= 1
    when '>'
      x += 1
    when '<'
      x -= 1
    end
    houses << [x, y] unless houses.includes?([x, y])
  end
  houses.size
end

puts part1 data

def part2(data)
  santa_x = 0
  santa_y = 0
  robo_x = 0
  robo_y = 0
  houses = [[0, 0]]
  data.each_char.each_with_index do |c, i|
    if i.even?
      case c
      when '^'
        santa_y += 1
      when 'v'
        santa_y -= 1
      when '>'
        santa_x += 1
      when '<'
        santa_x -= 1
      end
      houses << [santa_x, santa_y] unless houses.includes?([santa_x, santa_y])
    else
      case c
      when '^'
        robo_y += 1
      when 'v'
        robo_y -= 1
      when '>'
        robo_x += 1
      when '<'
        robo_x -= 1
      end
      houses << [robo_x, robo_y] unless houses.includes?([robo_x, robo_y])
    end
  end
  houses.size
end

puts part2 data
