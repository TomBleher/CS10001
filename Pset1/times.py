import time
import matplotlib.pyplot as plt
import math  # Ensure math is imported

def zeros(num):
    m = num
    cnt = 0
    while m > 0:
        if m % 10 == 0:
            cnt += 1
        m = m // 10
    return cnt

def zeros2(num):
    cnt = 0
    snum = str(num)
    for digit in snum:
        if digit == "0":
            cnt += 1
    return cnt

def zeros3(num):
    cnt = str(num).count("0")
    return cnt

nums_log = [] 
comp_times1 = []
comp_times2 = []
comp_times3 = []

# Loop over numbers mentioned in pset
for num in [1e10, 2e10, 3e10, 4e10, 5e10, 6e10, 7e10, 8e10, 9e10, 10e10]:
    nums_log.append(num)  # Store log10 of the number for plotting purposes
    
    t0 = time.perf_counter()
    zeros(num)
    t1 = time.perf_counter()
    comp_times1.append(t1 - t0)
    
    t0 = time.perf_counter()
    zeros2(num)
    t1 = time.perf_counter()
    comp_times2.append(t1 - t0)
    
    t0 = time.perf_counter()
    zeros3(num)
    t1 = time.perf_counter()
    comp_times3.append(t1 - t0)

# Give the plot axes labels
plt.ylabel(r"$t_{s}$")
plt.xlabel(r"$n$")

# Plot the data 
plt.plot(nums_log, comp_times1, label='zeros')
plt.plot(nums_log, comp_times2, label='zeros2')
plt.plot(nums_log, comp_times3, label='zeros3')

# Display labels and plot
plt.legend()

plt.savefig('log.png', dpi=400, format='jpg', bbox_inches='tight')  
plt.show()
