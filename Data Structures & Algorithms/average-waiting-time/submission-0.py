class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:

        t = 0
        total = 0
        res = []
        for arrival, order in customers:
            t = max(t, arrival) + order
            res.append(t-arrival)
            total += t - arrival
            average = sum(res)/len(res)
        #return total / len(customers)
        return average
