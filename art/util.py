from collections import deque

"""
Returns `True` if all elements on `iterable` are `None`, and `False`
otherwise.
"""
def all_none(iterable):
    for item in iterable:
        if item is not None:
            return False
    return True

"""
Returns `value` it it is a list, or a list containing it otherwise.
"""
def listify(value):
    if isinstance(value, list):
        return value
    else:
        return [value]

"""
Build a queue of unique elements.
"""
class SetQueue(set):
    def __init__(self, *args, **kwargs):
        super(SetQueue, self).__init__(self, *args, **kwargs)
        self._queue = deque()

    def __iter__(self):
        for item in self._queue:
            yield item

    def update(*args, **kwargs):
        return NotImplemented

    def copy(self):
        return NotImplemented

    def add(self, item):
        if item not in self:
            super(SetQueue, self).add(item)
            self._queue.append(item)

    def pop(self):
        item = self._queue.popleft()
        super(SetQueue, self).remove(item)
        return item

    def remove(self, item):
        super(SetQueue, self).remove(item)
        self._queue.remove(item)

    def clear(self):
        super(SetQueue, self).clear()
        self._queue.clear()
