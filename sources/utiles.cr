def get_input(year : Int32, day_number : Int32) : String
  add = day_number < 10 ? "0" : ""
  File.read("../../data/#{year}/day-#{add}#{day_number}.txt")
end
