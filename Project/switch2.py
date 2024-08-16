# def case_1():
#     return "Case 1 selected"
#
# def case_2():
#     return "Case 2 selected"
#
# def case_3():
#     return "Case 3 selected"
#
# def default_case():
#     return "Invalid case"
#
# def switch_example(case):
#     switcher = {
#         1: case_1,
#         2: case_2,
#         3: case_3
#     }
#     # The get() method of the dictionary returns the function for the given key
#     # if the key is not available, the default_case function will be returned.
#     func = switcher.get(case, default_case)
#     return func()
#
# # Test the switch example function
# for i in range(5):
#     print(f"Switch case {i}: {switch_example(i)}")


def operations(letter):
    switch={
       'a': "It is a vowel",
       'e': "It is a vowel",
       'i': "It is a vowel",
       'o': "It is a vowel",
       'u': "It is a vowel",
       }
    return switch.get(letter,"It is a not a vowel")

operations('a')
