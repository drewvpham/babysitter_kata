'''
The babysitter 
- starts no earlier than 5:00PM
- leaves no later than 4:00AM
- gets paid $12/hour from start-time to bedtime
- gets paid $8/hour from bedtime to midnight
- gets paid $16/hour from midnight to end of job
- gets paid for full hours (no fractional hours)
'''

pay_regular = 12
pay_bedtime = 8
pay_midnight = 16

def pay_calc(start_time, end_time, bed_time):
    if start_time == 12:
        end_time = end_time + 12
        return pay_midnight * (end_time - start_time)

    if bed_time < end_time:
        return (end_time - bed_time) * pay_bedtime + \
        (bed_time - start_time) * pay_regular

    if bed_time == start_time:
        return (end_time - start_time) * pay_bedtime

    return (end_time - start_time) * pay_regular