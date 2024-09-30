import csv

def read_mechanical_data(filename):
    """
    Read mechanical data from a CSV file.
    
    Args:
    filename (str): Name of the CSV file
    
    Returns:
    list of tuples: List of (time, position, force) tuples
    """
    # TODO: Implement reading from CSV file
    mechanical_data = []
    with open(filename, mode='r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader) # Skipping the header row
        for row in csv_reader:
            time = float(row[0])
            position = float(row[1])
            force = float(row[2])
            mechanical_data.append((time, position, force))
    return mechanical_data

def calculate_velocity(position_data, time_step):
    """
    Calculate velocity from position data.
    
    Args:
    position_data (list of tuples): List of (time, position) tuples
    time_step (float): Time step between measurements
    
    Returns:
    list of tuples: List of (time, velocity) tuples
    """
    # TODO: Implement velocity calculation
    velocity_data = []

    for i in range(1, len(position_data)):
        time_prev, position_prev = position_data[i - 1]
        time_curr, position_curr = position_data[i]

        # Calculate Velocity = change in position / time_step
        velocity = (position_curr - position_prev) / time_step

        # For the velocity time stamp, we can use the mid-point between previous and current time
        time_midpoint = (time_prev + time_curr) / 2
        velocity_data.append((time_midpoint, velocity))
    return velocity_data

def calculate_acceleration(velocity_data, time_step):
    """
    Calculate acceleration from velocity data.
    
    Args:
    velocity_data (list of tuples): List of (time, velocity) tuples
    time_step (float): Time step between measurements
    
    Returns:
    list of tuples: List of (time, acceleration) tuples
    """
    # TODO: Implement acceleration calculation
    acceleration_data = []

    for i in range(1, len(velocity_data)):
        time_prev, velocity_prev = velocity_data[i - 1]
        time_curr, velocity_curr = velocity_data[i]

        # Calculate acceleration = change in velocity / time_step
        acceleration = (velocity_curr - velocity_prev) / time_step
        time_midpoint = (time_prev + time_curr) / 2
        acceleration_data.append(time_midpoint, acceleration)
    return acceleration_data

def find_max_force(force_data):
    """
    Find the maximum force applied to the system.
    
    Args:
    force_data (list of tuples): List of (time, force) tuples
    
    Returns:
    tuple: (time, max_force)
    """
    # TODO: Implement maximum force calculation
    forces = []
    for i in force_data:
        time, force = i
        forces.append(force)

    max_force = max(forces)
    return max_force
        

def calculate_work_done(force_data, position_data):
    """
    Calculate the total work done on the system.
    
    Args:
    force_data (list of tuples): List of (time, force) tuples
    position_data (list of tuples): List of (time, position) tuples
    
    Returns:
    float: Total work done
    """
    # TODO: Implement work done calculation
    # Initializing total_work to 0
    total_work = 0
    # We must ensure that force_data and position_data are of the same length
    if len(force_data) != len(position_data):
        raise ValueError("force_data and position_data must have the same length")
    
    for i in range(1, len(force_data)):
        force_prev = force_data[i - 1][1]
        force_curr = force_data[i][1]
        avg_force = (force_prev + force_curr) / 2

        position_prev = position_data[i - 1][1]
        position_curr = position_data[i][1]
        delta_position = position_curr - position_prev

        # Calculating work done = F_avg * delta x
        work_done = avg_force * delta_position
        total_work += work_done
    return total_work

    

def write_results(filename, results_data):
    """
    Write calculation results to a CSV file.
    
    Args:
    filename (str): Name of the output CSV file
    results_data (dict): Dictionary containing results to be written
    """
    # TODO: Implement writing results to CSV file
    with open(filename, mode='w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(results_data.keys())
        writer.writerow(results_data.values())
    print(f"Results succesfully written to {filename}")


def main():
    input_file = "mechanical_data.csv"
    output_file = "analysis_results.csv"
    time_step = 0.1  # s

    try:
        # Read mechanical data
        data = read_mechanical_data(input_file)

        # Extract position and force data
        time_data = [item[0] for item in data]
        position_data = [(item[0], item[1]) for item in data]
        force_data = [(item[0], item[2]) for item in data]

        # Calculate velocity and acceleration
        velocity_data = calculate_velocity(position_data, time_step)
        acceleration_data = calculate_acceleration(velocity_data, time_step)

        # Find maximum force
        max_force_time, max_force = find_max_force(force_data)

        # Calculate work done
        work_done = calculate_work_done(force_data, position_data)

        # Prepare results
        results = {
            "velocity": velocity_data,
            "acceleration": acceleration_data,
            "max_force": (max_force_time, max_force),
            "work_done": work_done
        }

        # Write results to file
        write_results(output_file, results)
        print(f"Results written to {output_file}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()