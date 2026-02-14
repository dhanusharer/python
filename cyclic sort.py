def cycle_sort(arr):
    for cycleStart in range(0,len(arr)-1):
        item=arr[cycleStart]
        pos=cycleStart 
        for i in range(cycleStart+1,len(arr)):
            if arr[i]<=item:
               pos+=1
        if pos==cycleStart:
            continue
        while item == arr[pos]:
           pos+=1
        arr[pos],item=item,arr[pos]
        while pos !=cycleStart:
            pos=cycleStart
            for i in range(cycleStart+1,len(arr)):
                if arr[i]<item:
                    pos+=1
            while item == arr[pos]:
                pos+=1
            arr[pos],item=item,arr[pos]
        return arr
arr=[7,4,9,5,2,1]
result= cycle_sort(arr)
print(result)         