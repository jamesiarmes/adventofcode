package main

import (
	"errors"
	"fmt"
)

type Instruction struct {
	Position  int
	Operation string
	argument  int
	executed  bool
}

func NewInstruction(operation string, argument int) *Instruction {
	instruction := new(Instruction)
	instruction.Operation = operation
	instruction.argument = argument
	instruction.executed = false

	return instruction
}

func (i Instruction) String() string {
	return fmt.Sprintf("(%d: %s %d)", i.Position, i.Operation, i.argument)
}

func (i *Instruction) Execute(accumulator *int) (int, error) {
	if i.executed {
		return 0, errors.New(fmt.Sprintf("Instruction %s has already been executed", i))
	}

	i.executed = true
	nextPosition := i.Position

	switch i.Operation {
	case "nop":
		nextPosition++
	case "acc":
		nextPosition++
		*accumulator += i.argument
	case "jmp":
		nextPosition += i.argument
	}

	return nextPosition, nil
}

func (i *Instruction) Reset() {
	i.executed = false
}
