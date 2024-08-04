
d = {'mango': 10, 'banana': 0, 'apple': 15, 'orange': 0, 'pineapple': 20}

# Remove out of stock fruits (where value is 0)
d = {k: v for k, v in d.items() if v != 0}
print(d) 

# Update mango quantity to 15
d['mango'] = 15

# Decrease pineapple quantity by 5
d['pineapple'] -= 5

print(d)  
