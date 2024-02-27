# https://leetcode.com/problems/find-all-people-with-secret/?envType=daily-question&envId=2024-02-24
# 2092. Find All People With Secret
# Attempted
# Hard
# Topics
# Companies
# Hint
# You are given an integer n indicating there are n people numbered from 0 to n - 1. You are also given a 0-indexed 2D integer array meetings where meetings[i] = [xi, yi, timei] indicates that person xi and person yi have a meeting at timei. A person may attend multiple meetings at the same time. Finally, you are given an integer firstPerson.
#
# Person 0 has a secret and initially shares the secret with a person firstPerson at time 0. This secret is then shared every time a meeting takes place with a person that has the secret. More formally, for every meeting, if a person xi has the secret at timei, then they will share the secret with person yi, and vice versa.
#
# The secrets are shared instantaneously. That is, a person may receive the secret and share it with people in other meetings within the same time frame.
#
# Return a list of all the people that have the secret after all the meetings have taken place. You may return the answer in any order.
#
#
#
# Example 1:
#
# Input: n = 6, meetings = [[1,2,5],[2,3,8],[1,5,10]], firstPerson = 1
# Output: [0,1,2,3,5]
# Explanation:
# At time 0, person 0 shares the secret with person 1.
# At time 5, person 1 shares the secret with person 2.
# At time 8, person 2 shares the secret with person 3.
# At time 10, person 1 shares the secret with person 5.
# Thus, people 0, 1, 2, 3, and 5 know the secret after all the meetings.
# Example 2:
#
# Input: n = 4, meetings = [[3,1,3],[1,2,2],[0,3,3]], firstPerson = 3
# Output: [0,1,3]
# Explanation:
# At time 0, person 0 shares the secret with person 3.
# At time 2, neither person 1 nor person 2 know the secret.
# At time 3, person 3 shares the secret with person 0 and person 1.
# Thus, people 0, 1, and 3 know the secret after all the meetings.
# Example 3:
#
# Input: n = 5, meetings = [[3,4,2],[1,2,1],[2,3,1]], firstPerson = 1
# Output: [0,1,2,3,4]
# Explanation:
# At time 0, person 0 shares the secret with person 1.
# At time 1, person 1 shares the secret with person 2, and person 2 shares the secret with person 3.
# Note that person 2 can share the secret at the same time as receiving it.
# At time 2, person 3 shares the secret with person 4.
# Thus, people 0, 1, 2, 3, and 4 know the secret after all the meetings.
#
#
# Constraints:
#
# 2 <= n <= 105
# 1 <= meetings.length <= 105
# meetings[i].length == 3
# 0 <= xi, yi <= n - 1
# xi != yi
# 1 <= timei <= 105
# 1 <= firstPerson <= n - 1

# test case
n = 12
meetings = [[10,8,6],[9,5,11],[0,5,18],[4,5,13],[11,6,17],[0,11,10],[10,11,7],[5,8,3],[7,6,16],[3,6,10],[3,11,1],[8,3,2],[5,0,7],[3,8,20],[11,0,20],[8,3,4],[1,9,4],[10,7,11],[8,10,18]]
firstPerson = 9
expected = [0,1,4,5,6,9,11]

# Visualization graph data
# According to the description, person 0 initially shares the secret with a person "firstPerson" at time 0. Add this sharing to meetings.
meetings.append([0, firstPerson, 0])

# Use graphviz for graph visualization
from graphviz import Graph

def visualizeGraph(n, meetings):
    # Create an undirected graph
    graph = Graph(format='pdf', engine='dot', strict=False)
    graph.attr(directed='false')

    # Add nodes to the graph
    for i in range(n):
        graph.node(str(i))

    # Add edges to the graph with weights
    for x, y, weight in meetings:
        graph.edge(str(x), str(y), label=str(weight))

    # Save the graph visualization as PNG
    graph.render('weighted_graph')

visualizeGraph(n, meetings)
