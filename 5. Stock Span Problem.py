def stockspan(price):
    #Creating empty stack and span list
    stack = []
    span = []
    #Assign the first span as 1 and the push the index of the first element 
    #into the stack
    span.append(1)
    stack.append(0)
        
    for i in range(1,len(price)):
        #Loop through the price list and keep on popping element from the stack
        #if the ith price is greater than the price of the index in stack
        while((len(stack) > 0) and (price[i] >= price[stack[-1]])):
            stack.pop()
        
        #If the stack becomes empty after popping then the span is the ith element
        #itself else the span is the difference of the ith position and the element
        #at the top index of the stack
        
        if(len(stack) <= 0):
            span.append(i+1)
        else:
            span.append(i - stack[-1])

        #Append the current price to the stack
        stack.append(i)
        
    return span

###############
##Driver Code##
###############

price = [10, 4, 5, 90, 120, 80] 
stockspan(price)
    
