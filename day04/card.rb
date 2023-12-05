# frozen_string_literal: true

class Card
  REGEX_ID = /(?<=Card )\s*\d+(?=:)/.freeze
  REGEX_WINNERS = /\d+(?![\d:])(?=.*\|)/.freeze
  REGEX_CONTENTS = /\d+(?=[^:|]*$)/.freeze

  def self.from_record(record)
    new(
      record[REGEX_ID].to_i,
      record.scan(REGEX_WINNERS).map(&:to_i),
      record.scan(REGEX_CONTENTS).map(&:to_i),
    )
  end

  attr_reader :id

  def initialize(id, winners, contents)
    @id = id
    @winners = winners
    @contents = contents
  end

  def points
    return 0 unless matches > 0

    1 * (2 ** (matches - 1))
  end

  def matches
    @matches ||= @winners.uniq.select { |winner| @contents.include?(winner) }.size
  end

  def prize_cards(collection)
    return 0 unless matches > 0
    return @prize_cards if @prize_cards

    cards = collection[@id..(@id + matches - 1)]
    @prize_cards = cards.size + cards.sum { |c| c.prize_cards(collection) }
  end
end
