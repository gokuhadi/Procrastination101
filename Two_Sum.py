#Array consists of random numbers.
#We need this code to look for ANY 2 numbers which when
#added, will give a value equal to the target
nums=[5,76,1,6,38,2,66]
target=40

for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        total=(nums[i] + nums[j])
        if total==target:
            print (nums[i])
            print (nums[j])
            print (" index on i is " + str(i))
            print ("index on j is "+ str(j))
