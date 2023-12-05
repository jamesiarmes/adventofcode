# frozen_string_literal: true

class Slot
  attr_reader :position, :content
  attr_accessor :before, :after

  def initialize(content, position, row, before: nil, after: nil)
    @content = content
    @position = position.to_i
    @row = row
    @before  = before
    @after = after
  end

  def gear?
    return false unless @content == '*'

    # TODO: Check for adjacent numbers.
    @content == '*'
  end

  def gear_ratio
    return 0 unless gear?

    numbers = adjacent_numbers
    numbers.size == 2 ? numbers.inject(:*) : 0
  end

  def value
    (number? && symbol_adjacent?) ? number : 0
  end

  def number?
    %r'\d'.match?(@content)
  end

  def number
    raise RuntimeError, 'Not a number' unless number?

    @content.to_i * multiplier
  end

  def number_full
    raise RuntimeError, 'Not a number' unless number?

    full = number
    traverse(:before) do |slot|
      break unless slot.number?
      slot.number
    end
    traverse(:after) do |slot|
      break unless slot.number?
      full += slot.number
    end

    full
  end

  def symbol?
    %r'[^\d.]'.match?(@content)
  end

  def symbol_adjacent?
    return true if @before&.symbol? || @after&.symbol?
    return true if symbol_sibling?(:before) || symbol_sibling?(:after)

    symbol_neighbors?
  end

  def symbol_neighbors?
    (@row.before && symbol_neighbor?(@row.before)) ||
      (@row.after && symbol_neighbor?(@row.after))
  end

  private

  def number_neighbors(row)
    # If the slot in the same position as the current one is a number, there can
    # only be one neighbor in this row.
    if row[@position]&.number?
      return [row[@position].number_full]
    end

    numbers = []
    numbers << row[@position - 1].number_full if row[@position - 1]&.number?
    numbers << row[@position + 1].number_full if row[@position + 1]&.number?
    numbers
  end

  def adjacent_numbers
    numbers = []
    numbers << number_sibling(:before) if @before&.number?
    numbers << number_sibling(:after) if @after&.number?
    numbers += number_neighbors(@row.before) if @row.before
    numbers += number_neighbors(@row.after) if @row.after
    numbers
  end

  def number_sibling(direction)
    raise RuntimeError, 'Neighbor is not a number' unless send(direction)&.number?

    number = 0
    traverse(direction) do |slot|
      break unless slot.number?
      number += slot.number
    end

    number
  end

  def symbol_sibling?(direction)
    adjacent = false
    traverse(direction) do |slot|
      adjacent = slot.symbol? || (slot.number? && slot.symbol_neighbors?)
      break unless slot.number? && !adjacent
    end

    adjacent
  end

  def symbol_neighbor?(row)
    row[@position - 1]&.symbol? || row[@position]&.symbol? ||
      row[@position + 1]&.symbol?
  end

  def traverse(direction)
    current = self
    loop do
      break if current.send(direction).nil?

      current = current.send(direction)
      yield current
    end
  end

  def multiplier
    # If this number is part of a sequence, apply a multiplier.
    return 1 unless after&.number?

    multipliers = 0
    current = self
    loop do
      break unless current.after&.number?

      multipliers += 1
      current = current.after
    end

    10 ** multipliers
  end
end
