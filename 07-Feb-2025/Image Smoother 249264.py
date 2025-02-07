# Problem: Image Smoother - https://leetcode.com/problems/image-smoother/description/

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        

        row = len(img)
        col = len(img[0])


        res = [[0]*col for r in range(row)]
        for r in range(row): 
            for c in range(col):
                cnt = 1
                _sum =  0

                if r-1 >= 0:
                    _sum+=img[r-1][c]
                    cnt+=1
                if r-1 >= 0 and c+1 < col:
                    _sum+=img[r-1][c+1]
                    cnt+=1
                if r-1 >= 0 and c-1 >= 0:
                    _sum+=img[r-1][c-1]
                    cnt+=1
                if c-1 >= 0:
                    _sum+=img[r][c-1]
                    cnt+=1
                if c+1 < col:
                    _sum+=img[r][c+1]
                    cnt+=1
                if r+1 < row and c-1 >= 0:
                    _sum+=img[r+1][c-1]
                    cnt+=1
                if r+1 < row:
                    _sum+=img[r+1][c]
                    cnt+=1
                if r+1 < row and c+1 < col:
                    _sum+=img[r+1][c+1]
                    cnt+=1
               
                _sum+=img[r][c]

                print(_sum,"ind", r, c)
                aveg = _sum // cnt
                res[r][c] = aveg
        
        
        return res



                            
                        
                
                
                        

