# Binary Search Algorithm

def Binary_Search(list,item):
	low = 0
	high = len(list)-1
	
	while low <= high:
		mid = low + (high - low)//2
		if list[mid] == item:
		 return mid
		if list[mid] < item:
			low = mid+1
		else:
			high = mid-1
	return None



my_list = [1,3,5,7,9]

print (Binary_Search(my_list,7))
#print (Binary_Search(my_list,-1))




