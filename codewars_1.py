# You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. We want to create the text that should be displayed next to such an item.
#
# Implement the function likes which takes an array containing the names of people that like an item. It must return the display text as shown in the examples:
#
# likes([]) # must be "no one likes this"
# likes(["Peter"]) # must be "Peter likes this"
# likes(["Jacob", "Alex"]) # must be "Jacob and Alex like this"
# likes(["Max", "John", "Mark"]) # must be "Max, John and Mark like this"
# likes(["Alex", "Jacob", "Mark", "Max"]) # must be "Alex, Jacob and 2 others like this"
# For 4 or more names, the number in and 2 others simply increases.

def likes(names):
    # your code here
    for x in names:
        if len(x) == 0:
            print("[],  no one likes this")
        elif len(x) >= 1:
            return print(str(names) + f", {names[0]} likes this")
        elif len(x) > 1 and len(x) >= 2:
            return print(str(names) + f", {names[0]} and {names[1]} like this")
        elif len(x) > 2 and len(x) >= 3:
            return print(str(names) + f", {names[0]}, {names[1]} and {names[2]} like this")
        elif len(x) > 3:
            return print(str(names) + f", {names[0]}, {names[1]} and {len(names) - 2} others like this")
        else:
            print("[],  no one likes this")
    return print("[],  no one likes this")


lis_0 = []
lis_1 = ['Peter']
lis_2 = ['Jacob', 'Alex']
lis_3 = ['Max', 'John', 'Mark']
lis_4 = ['Alex', 'Jacob', 'Mark', 'Max']

likes(lis_0)
likes(lis_1)
likes(lis_2)
likes(lis_3)
likes(lis_4)



# import codewars_test as test
# from solution import likes
#
#
# @test.it('Basic tests')
# def _():
#     test.assert_equals(likes([]), 'no one likes this')
#     test.assert_equals(likes(['Peter']), 'Peter likes this')
#     test.assert_equals(likes(['Jacob', 'Alex']), 'Jacob and Alex like this')
#     test.assert_equals(likes(['Max', 'John', 'Mark']), 'Max, John and Mark like this')
#     test.assert_equals(likes(['Alex', 'Jacob', 'Mark', 'Max']), 'Alex, Jacob and 2 others like this')
