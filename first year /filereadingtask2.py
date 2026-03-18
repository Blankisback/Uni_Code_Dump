filename = "testlog.txt"
def count_log_entries(filename):
    total_entries = 0
    ok_count = 0
    error_count = 0
    
    try:
        f = open(filename, 'r')  
        for line in f:
            print(line)
            line = line.strip()
            if line:  
                total_entries += 1
                if "OK" in line:
                    ok_count += 1
                if "ERROR" in line:
                     error_count += 1
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return
    
    print(f"Total entries: {total_entries}")
    print(f"Successful tests (OK): {ok_count}")
    print(f"Errors (ERROR): {error_count}")

count_log_entries("testlog.txt")