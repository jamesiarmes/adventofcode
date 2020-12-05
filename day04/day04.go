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
	passports := loadPassports()
	validPassports := 0
	for _, passport := range passports {
		if passport.Validate() {
			validPassports++
		}
	}

	fmt.Printf("Valid passports found: %d\n", validPassports)
}

func loadPassports() []*Passport {
	file, err := os.Open("input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	var passports []*Passport
	passport := ""

	reader := bufio.NewReader(file)
	for {
		line, _, err := reader.ReadLine()
		if err == io.EOF {
			passports = append(passports, parsePassport(passport))
			break
		}

		passportLine := strings.TrimSpace(string(line))
		if passportLine == "" {
			passports = append(passports, parsePassport(passport))
			passport = ""
		} else {
			passport += " " + passportLine
		}
	}

	return passports
}

func parsePassport(rawPassport string) *Passport {
	passport := new(Passport)
	for _, field := range strings.Fields(rawPassport) {
		f := strings.Split(field, ":")
		passport.SetField(f[0], f[1])
	}

	return passport
}
