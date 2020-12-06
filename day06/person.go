package main

type Person struct {
	Answers string
}

func NewPerson(answers string) *Person {
	p := new(Person)
	p.Answers = answers

	return p
}

func (p Person) GetAnswers() []string {
	var answers []string

	for _, c := range p.Answers {
		answers = append(answers, string(c))
	}

	return answers
}
