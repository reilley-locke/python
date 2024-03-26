
stop = int(input())

for a in range(3):
    result = 0
    
    for b in range(4):
        result += a + b
    
    print(result)
    
    if result > stop:
        break