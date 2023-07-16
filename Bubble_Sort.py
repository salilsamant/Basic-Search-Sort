#Bubble Sort Algorithm in Python

def Bubble_Sort(arr):
	unsorted = len(arr)
	sorted = False

	while unsorted > 0 and not sorted:
	 	sorted=True
	 	for i in range(unsorted-1): # Note we if we have n elements we iterate n-1 times 
	 		if arr[i]>arr[i+1]:
	 			arr[i],arr[i+1]=arr[i+1],arr[i]
	 			sorted=False

	unsorted-=1
	return arr

my_arr = [4,1,5,1,2,3]
print(Bubble_Sort(my_arr))
