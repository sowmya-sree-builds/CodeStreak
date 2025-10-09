# Day 49: Find Intersection of Two Lists without Built-ins
def list_intersection(a, b):
    result = []
    for i in a:
        for j in b:
            if i == j and i not in result:
                result.append(i)
    return result

print(list_intersection([1, 2, 3, 4], [3, 4, 5, 6]))
