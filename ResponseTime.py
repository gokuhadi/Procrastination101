response_time=[1,2,3,4,5]
new_response_time=[5,6,7,8,9,2,33]


def average_rt(average):
    if not average:
        return 0
    x=sum(average)
    length=len(average)
    return x/length
print (average_rt(response_time))
print (average_rt(new_response_time))

