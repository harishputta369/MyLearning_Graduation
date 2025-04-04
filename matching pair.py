""""""'''
[9:34 am, 07/12/2021] HARISH: Matching Pair 
Basic Accuracy: 67.23% Submissions: 14182 Points: 1
Given a set of numbers from 1 to N, each number is exactly present twice so there are N pairs. In the worst-case scenario, how many numbers X should be picked and removed from the set until we find a matching pair?

Example 1:

Input:
N = 1
Output:
2
Explanation:
When N=1 Then there is 
one pair and a matching 
pair can be extracted in 
2 Draws.
Example 2:

Input:
N = 2
Output:
3
Explanation:
When N=2 then there are 
2 pairs, let them be {1,2,1,2}
and a matching pair will 
be made in 3 draws.

Your Task:
You don't need to read input or print anything. Your task is to complete the function find() which takes an integer N as input parameter and returns an integer, the number of x must be picked…
[9:34 am, 07/12/2021] HARISH: Second examle lo 3 draws enduku vachhayi
[9:38 am, 07/12/2021] Prem 2: n+1 aa ans
[9:40 am, 07/12/2021] HARISH: Haa
[9:40 am, 07/12/2021] HARISH: Ade undi
[9:40 am, 07/12/2021] HARISH: Discussion lo
[9:40 am, 07/12/2021] HARISH: Kani question ardam
[9:40 am, 07/12/2021] HARISH: Kaledu
[9:40 am, 07/12/2021] HARISH: Naku
[9:41 am, 07/12/2021] Prem 2: Vadu worst case anad
[9:41 am, 07/12/2021] HARISH: Enduku n+1 asalu
[9:41 am, 07/12/2021] Prem 2: So first 1 teeste next 1 malli 1 to n numbers teesake ostadi
[9:42 am, 07/12/2021] HARISH: oh
[9:42 am, 07/12/2021] HARISH: 1 pair ante
[9:42 am, 07/12/2021] HARISH: 1,1 unnay anukundam
[9:42 am, 07/12/2021] HARISH: 1 thisthe 1 e untadi
[9:42 am, 07/12/2021] HARISH: anduke 2 draws
[9:43 am, 07/12/2021] HARISH: 1,2,1,2 unte
[9:43 am, 07/12/2021] HARISH: 1 thisthe 2 thiyali next 1 thiyali
[9:43 am, 07/12/2021] Prem 2: 2 times kada 1,1 teyalante
[9:43 am, 07/12/2021] HARISH: final ga mana chethilo malli 1,1 ane pair vachhindi annatta
"""""""'''
def find(n):
    return n+1
