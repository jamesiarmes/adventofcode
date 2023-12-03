# frozen_string_literal: true

require_relative 'bag'
require_relative 'game'

INPUT_PATH = File.expand_path('input.txt', __dir__)

possible = []
powers = 0
bag = Bag.new(red: 12, green: 13, blue: 14)
File.readlines(INPUT_PATH).each do |line|
  game = Game.from_record(line)
  possible << game if game.possible?(bag)
  powers += game.smallest.power
end

print("Sum of possible game ids: #{possible.map(&:id).sum}\n")
print("Sum of smallest bag powers: #{powers}\n")
