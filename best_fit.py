def best_fit(memory_blocks,process_size):
    allocation=[-1]*len(process_size)

    for i in range(len(process_size)):
        best_index=-1
        #Resetting the worst Index at every iteration of process_size
        for j in range(len(memory_blocks)):
            if(memory_blocks[j]>process_size[i]):
                # j is current one 
                if(best_index==-1 or memory_blocks[j]<memory_blocks[best_index]):
                    best_index=j
        
        if(best_index!=-1):# Once all the memory_blocks are chcked assign a permenent value 
            allocation[i]=best_index
            memory_blocks[best_index]-=process_size[i]  
    return allocation
    
memory_blocks = [100, 200, 300, 400, 500]
process_size = [212, 417, 112, 426]
allocation=best_fit(memory_blocks,process_size)
print("best Fit Allocation:", allocation)