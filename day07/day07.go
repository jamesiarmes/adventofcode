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
	bagColor := "shiny gold"
	loadRules()

	bag := NewBag(bagColor)
	possibleParents := bag.AllPossibleParents()
	totalChildren := bag.TotalRequiredChildren()

	fmt.Printf("%s bag has %d possible parents.\n", bagColor,
		len(possibleParents))
	fmt.Printf("%s has %d total required children.\n", bagColor, totalChildren)
}

func loadRules() map[string]*Bag {
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

		rule := strings.TrimSpace(string(line))
		parseRule(rule)
	}

	return bags
}

func parseRule(rule string) {
	parentBagPattern := regexp.MustCompile(`^(.+?) bags contain`)
	parentResult := parentBagPattern.FindStringSubmatch(rule)

	parent := NewBag(parentResult[1])

	childBagsPattern := regexp.MustCompile(`(\d+) (.*?) bags?`)
	childResults := childBagsPattern.FindAllStringSubmatch(rule, -1)

	for _, result := range childResults {
		child := NewBag(result[2])
		child.AddParent(parent)

		quantity, _ := strconv.Atoi(result[1])
		parent.AddChild(child, quantity)
	}
}
