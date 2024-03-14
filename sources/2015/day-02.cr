require "../utiles"

data = get_input 2015, 2

def paper_needed(l_w_h)
  l, w, h = l_w_h
  faces = [l*w, w*h, h*l]
  2 * faces.sum + faces.min
end

def part1(data)
  data.split("\n").map { |l| paper_needed(l.split("x").map(&.to_i)) }.sum
end

puts part1 data

def ribbon_needed(l_w_h)
  l, w, h = l_w_h
  l, w, h = [l, w, h].sort
  2 * (l + w) + l * w * h
end

def part2(data)
  data.split("\n").map { |l| ribbon_needed(l.split("x").map(&.to_i)) }.sum
end

puts part2 data
