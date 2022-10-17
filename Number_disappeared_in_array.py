class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        result = []  #to store the missing numbers
        
        for i in range(len(nums)):  #to iterate through the loops
            
            index = abs(nums[i])-1  #index is used here to find whether we encountered the num or not, so we are reducing the i by -1 and storing it in the index var. 
            
            if nums[index]>0:   #if the nums[index] is positive we multiply that value with -1 to identify that we encountered this number
                nums[index]*=-1
                
        for j in range(len(nums)):  #we are using another loop to append the missing numbers
            
            if nums[j]>0:   #if the nums in list is positive that is the value missing  
                result.append(j+1)  #so we are adding 1 with the index and appending it in the resultant array
                
            else:
                continue
                
        return result  #returning the missing num list
                
            
        