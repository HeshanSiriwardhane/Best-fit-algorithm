# Function to allocate processes to memory blocks using Best Fit Algorithm
def best_fit(memory_blocks, processes):
    # Store allocation details
    allocation = [-1] * len(processes)  # -1 means the process is not allocated

    for i, process in enumerate(processes):
        best_block_idx = -1

        for j, block in enumerate(memory_blocks):
            if block >= process:
                if best_block_idx == -1 or memory_blocks[j] < memory_blocks[best_block_idx]:
                    best_block_idx = j

        if best_block_idx != -1:
            allocation[i] = best_block_idx
            memory_blocks[best_block_idx] -= process

    return allocation, memory_blocks

# Initial memory blocks (in KB)
memory_blocks = [150, 200, 250, 50, 100]

# Processes to be allocated (in KB)
processes = [120, 230, 30]

# Run the Best Fit Algorithm
allocation, updated_blocks = best_fit(memory_blocks, processes)

# Display results
print("Process Allocation Results:")
for i, block in enumerate(allocation):
    if block != -1:
        print(f"Process {i + 1} (Size: {processes[i]} KB) allocated to Block {block + 1}.")
    else:
        print(f"Process {i + 1} (Size: {processes[i]} KB) could not be allocated.")

print("\nFinal Memory State:")
for i, block in enumerate(updated_blocks):
    print(f"Block {i + 1}: {block} KB (free)")
