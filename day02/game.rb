# frozen_string_literal: true

require_relative 'bag'
require_relative 'hand'

class Game
  REGEX_ID = /(?<=Game )\d+(?=:)/.freeze
  REGEX_HANDS = /^Game \d+: (.*)$/.freeze

  def self.from_record(record)
    game = new(record[REGEX_ID])
    record.match(REGEX_HANDS)[1].split('; ').each do |hand|
      game.add_hand(Hand.from_record(game, hand))
    end

    game
  end

  attr_reader :id

  def initialize(id)
    @id = id.to_i
    @hands = []
  end

  def add_hand(hand)
    @hands << hand
  end

  def record_hand(red: 0, green: 0, blue: 0)
    @hands << Hand.new(self, red:, green:, blue:)
  end

  def possible?(bag)
    @hands.each do |hand|
      return false unless hand.possible?(bag)
    end

    true
  end

  def smallest
    colors = { red: 0, green: 0, blue: 0 }
    @hands.each do |hand|
      colors[:red] = hand.red if hand.red > colors[:red]
      colors[:green] = hand.green if hand.green > colors[:green]
      colors[:blue] = hand.blue if hand.blue > colors[:blue]
    end

    Bag.new(**colors)
  end
end
