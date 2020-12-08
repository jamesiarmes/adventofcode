package main

var bags map[string]*Bag

func init() {
	bags = make(map[string]*Bag)
}

type Bag struct {
	Color    string
	Parents  []*Bag
	Children map[*Bag]int
}

func NewBag(color string) *Bag {
	var bag *Bag

	bag, ok := bags[color]
	if !ok {
		bag = new(Bag)
		bag.Color = color
		bag.Children = make(map[*Bag]int)
		bags[color] = bag
	}

	return bag
}

func (b Bag) String() string {
	return b.Color
}

func (b *Bag) AddParent(parent *Bag) {
	b.Parents = append(b.Parents, parent)
}

func (b *Bag) AddChild(child *Bag, quantity int) {
	b.Children[child] = quantity
}

func (b Bag) AllPossibleParents() map[string]Bag {
	parents := make(map[string]Bag)
	for _, parent := range b.Parents {
		parents[parent.Color] = *parent
		parentParents := parent.AllPossibleParents()
		for k, v := range parentParents {
			parents[k] = v
		}
	}

	return parents
}

func (b Bag) TotalRequiredChildren() int {
	total := 0

	for child, quantity := range b.Children {
		total += quantity
		total += quantity * child.TotalRequiredChildren()
	}

	return total
}
