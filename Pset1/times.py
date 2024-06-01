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

nums = [] 
comp_times1 = []
comp_times2 = []
comp_times3 = []

# Loop over numbers mentioned in pset
for exponent in [100, 250, 600, 1400]:
    num = 2 ** exponent
    nums.append(math.log10(num))  # Store log10 of the number for plotting purposes
    
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
plt.xlabel(r"$\log_{10}{n}$")

# Plot the data 
plt.plot(nums, comp_times1, label='zeros')
plt.plot(nums, comp_times2, label='zeros2')
plt.plot(nums, comp_times3, label='zeros3')

# Display labels and plot
plt.legend()

# Save the plot with specified DPI, format, and without cropping
plt.savefig('comparison_plot.png', dpi=400, format='jpg', bbox_inches='tight')  

# Show the plot
plt.show()
