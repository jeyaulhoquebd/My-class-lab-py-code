# def summation():
#     n = 1
#     sum = 0;
# for n in range(100):
#     if n%2 == 0:
#         continue
#     sum += n
#     return n
    
# add = summation()
# print("The summation is = ", add)

def summation():
    total = 0
    for n in range(100):
        if n % 2 == 0:
            continue
        total = total + n
    return total

add = summation()
print("The summation is = ", add)