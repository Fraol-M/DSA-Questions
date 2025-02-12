# Problem: Selection Sort - https://practice.geeksforgeeks.org/problems/selection-sort/1

#User function Template for python3

class Solution: 
    def selectionSort(self, arr):
        n = len(arr)
        for i in range(n):
            min_index = i
            for j in range(i+1,n):
                if arr[j] < arr[min_index]:
                    min_index = j
            arr[min_index],arr[i] = arr[i],arr[min_index]
        return arr