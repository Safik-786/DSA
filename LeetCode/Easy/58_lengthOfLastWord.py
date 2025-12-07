arr= [1,2,9]

num_str = ''.join(map(str, arr))  # Convert each int to str and join → "99"
print("num_str= ", num_str)
num = int(num_str)  # Convert to integer → 99print(numb)

temp = num + 1  # temp = 100
digits = list(str(temp))  # Split into ['1', '0', '0']
print(digits)




class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # numb= ",".join(map(str, digits))
        # temp= (int(numb))+1
        # ans= list(str(temp))
        # return ans

        num_str = ''.join(map(str, digits))  # Convert each int to str and join → "99"
        num = int(num_str)  # Convert to integer → 99print(numb)

        temp = num + 1  # temp = 100
        digits = list(str(temp))  # Split into ['1', '0', '0']
        ans= map(int, digits)
        return (ans)
    
    
    
class Solution(object):
    def plusOne(self, digits):
        n = len(digits)
        
        for i in range(n - 1, -1, -1):  # Traverse from right to left
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0  # Set to 0 and carry over 1
        
        # If all digits were 9 (e.g., [9,9] → [1,0,0])
        return [1] + digits