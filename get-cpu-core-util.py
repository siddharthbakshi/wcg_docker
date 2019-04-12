import time
import psutil
util_sum = psutil.cpu_percent(percpu=True)
i = 1
while i < 10:
    time.sleep(0.2)
    new_util = psutil.cpu_percent(percpu=True)
    for j in range(len(util_sum)):
        util_sum[j] += new_util[j]
    i += 1
tot_util = [x/i for x in util_sum]
tot_util.sort()
tot_util[int(0.75 * len(tot_util)) - 1]