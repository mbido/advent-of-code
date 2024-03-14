require "../utiles"

data = get_input(2015, 5)

def contains_three_vowels?(str)
  str.scan(/[aeiou]/).size >= 3
end

def contains_double_letter?(str)
  str.scan(/(.)\1/).size >= 1
end

def contains_naughty_strings?(str)
  str.scan(/ab|cd|pq|xy/).size >= 1
end

def part1(data)
  data.split("\n").count do |str|
    contains_three_vowels?(str) && contains_double_letter?(str) && !contains_naughty_strings?(str)
  end
end

puts part1 data

def contains_double_separated?(str)
  str.scan(/(.).\1/).size >= 1
end

def contains_two_double?(str)
  str.scan(/(..).*\1/).size >= 1
end

def part2(data)
  data.split("\n").count do |str|
    contains_double_separated?(str) && contains_two_double?(str)
  end
end

puts part2 data
