#!/usr/bin/python3
class VerboseList(list):
    def append(self, value):
        super().append(value)
        print(f"Added [{value}] to the list.")

    def extend(self, iterable):
        item_count = len(iterable)
        super().extend(iterable)
        print(f"Extended the list with [{item_count}] items.")

    def remove(self, value):
        print(f"Removed [{value}] from the list.")
        super().remove(value)

    def pop(self, index=-1):
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
