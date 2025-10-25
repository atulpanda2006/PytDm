class Solution:
    def totalMoney(self, n: int) -> int:
        i=1
        count=1
        
        sum=0
        while count<=n:
                    sum += i
                    if count%7==0:
                        i=(count//7)+1
                    else:

                        i+=1
                    count+=1
        return sum

        
