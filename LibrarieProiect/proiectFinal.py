from collections import*
import re
from datetime import datetime

class Proiect():
    def __init__(self) -> None:
        pass

    def count(self,file_to_read):#1
        with open(file_to_read, mode = "r") as file:
            log_data = file.read()
        
        
        log_entries = re.findall(r"\[([A-Z]+)\] - ([\w]+)", log_data) 
    
        log_counts = Counter()
        for log_type, app in log_entries:
            if log_type == "INFO":
                log_counts[(log_type, app)] += 0.5
            else:
                log_counts[(log_type,app)] += 1
        return log_counts
    

    def average_run_time_excluding_system(self,file_to_read):#2
        with open(file_to_read, 'r') as file:
            log_data = file.readlines()

        total_run_time = {}
        run_counts = {}
        app_avg= {}

        for line in log_data:
            # Check if the line indicates a successful run
            if 'has ran successfully' in line:
                # Use regular expression to find the app name and run time
                match = re.search(r'(\w+) has ran successfully in (\d+)ms', line)
                if match:
                    app_name = match.group(1)
                    run_time = int(match.group(2))

                    # Skip if the app is SYSTEM
                    if app_name == 'SYSTEM':
                        continue

                    # Update the total run time and count
                    if app_name not in total_run_time:
                        total_run_time[app_name] = 0
                        run_counts[app_name] = 0
                    total_run_time[app_name] += run_time
                    run_counts[app_name] += 1

        # Calculate and print the average run time for each app
        for app in total_run_time:
            average_time = total_run_time[app] / run_counts[app]
            app_avg[app]=round(average_time,2)
            print(f"{app} - Average Successful Run Time: {average_time:.2f}ms")
        return app_avg
    

    def count_app_failures3(self,file_to_read):#3

        with open(file_to_read, 'r') as file:
            log_data = file.readlines()

        # Initialize a dictionary to store failure counts for each app
        failure_counts = {'FrontendApp': 0, 'BackendApp': 0, 'API': 0, 'SYSTEM': 0}

        for line in log_data:
            # Check if the line indicates a failure
            if '[ERROR]' in line:
                # Check for each app and increment the count
                if 'FrontendApp' in line:
                    failure_counts['FrontendApp'] += 1
                elif 'BackendApp' in line:
                    failure_counts['BackendApp'] += 1
                elif 'API' in line:
                    failure_counts['API'] += 1
                elif 'SYSTEM' in line:
                    failure_counts['SYSTEM'] += 1

        return failure_counts
    

    def count_app_failures(self,file_to_read):#4
        with open(file_to_read, 'r') as file:
            log_data = file.readlines()

        # Initialize a dictionary to store failure counts for each app
        failure_counts = {'FrontendApp': 0, 'BackendApp': 0, 'API': 0, 'SYSTEM': 0}

        for line in log_data:
            # Check if the line indicates a failure
            if '[ERROR]' in line:
                # Check for each app and increment the count
                if 'FrontendApp' in line:
                    failure_counts['FrontendApp'] += 1
                elif 'BackendApp' in line:
                    failure_counts['BackendApp'] += 1
                elif 'API' in line:
                    failure_counts['API'] += 1
                elif 'SYSTEM' in line:
                    failure_counts['SYSTEM'] += 1

        # Determine the app with the most failures
        most_failed_app = max(failure_counts, key=failure_counts.get)
        most_failures = failure_counts[most_failed_app]

        return most_failed_app, most_failures
    

    def app_with_most_successful_runs(self,file_to_read):#5
        with open(file_to_read, 'r') as file:
            log_data = file.readlines()

        # Initialize a dictionary to store success counts for each app
        success_counts = {'FrontendApp': 0, 'BackendApp': 0, 'API': 0, 'SYSTEM': 0}

        for line in log_data:
            # Check if the line indicates a successful run
            if '[INFO]' in line and 'has ran successfully' in line:
                # Check for each app and increment the count
                if 'FrontendApp' in line:
                    success_counts['FrontendApp'] += 1
                elif 'BackendApp' in line:
                    success_counts['BackendApp'] += 1
                elif 'API' in line:
                    success_counts['API'] += 1
                elif 'SYSTEM' in line:
                    success_counts['SYSTEM'] += 1

        # Determine the app with the most successful runs
        most_successful_app = max(success_counts, key=success_counts.get)
        most_successes = success_counts[most_successful_app]

        return most_successful_app, most_successes
    

    def third_of_day_with_most_failures(self,file_to_read):#6
        with open(file_to_read, 'r') as file:
            log_data = file.readlines()

        first_third, second_third, third_third = 0, 0, 0

        for line in log_data:
            if '[ERROR]' in line:
                try:
                    time_str = line.split(' - ')[0]
                    time_obj = datetime.strptime(time_str, "%H:%M:%S")

                    if time_obj.hour < 8:
                        first_third += 1
                    elif time_obj.hour < 16:
                        second_third += 1
                    else:
                        third_third += 1
                except Exception as e:
                    print(f"Error processing line: {line}\nError: {e}")

        most_failures = max(first_third, second_third, third_third)
        if most_failures == first_third:
            return "00:00:00 - 07:59:59", most_failures
        elif most_failures == second_third:
            return "08:00:00 - 15:59:59", most_failures
        else:
            return "16:00:00 - 23:59:59", most_failures
        

    def run_times_per_app(self,file_to_read):#7
        with open(file_to_read, 'r') as file:
            log_data = file.readlines()

        # Dictionaries to store the longest and shortest run times for each app
        longest_runs = {}
        shortest_runs = {}

        for line in log_data:
            if 'has ran successfully' in line and 'SYSTEM' not in line:
                try:
                    parts = line.split()
                    timestamp = parts[0]
                    app_name = parts[4]
                    run_time_str = [s for s in parts if "ms" in s][0]
                    run_time = int(run_time_str.replace('ms', ''))

                    # Initialize if first occurrence of the app
                    if app_name not in longest_runs:
                        longest_runs[app_name] = (timestamp, run_time)
                        shortest_runs[app_name] = (timestamp, run_time)

                    # Update longest run
                    if run_time > longest_runs[app_name][1]:
                        longest_runs[app_name] = (timestamp, run_time)

                    # Update shortest run
                    if run_time < shortest_runs[app_name][1]:
                        shortest_runs[app_name] = (timestamp, run_time)

                except (ValueError, IndexError) as e:
                    print(f"Error processing line: {line}\nError: {e}")

        return longest_runs, shortest_runs
    

    def busiest_hour_per_app(self,file_to_read):#8
        with open(file_to_read, 'r') as file:
            log_data = file.readlines()

        # Dictionary to store activity counts per hour for each app
        activities_per_hour = defaultdict(lambda: defaultdict(int))

        for line in log_data:
            # Exclude SYSTEM logs
            if 'SYSTEM' not in line:
                # Extract hour and app name
                match = re.search(r'(\d{2}):\d{2}:\d{2} - \[\w+\] - (\w+)', line)
                if match:
                    hour, app_name = match.groups()
                    # Increment the count for the hour for this app
                    activities_per_hour[app_name][hour] += 1

        # Determine the busiest hour for each app
        busiest_hours = {}
        for app, hours in activities_per_hour.items():
            busiest_hour = max(hours, key=hours.get)
            busiest_hours[app] = (busiest_hour, hours[busiest_hour])

        return busiest_hours
    
    def calculate_failure_rates(self,file_to_read):#9
        with open(file_to_read, 'r') as file:
            log_data = file.readlines()

        # Dictionaries to store total and error log counts for each app
        total_logs = defaultdict(int)
        error_logs = defaultdict(int)

        for line in log_data:
            # Extract log type and app name
            match = re.search(r'\[\w+\] - (\w+)', line)
            if match:
                app_name = match.group(1)
                # Count each log for the app
                total_logs[app_name] += 1
                # Count only error logs for the app
                if '[ERROR]' in line:
                    error_logs[app_name] += 1

        # Calculate and store failure rates for each app
        failure_rates = {}
        for app in total_logs:
            if total_logs[app] > 0:  # Prevent division by zero
                rate = (error_logs[app] / total_logs[app]) * 100
                failure_rates[app] = round(rate,2)
                
        return failure_rates