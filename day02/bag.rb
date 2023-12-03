# frozen_string_literal: true

class Bag
  attr_reader :red, :green, :blue

  def initialize(red: 0, green: 0, blue: 0)
    @red = red
    @green = green
    @blue = blue
  end

  def size
    red + green + blue
  end

  def power
    red * green * blue
  end
end
