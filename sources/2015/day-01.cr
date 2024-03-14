require "../utiles"

data = get_input(2015, 1)

def part1(data : String) : Int32
  floor = 0
  data.each_char do |c|
    floor += 1 if c == '('
    floor -= 1 if c == ')'
  end
  floor
end

puts part1(data)

def part2(data : String) : Int32
  floor = 0
  data.each_char.with_index do |c, i|
    floor += 1 if c == '('
    floor -= 1 if c == ')'
    return i + 1 if floor == -1
  end
  -1
end

puts part2(data)
