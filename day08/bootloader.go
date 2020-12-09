package main

import "fmt"

type Bootloader struct {
	Accumulator  int
	instructions []*Instruction
}

func NewBootloader() *Bootloader {
	bootloader := new(Bootloader)
	bootloader.Accumulator = 0

	return bootloader
}

func (b *Bootloader) AddInstruction(instruction *Instruction) {
	instruction.Position = len(b.instructions)
	b.instructions = append(b.instructions, instruction)
}

func (b *Bootloader) Boot() (int, error) {
	for i := 0; i < len(b.instructions); {
		var err error

		i, err = b.instructions[i].Execute(&b.Accumulator)
		if err != nil {
			return b.Accumulator, err
		}
	}

	return b.Accumulator, nil
}

func (b *Bootloader) Debug() int {
	for i := 0; i < len(b.instructions); i++ {
		current := b.instructions[i].Operation
		switch current {
		case "acc":
			continue
		case "jmp":
			b.instructions[i].Operation = "nop"
		case "nop":
			b.instructions[i].Operation = "jmp"
		}

		_, err := b.Boot()
		if err == nil {
			fmt.Printf("Changing step %d from %s to %s would fix the issue.\n",
				i+1, current, b.instructions[i].Operation)
			b.instructions[i].Operation = current
			break
		}

		b.instructions[i].Operation = current
		b.Reset()
	}

	return b.Accumulator
}

func (b *Bootloader) Reset() {
	b.Accumulator = 0
	for i := 0; i < len(b.instructions); i++ {
		b.instructions[i].Reset()
	}
}
