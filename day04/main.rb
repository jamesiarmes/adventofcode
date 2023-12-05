# frozen_string_literal: true

require_relative 'card'

INPUT_PATH = File.expand_path('input.txt', __dir__)

cards = []
File.readlines(INPUT_PATH).each do |line|
  cards << Card.from_record(line)
end

puts "Total points: #{cards.sum(&:points)}"
puts "Total cards: #{cards.size + cards.sum { |c| c.prize_cards(cards)}}"
