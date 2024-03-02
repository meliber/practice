# if a collection has no __contains__ method, in test does a sequential scan.
class Everything:
    """An object contains everything.
    """
    def __init__(self):
        pass

    def __contains__(self, other):
        return True

universe = Everything()
for i in "the_whole_world":
    assert i in universe
