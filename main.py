from Iterator import IteratorForNested
from Generator import generator_for_nested

nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    [1, 2, None],
]

my_iterator = IteratorForNested(nested_list)
for i in my_iterator:
    print(i)

for item in generator_for_nested(nested_list):
    print(item)
