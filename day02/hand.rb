# frozen_string_literal: true

class Hand
  REGEX_STONES = /(?<count>\d+) (?<color>\w+)/.freeze

  def self.from_record(game, record)
    stones = {}
    record.split(', ').each do |group|
      matches = group.match(REGEX_STONES)
      stones[matches[:color].to_sym] = matches[:count].to_i
    end

    new(game, **stones)
  end

  attr_reader :red, :green, :blue

  def initialize(game, red: 0, green: 0, blue: 0)
    @game = game
    @red = red
    @green = green
    @blue = blue
  end

  def size
    red + green + blue
  end

  def possible?(bag)
    size <= bag.size && red <= bag.red && green <= bag.green && blue <= bag.blue
  end
end
