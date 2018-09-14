#Question problem
'''After a long and successful day of preparing food for the banquet,
it is time to clean up. There is a list of n jobs to do before the
kitchen can be closed for the night. These jobs are indexed from 1
to n.

Most of the cooks have already left and only the Chef and his assistant
are left to clean up. Thankfully, some of the cooks took care of some of
the jobs before they left so only a subset of the n jobs remain. The Chef
and his assistant divide up the remaining jobs in the following manner.
The Chef takes the unfinished job with least index, the assistant takes
the unfinished job with the second least index, the Chef takes the unfinished
job with the third least index, etc. That is, if the unfinished jobs were
listed in increasing order of their index then the Chef would take every
other one starting with the first job in the list and the assistant would
take every other one starting with the second job on in the list.

The cooks logged which jobs they finished before they left. Unfortunately,
these jobs were not recorded in any particular order. Given an unsorted
list of finished jobs, you are to determine which jobs the Chef must complete
and which jobs his assitant must complete before closing the kitchen for the
evening.'''

cases = int(input())

#Declaration of lists
cheif = []
assistant = []
jobs = []

for case in range(0, cases):
    n, m = map(int, input().split())
    jobDone = list(map(int, input().split()))

    #Sort the list "JobDone"
    jobDone.sort()

    #Calculating the remaining jobs
    for i in range(1, n+1):
        if i in jobDone:
            continue
        jobs.append(i)

    #Assigning jobs to the chief and his/her assistant
    for j in range(0, len(jobs)):
        if (j+1)%2==0:
            assistant.append(jobs[j])
        else:
            cheif.append(jobs[j])

    #Print all the required outputs
    for i in cheif:
        print(i,end=' ')
    print('')
    for i in assistant:
        print(i,end=' ')
    print('')

    #Empty all the lists
    del cheif[:]
    del assistant[:]
    del jobDone[:]
    del jobs[:]
