"""
Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list of favorite restaurants represented by strings.
You need to help them find out their common interest with the least list index sum. If there is a choice tie between answers, output all of them with no order requirement. 
You could assume there always exists an answer.

Example :
Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
Output: ["Shogun"]
Explanation: The only restaurant they both like is "Shogun".
"""

#Optimal solution (by : awice)
class Solution(object):
    def findRestaurant(self, list1, list2):
        Aindex = {u: i for i, u in enumerate(list1)}
        best, ans = len(list1) + len(list2), []

        for j, v in enumerate(list2):
            i = Aindex.get(v, 1e9)
            if i + j < best:
                best = i + j
                ans = [v]
            elif i + j == best:
                ans.append(v)
        return ans
      
"""
For this problem, we can store the first list item and its index in dictionary. Then, we iterate through list2 and compare if the item is same, then compare again 
if sum of both index is less than or equal the minimum. If yes, then append item to answer.
"""
