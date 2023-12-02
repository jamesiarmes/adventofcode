# frozen_string_literal: true

INPUT_PATH = "#{__dir__}/input.txt"
DIGITS = {
  one: 1,
  two: 2,
  three: 3,
  four: 4,
  five: 5,
  six: 6,
  seven: 7,
  eight: 8,
  nine: 9
}.freeze
DIGIT_REGEX = /(?=(\d|#{DIGITS.keys.join('|')}))/.freeze

def parse_digits(value)
  matches = value.scan(DIGIT_REGEX).flatten
  (word_to_digit(matches.first) * 10) + word_to_digit(matches.last)
end

def numeric?(value)
  Float(value) != nil rescue false
end

def word_to_digit(value)
  numeric?(value) ? value.to_i : DIGITS[value.to_sym]
end

values = []
File.readlines(INPUT_PATH).each do |line|
  values << parse_digits(line.strip.downcase)
end

print "Final calibration value: #{values.sum}"
