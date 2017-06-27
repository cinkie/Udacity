import webbrowser
import time

total_breaks = 3

print("This program started on " + time.ctime())

for i in range(total_breaks):
    time.sleep(10)
    print(str(i+1) + ' time for break at ' + time.ctime())
    webbrowser.open("https://www.youtube.com/watch?v=qgnMRNoT-PM&index=1&list=RDqgnMRNoT-PM")
