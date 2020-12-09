package main

import (
	"bufio"
	"fmt"
	"io"
	"log"
	"os"
	"regexp"
	"strconv"
	"strings"
)

func main() {
	bootloader := NewBootloader()
	loadInstructions(bootloader)
	accumulator, _ := bootloader.Boot()

	fmt.Printf("Last accumulator: %d\n", accumulator)

	bootloader.Debug()
	fmt.Printf("Last accumulator after debugging: %d\n", bootloader.Accumulator)
}

func loadInstructions(bootloader *Bootloader) {
	file, err := os.Open("input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	reader := bufio.NewReader(file)
	for {
		line, _, err := reader.ReadLine()
		if err == io.EOF {
			break
		}

		instruction := parseInstruction(strings.TrimSpace(string(line)))
		bootloader.AddInstruction(instruction)
	}
}

func parseInstruction(input string) *Instruction {
	pattern := regexp.MustCompile(`^(nop|acc|jmp) ([+-]\d+)$`)
	result := pattern.FindStringSubmatch(input)

	argument, _ := strconv.Atoi(result[2])

	return NewInstruction(result[1], argument)
}
