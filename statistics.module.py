# calculate the mean ,median,mode
import statistics
data=[1,2,2,3,4,4,4,4,3,3]

mean=statistics.mean(data)

print("mean is:",mean)

# calculate the median function

median=statistics.median(data)
print("median is :",median)

# calculate the mode function 
data2=[22,24,27,22,22,23,26,26,28]
mode=statistics.mode(data2)
print("mode is :",mode)

# stdev () fuction is used tofind the standard deviation

stdev=statistics.stdev(data)
print("standard devitation:", stdev)

data3=[4,6,3,5,7,7]
 
l_median=statistics.median_low(data3)
print("low median :",l_median)

h_median=statistics.median_high(data3) 
print("high median:", h_median)