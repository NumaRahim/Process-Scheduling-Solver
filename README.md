# Process-Scheduling-Solver
This project implements a Process Scheduler Algorithm in Python that calculates the Turnaround Time and Waiting Time based on various scheduling algorithms.

<img width="317" alt="screenshot" src="https://github.com/user-attachments/assets/98bcde17-014f-413c-9e99-3375b0281472">

### Supported algorithms

* First Come First Serve / FCFS
* Shortest Job First / SJF (non-preemptive)
* Shortest Remaining Time First / SRTF (preemptive)
* Round-Robin / RR
* Priority (non-preemptive)
* Priority (preemptive)

## Features
* User-Friendly Interface
Graphical User Interface (GUI): Easy-to-use interface built with Tkinter for inputting process details and viewing simulation results.
* Process Input: Allows users to input Process ID, Arrival Time, Burst Time, Priority, and Time Quantum.

## GUI Components
**Process ID Entry:** Input for process ID.
**Arrival Time Entry:** Input for process arrival time.
**Burst Time Entry:** Input for process burst time.
**Priority Entry:** Input for process priority.
**Time Quantum Entry:** Input for time quantum (used in Round Robin scheduling).
## Buttons:
**Add Process:** Adds the process to the list.
**Simulate FCFS:** Simulates FCFS scheduling.
**Simulate SJF:** Simulates SJF scheduling.
**Simulate SJF Preemptive:** Simulates Preemptive SJF scheduling.
**Simulate Priority:** Simulates Priority scheduling.
**Simulate Priority Preemptive:** Simulates Preemptive Priority scheduling.
**Simulate Round Robin:** Simulates Round Robin scheduling.

## Appendix
## Scheduling Algorithms Overview
* FCFS (First-Come, First-Served): Processes are executed in the order they arrive.
* SJF (Shortest Job First): Processes with the shortest burst time are executed first.
* Preemptive SJF: Similar to SJF, but allows interruption of currently running processes if a new process with a shorter burst time arrives.
* Priority Scheduling: Processes are executed based on their priority. Lower priority numbers are executed first.
* Preemptive Priority Scheduling: Allows interruption of currently running processes if a new process with a higher priority arrives.
Round Robin (RR): Each process is given a fixed time quantum and cycles through all processes until completion.

## Contributing
Contributions are welcome! 

## Author
-Numa Rahim https://github.com/NumaRahim

## License





