# def add():
#     return n+m
# def subs():
#     return n-m
# def prod():
#     return n*m
# def div():
#     return m/n
# def rem():
#     return m%n
# def operations(op):
#     switch={
#        '+': add(),
#        '-': subs(),
#        '*': prod(),
#        '/': div(),
#        '%': rem(),
#        }
#     return switch.get(op,'Choose one of the following operator:+,-,*,/,%')
#
# operations('*')
#
# operations('^')


def switch_example(case):
    switcher = {
        1: "Case 1 selected",
        2: "Case 2 selected",
        3: "Case 3 selected"
    }
    # The get() method of the dictionary returns the value for the given key
    # if the key is not available, the second argument will be returned.
    return switcher.get(case, "Invalid case")

# Test the switch example function
for i in range(5):
    print(f"Switch case {i}: {switch_example(i)}")
