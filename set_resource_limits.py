# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 18:28:58 2019

@author: Siddharth Bakshi
"""
import time
import psutil
import os

filename_cgroup = "/sys/fs/cgroup/memory/memory.limit_in_bytes"
filename_all="/proc/meminfo"
with open(filename_all) as f:
    for i in f:
        sline=i.split()
        if (sline[0]=='MemTotal:'):
            total_memory=sline[1]
            break


with open(filename_cgroup) as f:
    content = f.readlines()
 
for line in content:
    memory=line
percent=((int(memory)*0.001)/int(total_memory))*100
#print(percent,int(memory)*math.exp(-6),int(total_memory))

#sys_cores = psutil.cpu_count()
cgroup_cputime_quota_file = open("/sys/fs/cgroup/cpu/cpu.cfs_quota_us","r")
cgroup_cputime_period_file = open("/sys/fs/cgroup/cpu/cpu.cfs_period_us","r")
cg_cores = float(cgroup_cputime_quota_file.readlines()[0][:-1]) / float(cgroup_cputime_period_file.readlines()[0][:-1])
#max_cpu_pct = 100 * cg_cores / sys_cores

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
sys_cores = len(tot_util)
non_boinc_per_core_util = tot_util[int(0.75 * sys_cores) - 1]
boinc_max = 100 - non_boinc_per_core_util

os.environ["boincmaxcpu"] = str(boinc_max)

xml_file='''<global_preferences>
  <run_on_batteries>0</run_on_batteries>
  <run_if_user_active>1</run_if_user_active>
  <run_gpu_if_user_active>0</run_gpu_if_user_active>
  <start_hour>0.000000</start_hour>
  <end_hour>0.000000</end_hour>
  <net_start_hour>0.000000</net_start_hour>
  <net_end_hour>0.000000</net_end_hour>
  <leave_apps_in_memory>0</leave_apps_in_memory>
  <confirm_before_connecting>0</confirm_before_connecting>
  <hangup_if_dialed>0</hangup_if_dialed>
  <dont_verify_images>0</dont_verify_images>
  <work_buf_min_days>0.100000</work_buf_min_days>
  <work_buf_additional_days>0.000000</work_buf_additional_days>
  <max_ncpus_pct>20.000000</max_ncpus_pct>
  <cpu_scheduling_period_minutes>60.000000</cpu_scheduling_period_minutes>
  <disk_interval>60.000000</disk_interval>
  <disk_max_used_gb>100.000000</disk_max_used_gb>
  <disk_max_used_pct>100.000000</disk_max_used_pct>
  <disk_min_free_gb>0.100000</disk_min_free_gb>
  <vm_max_used_pct>75.000000</vm_max_used_pct>
  <ram_max_used_busy_pct>'''+str(percent)+'''</ram_max_used_busy_pct>
  <ram_max_used_idle_pct>100.000000</ram_max_used_idle_pct>
  <max_bytes_sec_up>0.000000</max_bytes_sec_up>
  <max_bytes_sec_down>0.000000</max_bytes_sec_down>
  <cpu_usage_limit>100.000000</cpu_usage_limit>
  <suspend_cpu_usage>10.0</suspend_cpu_usage>
  <daily_xfer_limit_mb>0.000000</daily_xfer_limit_mb>
  <daily_xfer_period_days>0</daily_xfer_period_days>
  <day_prefs> ]
     <day_of_week>0</day_of_week>
     <start_hour>0.00</start_hour>
     <end_hour>24.00</end_hour>
     <net_start_hour>0.00</net_start_hour>
     <net_end_hour>6.00</net_end_hour>
  </day_prefs> ]
  <day_prefs> ]
     <day_of_week>6</day_of_week>
     <start_hour>0.00</start_hour>
     <end_hour>24.00</end_hour>
  </day_prefs>
</global_preferences>'''
f=open("global_prefs_override.xml","w+")
f.write(xml_file)
f.close()