def custom_range(start, stop=None, step=1):
    if stop is None:
        start, stop = 0, start
    return [i for i in range(start, stop, step)]


print(custom_range(5))         
print(custom_range(1, 5))     
print(custom_range(1, 10, 2))  
print(custom_range(10, 1, -2)) 
