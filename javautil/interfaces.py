class Const_Type:
    def set_index(self, index: int):
        self.index = index

    def __lt__(self, other):
        if self.const_type == other.const_type:
            return self.index < other.index
        return self.const_type < other.const_type


class Linkable:
    def __init__(self):
        self.const_pool = None

    def link(self, const_pool):
        self.const_pool = const_pool