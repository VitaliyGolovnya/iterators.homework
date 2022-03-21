
def generator_for_nested(nested_list):
    for item in nested_list:
        if not isinstance(item, list):
            yield item
        else:
            for sub_item in generator_for_nested(item):
                yield sub_item
