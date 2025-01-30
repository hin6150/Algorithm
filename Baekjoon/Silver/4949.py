while(1):
    temp = []
    arr = list(map(str, input()))
    
    if(arr==['.']):
        break
    
    if(arr[len(arr)-1] != '.'):
        temp.append(0)
        pass

    for idx in range(len(arr)):
        if(arr[idx]) == '(':
            temp.append(arr[idx])
        
        elif(arr[idx]) ==')':
            try:
                if(temp.pop() !='('):
                    temp.append(0)
                    break   
            except:
                temp.append(0)
                break   
            
        if(arr[idx]) == '[':
            temp.append(arr[idx])
        
        elif(arr[idx]) ==']':
            try:
                if(temp.pop() !='['):
                    temp.append(0)
                    break
            except:
                temp.append(0)
                break   
            
    if(len(temp) > 0):
        print("no")
    else:
        print("yes")