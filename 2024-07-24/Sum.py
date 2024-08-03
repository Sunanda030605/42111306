def replica_sum(iterable, start=0):
    total = start
    for element in iterable:
        total += element
    return total

numbers = [1, 2, 3, 4, 5]
result = replica_sum(numbers)
print(result)  


result_with_start = replica_sum(numbers, 10)
print(result_with_start)  
