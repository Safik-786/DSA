
# Example 1:

# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Incrementing by one gives 123 + 1 = 124.
# Thus, the result should be [1,2,4].
# Example 2:

# Input: digits = [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
# Incrementing by one gives 4321 + 1 = 4322.
# Thus, the result should be [4,3,2,2].
# Example 3:

# Input: digits = [9]
# Output: [1,0]
# Explanation: The array represents the integer 9.
# Incrementing by one gives 9 + 1 = 10.
# Thus, the result should be [1,0].




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
    
    
    
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n= len(digits)
        carry= 1
        for i in range(n-1, -1, -1):
            total= digits[i] + carry
            digits[i]= total % 10 
            carry= total // 10
        if carry:
            digits.insert(0, 1)
        return digits