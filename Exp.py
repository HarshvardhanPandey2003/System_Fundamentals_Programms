def fifo_disk_scheduling(requests):
    seek_count = 0
    current_track = 0

    for request in requests:
        seek_count += abs(current_track - request)
        current_track = request

    return seek_count

# Example Usage
requests = [98, 183, 37, 122, 14, 124, 65, 67]
fifo_result = fifo_disk_scheduling(requests)
print(f"FIFO Disk Scheduling Seek Count: {fifo_result}")


def sstf_disk_scheduling(requests):
    seek_count = 0
    current_track = 0

    while requests:
        closest_request = min(requests, key=lambda x: abs(x - current_track))
        seek_count += abs(current_track - closest_request)
        current_track = closest_request
        requests.remove(closest_request)

    return seek_count

# Example Usage
requests = [98, 183, 37, 122, 14, 124, 65, 67]
sstf_result = sstf_disk_scheduling(requests)
print(f"SSTF Disk Scheduling Seek Count: {sstf_result}")


def scan_disk_scheduling(requests, start_direction="left"):
    seek_count = 0
    current_track = 0

    if start_direction == "left":
        requests.sort()
    else:
        requests.sort(reverse=True)

    for request in requests:
        seek_count += abs(current_track - request)
        current_track = request

    return seek_count

# Example Usage
requests = [98, 183, 37, 122, 14, 124, 65, 67]
scan_result = scan_disk_scheduling(requests, start_direction="left")
print(f"SCAN Disk Scheduling Seek Count: {scan_result}")


def c_scan_disk_scheduling(requests, start_direction="left"):
    seek_count = 0
    current_track = 0

    if start_direction == "left":
        requests.sort()
    else:
        requests.sort(reverse=True)

    for request in requests:
        seek_count += abs(current_track - request)
        current_track = request

    # Move to the other end of the disk
    seek_count += abs(current_track - (0 if start_direction == "left" else max(requests)))

    return seek_count

# Example Usage
requests = [98, 183, 37, 122, 14, 124, 65, 67]
c_scan_result = c_scan_disk_scheduling(requests, start_direction="left")
print(f"C-SCAN Disk Scheduling Seek Count: {c_scan_result}")


def look_disk_scheduling(requests, start_direction="left"):
    seek_count = 0
    current_track = 0

    if start_direction == "left":
        requests.sort()
    else:
        requests.sort(reverse=True)

    for request in requests:
        seek_count += abs(current_track - request)
        current_track = request

    return seek_count

# Example Usage
requests = [98, 183, 37, 122, 14, 124, 65, 67]
look_result = look_disk_scheduling(requests, start_direction="left")
print(f"Look Disk Scheduling Seek Count: {look_result}")
