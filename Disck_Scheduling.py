# def FCFS(requests,head):
#     thm=0
#     current=0

#     for request in requests:
#         thm +=abs(current-head)
#         current=request
#     return thm

# requests=[23,67,87,90]
# head=45

# result=FCFS(requests,head)
# print(f"The thm is {result}")

# def SSTF(requests):
#     seek_count=0
#     current=0
#     #First find the closest request 
#     while requests:
#         closest = min(requests,key=lambda x: abs(x-current))
#         seek_count+=abs(current-closest)
#         current = closest
#         requests.remove(closest)
#     return seek_count

# requests=[23,67,87,90]

# result=SSTF(requests)
# print(f"The SSTFis {result}")

def SCAN(requests,direction="left"):
    seek_count=0
    current=0

    if direction=="left":
        requests.sort()
    else:
        requests.sort(reverse=True)
    
    for request in requests:
        seek_count+=abs(current-request)
        current=request
    return seek_count