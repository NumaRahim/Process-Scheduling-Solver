import tkinter as tk
from tkinter import messagebox

processes = []

def add_process():
    process_id = int(process_id_entry.get())
    arrival_time = int(arrival_time_entry.get())
    burst_time = int(burst_time_entry.get())
    priority = int(priority_entry.get())
    processes.append((process_id, arrival_time, burst_time, priority))
    process_id_entry.delete(0, tk.END)
    arrival_time_entry.delete(0, tk.END)
    burst_time_entry.delete(0, tk.END)
    priority_entry.delete(0, tk.END)

def simulate_fcfs():
    output_text.delete(1.0, tk.END)
    waiting_times = [0] * len(processes)
    turnaround_times = [0] * len(processes)
    for i in range(len(processes)):
        if i > 0:
            waiting_times[i] = waiting_times[i-1] + processes[i-1][2]
        turnaround_times[i] = waiting_times[i] + processes[i][2]
    output_text.insert(tk.END, "FCFS Output:\n")
    output_text.insert(tk.END, "Process ID\tArrival Time\tBurst Time\tWaiting Time\tTurnaround Time\n")
    for i in range(len(processes)):
        output_text.insert(tk.END, f"{processes[i][0]}\t{processes[i][1]}\t{processes[i][2]}\t{waiting_times[i]}\t{turnaround_times[i]}\n")
    avg_waiting_time = sum(waiting_times) / len(waiting_times)
    avg_turnaround_time = sum(turnaround_times) / len(turnaround_times)
    output_text.insert(tk.END, f"Average Waiting Time: {avg_waiting_time}\n")
    output_text.insert(tk.END, f"Average Turnaround Time: {avg_turnaround_time}\n")

def simulate_sjf():
    output_text.delete(1.0, tk.END)
    processes.sort(key=lambda x: x[2])  # Sort processes by burst time
    waiting_times = [0] * len(processes)
    turnaround_times = [0] * len(processes)
    for i in range(len(processes)):
        if i > 0:
            waiting_times[i] = waiting_times[i-1] + processes[i-1][2]
        turnaround_times[i] = waiting_times[i] + processes[i][2]
    output_text.insert(tk.END, "SJF Output:\n")
    output_text.insert(tk.END, "Process ID\tArrival Time\tBurst Time\tWaiting Time\tTurnaround Time\n")
    for i in range(len(processes)):
        output_text.insert(tk.END, f"{processes[i][0]}\t{processes[i][1]}\t{processes[i][2]}\t{waiting_times[i]}\t{turnaround_times[i]}\n")
    avg_waiting_time = sum(waiting_times) / len(waiting_times)
    avg_turnaround_time = sum(turnaround_times) / len(turnaround_times)
    output_text.insert(tk.END, f"Average Waiting Time: {avg_waiting_time}\n")
    output_text.insert(tk.END, f"Average Turnaround Time: {avg_turnaround_time}\n")

def simulate_sjf_preemptive():
    output_text.delete(1.0, tk.END)
    n = len(processes)
    waiting_times = [0] * n
    turnaround_times = [0] * n
    remaining_times = [proc[2] for proc in processes]
    current_time = 0
    complete = 0
    min_burst_time = float('inf')
    shortest = 0
    check = False

    while complete != n:
        for j in range(n):
            if (processes[j][1] <= current_time and
                remaining_times[j] < min_burst_time and
                remaining_times[j] > 0):
                min_burst_time = remaining_times[j]
                shortest = j
                check = True

        if not check:
            current_time += 1
            continue

        remaining_times[shortest] -= 1
        min_burst_time = remaining_times[shortest]
        if min_burst_time == 0:
            min_burst_time = float('inf')

        if remaining_times[shortest] == 0:
            complete += 1
            check = False
            finish_time = current_time + 1
            waiting_times[shortest] = finish_time - processes[shortest][2] - processes[shortest][1]
            if waiting_times[shortest] < 0:
                waiting_times[shortest] = 0

        current_time += 1

    for i in range(n):
        turnaround_times[i] = processes[i][2] + waiting_times[i]

    output_text.insert(tk.END, "SJF Preemptive Output:\n")
    output_text.insert(tk.END, "Process ID\tArrival Time\tBurst Time\tWaiting Time\tTurnaround Time\n")
    for i in range(len(processes)):
        output_text.insert(tk.END, f"{processes[i][0]}\t{processes[i][1]}\t{processes[i][2]}\t{waiting_times[i]}\t{turnaround_times[i]}\n")
    avg_waiting_time = sum(waiting_times) / len(waiting_times)
    avg_turnaround_time = sum(turnaround_times) / len(turnaround_times)
    output_text.insert(tk.END, f"Average Waiting Time: {avg_waiting_time}\n")
    output_text.insert(tk.END, f"Average Turnaround Time: {avg_turnaround_time}\n")

def simulate_priority():
    output_text.delete(1.0, tk.END)
    processes.sort(key=lambda x: x[3])  # Sort processes by priority
    waiting_times = [0] * len(processes)
    turnaround_times = [0] * len(processes)
    current_time = 0
    for i in range(len(processes)):
        waiting_times[i] = max(0, current_time - processes[i][1])
        current_time += processes[i][2]
        turnaround_times[i] = waiting_times[i] + processes[i][2]
    output_text.insert(tk.END, "Priority Output:\n")
    output_text.insert(tk.END, "Process ID\tArrival Time\tBurst Time\tWaiting Time\tTurnaround Time\n")
    for i in range(len(processes)):
        output_text.insert(tk.END, f"{processes[i][0]}\t{processes[i][1]}\t{processes[i][2]}\t{waiting_times[i]}\t{turnaround_times[i]}\n")
    avg_waiting_time = sum(waiting_times) / len(waiting_times)
    avg_turnaround_time = sum(turnaround_times) / len(turnaround_times)
    output_text.insert(tk.END, f"Average Waiting Time: {avg_waiting_time}\n")
    output_text.insert(tk.END, f"Average Turnaround Time: {avg_turnaround_time}\n")

def simulate_priority_preemptive():
    output_text.delete(1.0, tk.END)
    n = len(processes)
    waiting_times = [0] * n
    turnaround_times = [0] * n
    remaining_times = [proc[2] for proc in processes]
    current_time = 0
    complete = 0
    highest_priority = float('inf')
    highest_priority_index = -1

    while complete != n:
        for j in range(n):
            if (processes[j][1] <= current_time and
                processes[j][3] < highest_priority and
                remaining_times[j] > 0):
                highest_priority = processes[j][3]
                highest_priority_index = j

        if highest_priority_index == -1:
            current_time += 1
            continue

        remaining_times[highest_priority_index] -= 1
        if remaining_times[highest_priority_index] == 0:
            complete += 1
            finish_time = current_time + 1
            waiting_times[highest_priority_index] = finish_time - processes[highest_priority_index][2] - processes[highest_priority_index][1]
            if waiting_times[highest_priority_index] < 0:
                waiting_times[highest_priority_index] = 0
            highest_priority = float('inf')

        current_time += 1

    for i in range(n):
        turnaround_times[i] = processes[i][2] + waiting_times[i]

    output_text.insert(tk.END, "Priority Preemptive Output:\n")
    output_text.insert(tk.END, "Process ID\tArrival Time\tBurst Time\tWaiting Time\tTurnaround Time\n")
    for i in range(len(processes)):
        output_text.insert(tk.END, f"{processes[i][0]}\t{processes[i][1]}\t{processes[i][2]}\t{waiting_times[i]}\t{turnaround_times[i]}\n")
    avg_waiting_time = sum(waiting_times) / len(waiting_times)
    avg_turnaround_time = sum(turnaround_times) / len(turnaround_times)
    output_text.insert(tk.END, f"Average Waiting Time: {avg_waiting_time}\n")
    output_text.insert(tk.END, f"Average Turnaround Time: {avg_turnaround_time}\n")

def simulate_rr():
    output_text.delete(1.0, tk.END)
    time_quantum = int(time_quantum_entry.get())
    waiting_times = [0] * len(processes)
    turnaround_times = [0] * len(processes)
    remaining_times = [proc[2] for proc in processes]
    current_time = 0
    complete = 0

    while complete < len(processes):
        done = True
        for i in range(len(processes)):
            if processes[i][1] <= current_time and remaining_times[i] > 0:
                done = False
                if remaining_times[i] > time_quantum:
                    current_time += time_quantum
                    remaining_times[i] -= time_quantum
                else:
                    current_time += remaining_times[i]
                    waiting_times[i] = current_time - processes[i][2] - processes[i][1]
                    remaining_times[i] = 0
                    complete += 1
        if done:
            current_time += 1

    for i in range(len(processes)):
        turnaround_times[i] = processes[i][2] + waiting_times[i]

    output_text.insert(tk.END, "Round Robin Output:\n")
    output_text.insert(tk.END, "Process ID\tArrival Time\tBurst Time\tWaiting Time\tTurnaround Time\n")
    for i in range(len(processes)):
        output_text.insert(tk.END, f"{processes[i][0]}\t{processes[i][1]}\t{processes[i][2]}\t{waiting_times[i]}\t{turnaround_times[i]}\n")
    avg_waiting_time = sum(waiting_times) / len(waiting_times)
    avg_turnaround_time = sum(turnaround_times) / len(turnaround_times)
    output_text.insert(tk.END, f"Average Waiting Time: {avg_waiting_time}\n")
    output_text.insert(tk.END, f"Average Turnaround Time: {avg_turnaround_time}\n")

# GUI setup
root = tk.Tk()
root.title("CPU Scheduling Simulator")

# Labels and Entries for process details
tk.Label(root, text="Process ID").grid(row=0, column=0)
process_id_entry = tk.Entry(root)
process_id_entry.grid(row=0, column=1)
tk.Label(root, text="Arrival Time").grid(row=1, column=0)
arrival_time_entry = tk.Entry(root)
arrival_time_entry.grid(row=1, column=1)
tk.Label(root, text="Burst Time").grid(row=2, column=0)
burst_time_entry = tk.Entry(root)
burst_time_entry.grid(row=2, column=1)
tk.Label(root, text="Priority").grid(row=3, column=0)
priority_entry = tk.Entry(root)
priority_entry.grid(row=3, column=1)
tk.Label(root, text="Time Quantum").grid(row=4, column=0)
time_quantum_entry = tk.Entry(root)
time_quantum_entry.grid(row=4, column=1)

# Buttons to add processes and simulate algorithms
add_button = tk.Button(root, text="Add Process", command=add_process)
add_button.grid(row=5, column=0, columnspan=2, pady=10)
fcfs_button = tk.Button(root, text="Simulate FCFS", command=simulate_fcfs)
fcfs_button.grid(row=6, column=0, columnspan=2, pady=10)
sjf_button = tk.Button(root, text="Simulate SJF", command=simulate_sjf)
sjf_button.grid(row=7, column=0, columnspan=2, pady=10)
sjf_p_button = tk.Button(root, text="Simulate SJF Preemptive", command=simulate_sjf_preemptive)
sjf_p_button.grid(row=8, column=0, columnspan=2, pady=10)
priority_button = tk.Button(root, text="Simulate Priority", command=simulate_priority)
priority_button.grid(row=9, column=0, columnspan=2, pady=10)
priority_p_button = tk.Button(root, text="Simulate Priority Preemptive", command=simulate_priority_preemptive)
priority_p_button.grid(row=10, column=0, columnspan=2, pady=10)
rr_button = tk.Button(root, text="Simulate Round Robin", command=simulate_rr)
rr_button.grid(row=11, column=0, columnspan=2, pady=10)

# Text widget to display output
output_text = tk.Text(root, height=15, width=50)
output_text.grid(row=12, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
