def new_rjust(s, width, fillchar=' '):
    if len(s) >= width:
        return s
    return fillchar * (width - len(s)) + s

text = "hello"
result = new_rjust(text, 10, '-')
print(result)  
