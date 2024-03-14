def get_input(year : Int32, day_number : Int32) : String
  add = day_number < 10 ? "0" : ""
  File.read("../../data/#{year}/day-#{add}#{day_number}.txt")
end

require "digest"

def md5(input : String) : String
  Digest::MD5.hexdigest(input)
end
