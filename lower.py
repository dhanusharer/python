def lower_bound_optimal(arr,x):
    low=0
    high=len(arr)-1
    ans=len(arr)
     
    while low<=high:
        mid=(low+high)//2
        if arr[mid]>=x:
          ans=mid
          high=mid-1
        else:
           low=mid+1
    return ans
a=[1,2,2,2,4,5]
x=2
lower_bound_optimal(a,x)
result=lower_bound_optimal(a,x)
print(result)