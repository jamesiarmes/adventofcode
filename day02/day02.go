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

var pattern = regexp.MustCompile(`^(\d+)-(\d+) (.): (.*)$`)

type PasswordPolicy interface {
	ValidatePassword(password string) bool
}

type ConcretePasswordPolicy struct {
	Minimum   int
	Maximum   int
	Character string
}

func (policy ConcretePasswordPolicy) ValidatePassword(password string) bool {
	count := strings.Count(password, policy.Character)

	return count >= policy.Minimum && count <= policy.Maximum
}

type TobogganPasswordPolicy struct {
	LowerPosition int
	UpperPosition int
	Character     string
}

func (policy TobogganPasswordPolicy) ValidatePassword(password string) bool {
	return (string(password[policy.LowerPosition-1]) == policy.Character) !=
		(string(password[policy.UpperPosition-1]) == policy.Character)
}

type Password struct {
	Password string
	Policy   PasswordPolicy
}

func (password Password) IsValid() bool {
	return password.Policy.ValidatePassword(password.Password)
}

type TobogganPassword struct {
	*Password
	Policy TobogganPasswordPolicy
}

func main() {
	validPasswords := 0
	passwords := loadPasswords()
	for _, password := range passwords {
		if password.IsValid() {
			validPasswords++
		}
	}

	fmt.Printf("%d valid passwords found.\n", validPasswords)
}

func loadPasswords() []Password {
	file, err := os.Open("intput.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	var passwords []Password
	reader := bufio.NewReader(file)
	for {
		line, _, err := reader.ReadLine()
		if err == io.EOF {
			break
		}

		passwords = append(passwords,
			parseInputLine(strings.TrimSpace(string(line))))
	}

	return passwords
}

func parseInputLine(line string) Password {
	rs := pattern.FindStringSubmatch(line)

	min, _ := strconv.Atoi(rs[1])
	max, _ := strconv.Atoi(rs[2])

	return Password{rs[4], TobogganPasswordPolicy{min, max, rs[3]}}
}
