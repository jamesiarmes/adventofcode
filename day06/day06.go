package main

import (
	"bufio"
	"fmt"
	"io"
	"log"
	"os"
	"strings"
)

func main() {
	sumAnyAnswered := 0
	sumAllAnswered := 0
	groups := loadGroups()
	for _, group := range groups {
		sumAnyAnswered += group.NumberQuestionsAnyAnswer()
		sumAllAnswered += group.NumberQuestionsAllAnswered()
	}

	fmt.Printf("Sum of any answered: %d\n", sumAnyAnswered)
	fmt.Printf("Sum of all answered: %d\n", sumAllAnswered)
}

func loadGroups() []*Group {
	file, err := os.Open("input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	var groups []*Group
	group := NewGroup()

	reader := bufio.NewReader(file)
	for {
		line, _, err := reader.ReadLine()
		if err == io.EOF {
			groups = append(groups, group)
			break
		}

		groupLine := strings.TrimSpace(string(line))
		if groupLine == "" {
			groups = append(groups, group)
			group = NewGroup()
		} else {

			group.AddPerson(*NewPerson(groupLine))
		}
	}

	return groups
}
