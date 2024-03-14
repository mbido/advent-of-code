require "../utiles"

data = get_input(2015, 7)

def get_amount(wires, wire, memo = {} of String => Int32)
  return memo[wire] if memo[wire]?

  if wire.to_i?
    return wire.to_i
  end

  expression = wires[wire]
  result = case expression
           when /^(.+) AND (.+)$/
             get_amount(wires, $1, memo) & get_amount(wires, $2, memo)
           when /^(.+) OR (.+)$/
             get_amount(wires, $1, memo) | get_amount(wires, $2, memo)
           when /^(.+) LSHIFT (.+)$/
             get_amount(wires, $1, memo) << $2.to_i
           when /^(.+) RSHIFT (.+)$/
             get_amount(wires, $1, memo) >> $2.to_i
           when /NOT (.+)$/
             ~get_amount(wires, $1, memo) & 0xFFFF
           when /\d+/
             expression.to_i
           else
             get_amount(wires, expression, memo)
           end

  memo[wire] = result
  result
end

def part1(data)
  wires = {} of String => String
  data.each_line do |line|
    expression, wire = line.split(" -> ")
    wires[wire] = expression
  end
  get_amount(wires, "a")
end

puts part1 data

def part2(data)
  a_value = part1 data
  wires = {} of String => String
  data.each_line do |line|
    expression, wire = line.split(" -> ")
    wires[wire] = expression
  end
  wires["b"] = a_value.to_s
  get_amount(wires, "a")
end

puts part2 data
