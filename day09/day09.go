package main

import (
	"bufio"
	"errors"
	"fmt"
	"io"
	"log"
	"os"
	"strconv"
	"strings"
)

func main() {
	preamble := 25

	numbers := loadInput()
	invalid, weakness := findInvalid(numbers, preamble)
	fmt.Printf("Invalid number is %d due to weakness %d.\n", invalid, weakness)
}

func loadInput() []int {
	file, err := os.Open("input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	var numbers []int
	reader := bufio.NewReader(file)
	for {
		line, _, err := reader.ReadLine()
		if err == io.EOF {
			break
		}

		number, _ := strconv.Atoi(strings.TrimSpace(string(line)))
		numbers = append(numbers, number)
	}

	return numbers
}

func findInvalid(numbers []int, preamble int) (int, int) {
	for i := preamble; i < len(numbers); i++ {
		if !addendsExist(numbers, numbers[i], i-preamble, i-1) {
			weakness, err := findWeakness(numbers, numbers[i], i, 2)
			if err != nil {
				fmt.Println(err)
			}

			return numbers[i], weakness
		}
	}

	return 0, 0
}

func addendsExist(numbers []int, number int, start int, stop int) bool {
	for i := start; i < stop; i++ {
		for j := i + 1; j <= stop; j++ {
			if numbers[i]+numbers[j] == number {
				return true
			}
		}
	}

	return false
}

func findWeakness(numbers []int, invalid int, position int, size int) (int, error) {
	if size >= position {
		return 0, errors.New("Unable to find weakness.")
	}

	for i := 0; i < position-size; i++ {
		sum := numbers[i]
		min := numbers[i]
		max := numbers[i]
		for j := i + 1; j < i+size; j++ {
			sum += numbers[j]
			if numbers[j] < min {
				min = numbers[j]
			}
			if numbers[j] > max {
				max = numbers[j]
			}
		}

		if sum == invalid {
			return min + max, nil
		}
	}

	return findWeakness(numbers, invalid, position, size+1)
}
