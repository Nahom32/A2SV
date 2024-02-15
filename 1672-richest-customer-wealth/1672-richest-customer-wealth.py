class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        total = sum(accounts[0])
        for i in range(1, len(accounts)):
            var = sum(accounts[i])
            if var > total:
                total = var
        return total
        
        