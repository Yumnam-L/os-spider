class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.start_time = 0
        self.completion_time = 0
        self.turnaround_time = 0
        self.waiting_time = 0

def fifo_scheduling(processes):
    current_time = 0
    for process in processes:
        if current_time < process.arrival_time:
            current_time = process.arrival_time
        process.start_time = current_time
        process.completion_time = process.start_time + process.burst_time
        process.turnaround_time = process.completion_time - process.arrival_time
        process.waiting_time = process.turnaround_time - process.burst_time
        current_time += process.burst_time

def calculate_average_times(processes):
    total_turnaround_time = 0
    total_waiting_time = 0
    n = len(processes)
    for process in processes:
        total_turnaround_time += process.turnaround_time
        total_waiting_time += process.waiting_time
    average_turnaround_time = total_turnaround_time / n
    average_waiting_time = total_waiting_time / n
    return average_turnaround_time, average_waiting_time

# Example usage:
processes = [
    Process(1, 0, 4),
    Process(2, 1, 3),
    Process(3, 2, 1),
    Process(4, 3, 2),
]

fifo_scheduling(processes)

average_turnaround_time, average_waiting_time = calculate_average_times(processes)

print("PID | Arrival | Burst | Start | Completion | Turnaround | Waiting")
for process in processes:
    print(f"{process.pid:3} | {process.arrival_time:7} | {process.burst_time:5} | {process.start_time:5} | {process.completion_time:10} | {process.turnaround_time:10} | {process.waiting_time:7}")

print(f"\nAverage Turnaround Time: {average_turnaround_time:.2f}")
print(f"Average Waiting Time: {average_waiting_time:.2f}")
