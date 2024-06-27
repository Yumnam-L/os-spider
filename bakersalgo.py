def is_safe(processes, avail, max_demand, allocation):
    n = len(processes)
    m = len(avail)
    
    # Step 1: Calculate Need matrix
    need = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            need[i][j] = max_demand[i][j] - allocation[i][j]
    
    # Step 2: Initialize work and finish
    work = avail[:]
    finish = [False] * n
    
    # Step 3: Find an i such that finish[i] == False and need[i] <= work
    safe_sequence = []
    while len(safe_sequence) < n:
        found = False
        for i in range(n):
            if not finish[i]:
                if all(need[i][j] <= work[j] for j in range(m)):
                    for k in range(m):
                        work[k] += allocation[i][k]
                    safe_sequence.append(i)
                    finish[i] = True
                    found = True
                    break
        
        if not found:
            return False, []
    
    return True, safe_sequence

# Example usage:
processes = [0, 1, 2, 3, 4]
avail = [3, 3, 2]  # Available resources
max_demand = [
    [7, 5, 3],
    [3, 2, 2],
    [9, 0, 2],
    [2, 2, 2],
    [4, 3, 3]
]
allocation = [
    [0, 1, 0],
    [2, 0, 0],
    [3, 0, 2],
    [2, 1, 1],
    [0, 0, 2]
]

safe, sequence = is_safe(processes, avail, max_demand, allocation)

if safe:
    print("The system is in a safe state.")
    print("Safe sequence is:", sequence)
else:
    print("The system is not in a safe state. Deadlock may occur.")
