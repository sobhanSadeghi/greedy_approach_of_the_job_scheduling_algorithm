def job_scheduling(jobs):
    sorted_jobs=sorted(jobs,key=lambda x:x[2])
    schedule=[]
    current_time=0


    for job_id,processing_time,deadline in sorted_jobs:
        completion_time=current_time+processing_time

        if completion_time<=deadline:
            start_time=max(current_time,0)
            schedule.append((job_id,start_time,completion_time))
            current_time=completion_time

    return schedule



jobs = [(1, 3, 5), (2, 2, 6), (3, 5, 4), (4, 1, 8)]

result=job_scheduling(jobs)

for jobi_id,start_time,completion_time in result:
    print(f'job id:{jobi_id} start time:{start_time} completion time:{completion_time}')
