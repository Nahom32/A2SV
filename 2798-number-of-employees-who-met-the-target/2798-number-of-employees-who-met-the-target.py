class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        no_emp = 0
        for i in hours:
            if i >= target:
                no_emp+=1
        return no_emp
        