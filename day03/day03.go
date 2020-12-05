package main

import (
	"bufio"
	"container/ring"
	"fmt"
	"io"
	"log"
	"os"
	"strings"
)

type Sloap struct {
	Right int
	Down  int
}

func NewSloap(right int, down int) *Sloap {
	sloap := new(Sloap)
	sloap.Right = right
	sloap.Down = down

	return sloap
}

func (s Sloap) String() string {
	return fmt.Sprintf("Right %d, Down %d", s.Right, s.Down)
}

func main() {
	tobogganMap := loadMap()
	sloaps := []*Sloap{
		NewSloap(1, 1),
		NewSloap(3, 1),
		NewSloap(5, 1),
		NewSloap(7, 1),
		NewSloap(1, 2),
	}

	treesProduct := 1
	for _, sloap := range sloaps {
		trees := checkSloap(sloap, tobogganMap)
		treesProduct *= trees
		fmt.Printf("%s: %d\n", sloap, trees)
	}

	fmt.Printf("Product of trees: %d\n", treesProduct)
}

func checkSloap(sloap *Sloap, tobogganMap []*ring.Ring) int {
	columnPos := 0
	trees := 0
	for rowPos := sloap.Down; rowPos < len(tobogganMap); rowPos += sloap.Down {
		columnPos += sloap.Right
		char := tobogganMap[rowPos].Move(columnPos)
		if char.Value == "#" {
			trees++
		}
	}

	return trees
}

func loadMap() []*ring.Ring {
	file, err := os.Open("intput.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	var tobogganMap []*ring.Ring
	reader := bufio.NewReader(file)
	for {
		line, _, err := reader.ReadLine()
		if err == io.EOF {
			break
		}

		tobogganMap = append(tobogganMap,
			parseInputLine(strings.TrimSpace(string(line))))
	}

	return tobogganMap
}

func parseInputLine(line string) *ring.Ring {
	row := ring.New(len(line))

	for _, char := range line {
		row.Value = string(char)
		row = row.Next()
	}

	return row
}
