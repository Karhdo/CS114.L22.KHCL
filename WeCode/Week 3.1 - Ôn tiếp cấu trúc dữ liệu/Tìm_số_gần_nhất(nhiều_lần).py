from bisect import bisect_left
from sys import stdin

n = int(input())
arr = [int(i) for i in stdin.readline().split()]

def Index_closeX(arr, x):
	return bisect_left(arr, x)

def Print_k_closeX(arr, k, x):
	temp_arr = []
	index = Index_closeX(arr, x)
	if index == 0:
		return arr[0:k]
	elif index == len(arr)-1 or index == len(arr):
		return arr[len(arr)-k:len(arr)]
	else:
		left = index
		right = index + 1
		if x-arr[left] <= arr[right]-x:
			temp_arr.append(arr[left])
			left -= 1
		else:
			temp_arr.append(arr[right])
			right += 1
		k -= 1
	while k!=0:
		if left < 0 and right < len(arr)-1:
			temp_arr.append(arr[right])
			right += 1
		elif left >= 0 and right > len(arr)-1:
			temp_arr.append(arr[left])
			left -= 1
		else:
			if x - arr[left] <= arr[right] - x:
				temp_arr.append(arr[left])
				left -= 1
			else:
				temp_arr.append(arr[right])
				right += 1
		k -= 1
	temp_arr.sort()
	return temp_arr

while True:
	k_x = [int(i) for i in stdin.readline().split()]
	if len(k_x) == 0:
		break
	else:
		final_result = Print_k_closeX(arr, k_x[0], k_x[1])
		print(final_result[0], final_result[-1])
