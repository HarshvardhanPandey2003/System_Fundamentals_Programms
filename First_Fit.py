def best_fit(memory_blocks,process_size):
    allocation=[-1]*len(process_size)
    # Allocation represtents which process have been allocated or not
    # That is why its length is len(process_size)

    for i in range(len(process_size)):
        for j in range(len(memory_blocks)):
            if(memory_blocks[j]>process_size[i]):
                allocation[i]=j
                memory_blocks[j]-=process_size[i]
                break
    return allocation
    
memory_blocks = [600, 200, 300, 400, 500]
process_size = [212, 417, 112, 426]
allocation=best_fit(memory_blocks,process_size)
print("best Fit Allocation:", allocation)