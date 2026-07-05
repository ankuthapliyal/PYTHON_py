# language = {"C", "C++", "JAVA", "PYTHON", "C++"} # set not use duplecate value
# print(type(language))
# print(language)
# language.add("HTML")
# language.remove("C")
# print(language)

# set1 = {1, 2, 3, 4, 7, 5, 4}
# set2 = {3, 5, 6, 7, 8, 9, 10}

# print(set1.union(set2))
# print(set1.intersection(set2))

# Convert list into set

# programminglist = ["C", "C++", "JAVA", "PYTHON", "C++", "PYTHON", "JAVA"]
# print(programminglist)

# programmingset = set(programminglist)
# print(programmingset)
# print("These Many Language: ",len(programmingset))

# s1 = {(1,2,3),"Hello"}
# print(s1)

set1 = {1, 2, 3, 4, 7, 5, 4}
set2 = {3, 5, 6, 7, 8, 9, 10}
print(min(set1))
print(max(set1))
print(sum(set1))
print(sorted(set1))
print(set1.difference(set2))
print(set1.symmetric_difference(set2))
print(set1.isdisjoint(set2))
print(set1.issubset(set2))
print(set1.issuperset(set2))