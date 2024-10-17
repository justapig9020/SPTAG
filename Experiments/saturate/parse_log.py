import re
import os
import fnmatch
import csv

file_format= "saturate-*.log"

to_parse = []
# list all the files with the format
for file in os.listdir("."):
    if fnmatch.fnmatch(file, file_format):
        to_parse.append(file)

# sort the files
to_parse = [(re.findall("[0-9]+", name)[0], name) for name in to_parse]
to_parse.sort(key=lambda x: int(x[0]))
threads = [int(threads) for threads, _ in to_parse]
to_parse = [name for _, name in to_parse]

def get_qps(file):
    with open(file, "r") as f:
        log = f.read()
        qps = [float(q) for q in re.findall(r"actuallQPS is ([0-9]+.[0-9]+)", log)]
    return qps

all_qps = [get_qps(file) for file in to_parse]
qps = [qps[0] for qps in all_qps]


# Ensure the lengths of both arrays are the same
if len(threads) != len(qps):
    print("Error: The lengths of the threads and qps arrays must be the same.")
else:
    # Open a new CSV file to write
    with open('threads_qps.csv', mode='w', newline='') as file:
        writer = csv.writer(file)

        # Write the header
        writer.writerow(['Thread', 'QPS'])

        # Write each thread and its corresponding qps to the file
        for thread, qps_value in zip(threads, qps):
            writer.writerow([thread, qps_value])

    print("CSV file 'threads_qps.csv' created successfully!")

