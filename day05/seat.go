package main

type Seat struct {
	Partition string
}

func NewSeat(partition string) *Seat {
	seat := new(Seat)
	seat.Partition = partition

	return seat
}

func (s Seat) String() string {
	return s.Partition
}

func (s Seat) GetRow() int {
	row := s.Partition[0:7]
	min := 0
	max := 127
	for _, c := range row {
		if c == 'F' {
			max = min + ((max - min) / 2)
		} else {
			min = max - ((max - min) / 2)
		}
	}

	return max
}

func (s Seat) GetColumn() int {
	col := s.Partition[7:10]
	min := 0
	max := 7
	for _, c := range col {
		if c == 'L' {
			max = min + ((max - min) / 2)
		} else {
			min = max - ((max - min) / 2)
		}
	}

	return max
}

func (s Seat) GetID() int {
	return s.GetRow()*8 + s.GetColumn()
}
