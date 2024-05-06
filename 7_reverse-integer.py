class Solution:
    def reverse(self, x: int) -> int:
        result=0
        while x>=10 or x<=-10:
            reminder=x%10
            if x<=0 and reminder!=0:
                reminder=10-reminder
            x=x//10
            if x<=0 and reminder!=0:
                x+=1
            if x>=0:
                result=(result+reminder)*10
            else:
                result=(result-reminder)*10
        result=result+x
        if result>(2**31 - 1) or result<-2**31:
            return 0
        return result


        