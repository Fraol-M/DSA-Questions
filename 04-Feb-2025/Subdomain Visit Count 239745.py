# Problem: Subdomain Visit Count - https://leetcode.com/problems/subdomain-visit-count

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        

        visit = []

        total_visit = defaultdict(int)

        for i in range(len(cpdomains)):
            
            num, url = cpdomains[i].split(" ")
            num = int(num)

            level = list(url.split("."))

            domain_name = ""

            for i in range(len(level)-1, -1, -1):
                if domain_name:
                    domain_name=level[i]+ "." +domain_name
                else:
                    domain_name+=level[i]
                
                total_visit[domain_name]+= num
            

        for i, j in total_visit.items():
            visit.append(str(j)+" "+i)  
        return visit

