def new_ljust(s, width, fillchar=' '):
    if len(s) >= width:
        return s
    return s + fillchar * (width - len(s))

text = "hello"
result = new_ljust(text, 10, '-')
print(result)  
