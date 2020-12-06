package main

import (
	"bufio"
	"fmt"
	"io"
	"log"
	"os"
	"sort"
	"strings"
)

func main() {
	idMap := make(map[int]bool)
	var ids []int
	max := 0
	seats := loadSeats()
	for _, seat := range seats {
		id := seat.GetID()
		if id > max {
			max = id
		}

		idMap[id] = true
		ids = append(ids, id)
	}

	sort.Ints(ids)
	for _, id := range ids {
		_, ok := idMap[id+1]
		if !ok {
			fmt.Printf("Your seat number is %d\n", id+1)
			break
		}
	}

	fmt.Printf("Highest seat id: %d\n", max)
}

func loadSeats() []*Seat {
	file, err := os.Open("input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	var seats []*Seat

	reader := bufio.NewReader(file)
	for {
		line, _, err := reader.ReadLine()
		if err == io.EOF {
			break
		}

		seats = append(seats, NewSeat(strings.TrimSpace(string(line))))
	}

	return seats
}
