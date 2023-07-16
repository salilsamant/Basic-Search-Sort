#Insertion Sort Algorithm in Python

def insertion_sort(arr):
	sorted=1
	while sorted<len(arr):
	  i=sorted
	  while i > 0 and arr[i-1]>arr[i]:
	 		arr[i-1],arr[i]=arr[i],arr[i-1]
	 		i-=1
			
	  sorted+=1
	  
	return arr

my_arr = [4,1,5,1,2,3]
print(insertion_sort(my_arr))