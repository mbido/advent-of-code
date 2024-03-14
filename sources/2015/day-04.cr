require "../utiles"

data = get_input(2015, 4)

def helper(data, prefix)
  i = 0
  while true
    if md5("#{data}#{i}").starts_with?(prefix)
      return i
    end
    i += 1
  end
  -1
end

def part1(data)
  helper(data, "00000")
end

puts part1 data

def part2(data)
  helper(data, "000000")
end

puts part2 data
