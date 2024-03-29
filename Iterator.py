
class IteratorForNested:
    def __init__(self, some_list):
        self.main_list = some_list

    def __iter__(self):
        self.main_list_cursor = 0
        self.nested_list_cursor = -1
        return self

    def __next__(self):
        self.nested_list_cursor += 1
        if self.nested_list_cursor > len(self.main_list[self.main_list_cursor]) - 1:
            self.main_list_cursor += 1
            self.nested_list_cursor = 0
        if self.main_list_cursor > len(self.main_list) - 1:
            raise StopIteration
        return self.main_list[self.main_list_cursor][self.nested_list_cursor]


