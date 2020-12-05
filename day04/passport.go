package main

import (
	"fmt"
	"reflect"
	"regexp"
	"strconv"
	"strings"
)

type Passport struct {
	Byr string
	Cid string
	Iyr string
	Eyr string
	Hgt string
	Hcl string
	Ecl string
	Pid string
}

func (p Passport) String() string {
	//result, _ := json.Marshal(p)
	//
	//return string(result)

	return fmt.Sprintf("ecl: %s", p.Ecl)
}

func (p *Passport) SetField(field string, value string) {
	reflect.ValueOf(p).Elem().FieldByName(strings.Title(field)).
		SetString(value)
}

func (p Passport) Validate() bool {
	return p.validateBirth() && p.validateIssue() && p.validateExpire() &&
		p.validateHeight() && p.validateHair() && p.validateEye() &&
		p.validateId()
}

func (p Passport) validateBirth() bool {
	if p.Byr == "" {
		return false
	}

	return p.validateYear(p.Byr, 1920, 2002)
}

func (p Passport) validateIssue() bool {
	if p.Iyr == "" {
		return false
	}

	return p.validateYear(p.Iyr, 2010, 2020)
}

func (p Passport) validateExpire() bool {
	if p.Eyr == "" {
		return false
	}

	return p.validateYear(p.Eyr, 2020, 2030)
}

func (p Passport) validateYear(year string, minimum int, maximum int) bool {
	value, _ := strconv.Atoi(year)

	return len(year) == 4 && value >= minimum && value <= maximum
}

func (p Passport) validateHeight() bool {
	if p.Hgt == "" {
		return false
	}

	pattern := regexp.MustCompile(`^(\d+)(cm|in)$`)
	rs := pattern.FindStringSubmatch(p.Hgt)

	if len(rs) < 3 {
		return false
	}

	value, _ := strconv.Atoi(rs[1])
	var min, max int

	switch rs[2] {
	case "cm":
		min = 150
		max = 193
	case "in":
		min = 59
		max = 76
	}

	return value >= min && value <= max
}

func (p Passport) validateHair() bool {
	if p.Hcl == "" {
		return false
	}

	result, _ := regexp.MatchString("^#[0-9a-f]{6}$", p.Hcl)

	return result
}

func (p Passport) validateEye() bool {
	if p.Ecl == "" {
		return false
	}

	validValues := []string{"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}

	for _, value := range validValues {
		if value == p.Ecl {
			return true
		}
	}

	return false
}

func (p Passport) validateId() bool {
	if p.Pid == "" {
		return false
	}

	result, _ := regexp.MatchString("^[0-9]{9}$", p.Pid)

	return result
}
