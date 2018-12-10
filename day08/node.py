class Node:
    def __init__(self, child_count, metadata_count):
        self.child_count = child_count
        self.metadata_count = metadata_count
        self.children = []
        self.metadata = []

    def sum_metadata(self):
        total = sum(self.metadata)
        for child in self.children:
            total += child.sum_metadata()

        return total

    def process(self, structure):
        for _ in range(self.child_count):
            child = Node(structure.pop(0), structure.pop(0))
            child.process(structure)
            self.children.append(child)

        for _ in range(self.metadata_count):
            self.metadata.append(structure.pop(0))

        return structure

    def value(self):
        if self.child_count == 0:
            return sum(self.metadata)

        value = 0
        for index in self.metadata:
            if index > 0 and index <= self.child_count:
                value += self.children[index - 1].value()

        return value
