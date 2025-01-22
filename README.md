# DeltaFlow

DeltaFlow is a utility that manages and optimizes the allocation of system resources to active processes in Windows environments. It allows users to list active processes, change process priority, allocate CPU resources, and automatically manage resources based on usage patterns.

## Features

- **List Active Processes**: View all currently active processes.
- **Optimize Process Priority**: Change priority levels of processes.
- **Allocate CPU Resources**: Specify CPU usage for each process.
- **Automatic Resource Management**: Adjusts resource allocation based on process usage.

## Requirements

- Python 3.x
- `psutil` library (Install using `pip install psutil`)

## Usage

1. **List Active Processes**: Run the program to see a list of active processes with their PIDs and names.
2. **Optimize Process**: Enter the PID of the process to adjust its priority.
3. **Allocate Resources**: Specify the percentage of CPU to allocate to a specific process.
4. **Manage Resources**: Automatically optimize resources based on process CPU usage.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/deltaflow.git
   ```
2. Navigate to the project directory:
   ```bash
   cd deltaflow
   ```
3. Install the requirements:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Program

To run DeltaFlow, execute:

```bash
python deltaflow.py
```

Follow the on-screen instructions to manage and optimize your system resources.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.