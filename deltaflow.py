import psutil
import os

class DeltaFlow:
    def __init__(self):
        self.processes = []

    def list_processes(self):
        """List all active processes"""
        self.processes = [(p.info['pid'], p.info['name']) for p in psutil.process_iter(['pid', 'name'])]
        return self.processes

    def optimize_process(self, pid, priority):
        """Optimize process by setting its priority"""
        try:
            process = psutil.Process(pid)
            process.nice(priority)
            print(f"Set priority of process {pid} to {priority}")
        except psutil.NoSuchProcess:
            print(f"No process found with PID: {pid}")
        except psutil.AccessDenied:
            print(f"Access denied to process with PID: {pid}")

    def allocate_resources(self, pid, cpu_percent):
        """Allocate CPU resources to a process"""
        try:
            process = psutil.Process(pid)
            process.cpu_affinity([i for i in range(os.cpu_count())])
            process.cpu_percent(cpu_percent)
            print(f"Allocated {cpu_percent}% CPU to process {pid}")
        except psutil.NoSuchProcess:
            print(f"No process found with PID: {pid}")
        except psutil.AccessDenied:
            print(f"Access denied to process with PID: {pid}")

    def manage_resources(self):
        """Automatically manage resources based on usage"""
        for process in self.processes:
            pid, name = process
            try:
                proc = psutil.Process(pid)
                cpu_usage = proc.cpu_percent(interval=1)
                if cpu_usage > 80:
                    self.optimize_process(pid, psutil.HIGH_PRIORITY_CLASS)
                elif cpu_usage < 20:
                    self.optimize_process(pid, psutil.IDLE_PRIORITY_CLASS)
            except psutil.NoSuchProcess:
                continue

if __name__ == "__main__":
    delta_flow = DeltaFlow()
    print("Active Processes:")
    for pid, name in delta_flow.list_processes():
        print(f"PID: {pid}, Name: {name}")

    # Example usage
    pid_to_optimize = int(input("Enter PID to optimize: "))
    delta_flow.optimize_process(pid_to_optimize, psutil.NORMAL_PRIORITY_CLASS)
    delta_flow.allocate_resources(pid_to_optimize, 50)
    delta_flow.manage_resources()