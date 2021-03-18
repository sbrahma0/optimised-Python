# https://www.geeksforgeeks.org/job-sequencing-problem/
def job_scheduler(arr, t):
    arr = sorted(arr, key=lambda x:x[2], reverse=True)
    #arr = sorted(arr, key=lambda x:x[1], reverse=True)
    seq = [False]*t
    job = ['']*t
    print(arr)
    for i in range(len(arr)):
        for j in range(min(t-1, arr[i][1]-1),-1,-1): # since we want to add this to the last sec, so it will start from min of last or                                                          time of the task index
            if seq[j]==False:
                seq[j]=True
                job[j]=arr[i][0]
                break # since once it is alloted we dont need to continue the loop
    print(job)
    return

# Driver COde 
arr = [['a', 2, 100],  # Job Array 
       ['b', 1, 19], 
       ['c', 2, 27], 
       ['d', 1, 25], 
       ['e', 3, 15]] 

  
job_scheduler(arr,3)  
#print("Following is maximum profit sequence of jobs") 
# o(nt) t being time and n being length of the array
