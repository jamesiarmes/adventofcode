package main

type Group struct {
	People []Person
}

func NewGroup() *Group {
	g := new(Group)

	return g
}

func (g Group) Size() int {
	return len(g.People)
}

func (g *Group) AddPerson(person Person) {
	g.People = append(g.People, person)
}

func (g Group) NumberQuestionsAnyAnswer() int {
	return len(g.QuestionsAnswered())
}

func (g Group) NumberQuestionsAllAnswered() int {
	allAnswered := 0
	size := g.Size()
	for _, count := range g.QuestionsAnswered() {
		if count == size {
			allAnswered += 1
		}
	}

	return allAnswered
}

func (g Group) QuestionsAnswered() map[string]int {
	answers := make(map[string]int)
	for _, person := range g.People {
		for _, answer := range person.GetAnswers() {
			if _, ok := answers[answer]; ok {
				answers[answer] += 1
			} else {
				answers[answer] = 1
			}
		}
	}

	return answers
}
