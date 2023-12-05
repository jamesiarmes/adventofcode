# frozen_string_literal: true

require_relative 'row'
require_relative 'schematic'
require_relative 'slot'

INPUT_PATH = File.expand_path('input.txt', __dir__)

schematic = Schematic.new
File.readlines(INPUT_PATH).each_with_index do |line, i|
  schematic << Row.new(i).tap do |row|
    line.chomp.each_char.each_with_index { |c, j| row << Slot.new(c, j, row) }
  end
end

puts("Schematic sum: #{schematic.sum}")
puts("Gear ratio sum: #{schematic.gear_ratio}")
