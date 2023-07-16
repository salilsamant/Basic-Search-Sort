#Insertion Sort Algorithm in Python

def insertion_sort(arr):
	for i in range(len(arr)-1): # Note we if we have n elements we iterate n-1 times 
	 x=i
	 inserted = False
	 while x >= 0 and not inserted:
	 	if arr[x]>arr[x+1]:
	 		arr[x],arr[x+1]=arr[x+1],arr[x]
	 		x-=1
	 	else: inserted=True

	return arr

my_arr = [4,1,5,1,2,3]
print(insertion_sort(my_arr))