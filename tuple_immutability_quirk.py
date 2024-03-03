t = (1, 2, [3, 4])
try:
    t[-1] += [5, ]
except TypeError as e:
    print(f"TypeError: {e}")
finally:
    assert t == (1, 2, [3, 4, 5])
    print(t)
    print("Although a TypeError is raised, t is updated.")
