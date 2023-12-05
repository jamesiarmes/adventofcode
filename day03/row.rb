# frozen_string_literal: true

class Row
  attr_reader :position
  attr_accessor :before, :after

  def initialize(position, before: nil, after: nil)
    @position = position.to_i
    @slots = []
  end

  def <<(slot)
    if @slots.any?
      @slots.last.after = slot
      slot.before = @slots.last
    end

    @slots << slot
  end

  def [](index)
    @slots[index]
  end

  def sum
    @slots.sum(&:value)
  end

  def gear_ratio
    @slots.sum(&:gear_ratio)
  end
end
