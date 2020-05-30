class Sol:
    def find_max_continuos_increasing_subarray(self,arr):
        list_of_ones=[1 for x in range(len(arr))]
        for i in range(1,len(list_of_ones)):
            if arr[i]>arr[i-1]:
                list_of_ones[i]+=list_of_ones[i-1]
        return max(list_of_ones)


if __name__ == '__main__':
    p=Sol()
    print(p.find_max_continuos_increasing_subarray([-1,3,4,5,2,2,2,2]))
