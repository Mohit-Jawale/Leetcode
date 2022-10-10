class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        cost_dict = {}
        
        def climbling_cost(n):
            nonlocal cost_dict
            if n ==0:
                return 0
            if n==1:
                return cost[n-1]
            if n==2:
                return cost[n-1]
            if n in cost_dict:
                return cost_dict[n]
            
            
            min_cost = min(climbling_cost(n-1) , climbling_cost(n-2))
            cost_dict[n] = min_cost + cost[n-1]
            
            return min_cost + cost[n-1]
        
        
        cost.append(0)
        return (climbling_cost(len(cost)))
