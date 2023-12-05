# frozen_string_literal: true

class Schematic
  def initialize
    @rows = []
  end

  def <<(row)
    if @rows.any?
      @rows.last.after = row
      row.before = @rows.last
    end

    @rows << row
  end

  def sum
    sum = 0
    @rows.each { |row| sum += row.sum }
    sum
  end

  def gear_ratio
    sum = 0
    @rows.each { |row| sum += row.gear_ratio }
    sum
  end
end
