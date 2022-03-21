
class IteratorForNested:
    def __init__(self, nested_list):
        self.nested_list = nested_list
        self.start = -1
        self.end = len(nested_list)

    def __iter__(self):
        return self

    def __next__(self):
        self.start += 1
        if self.start == self.end:
            raise StopIteration
        return self.iteration(self.nested_list[self.start])

    def iteration(self, data):
        if isinstance(data, list):
            temp_list = []
            for element in data:
                temp_list.append(str(self.iteration(element)))
            return '\n'.join(temp_list)
        else:
            return data
