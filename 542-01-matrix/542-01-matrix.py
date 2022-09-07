class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        m, n = len(mat), len(mat[0])
        num_nonzero = sum(sum(mat[i]) for i in range(m))
        num_zero = m * n - num_nonzero
        
        def algo1():
            zeros = []
            for i in range(m):
                for j in range(n):
                    if mat[i][j] == 0:
                        zeros.append((i,j))


            def metropolis(idx):
                A = [[0]*n for _ in range(m)]
                for i in range(m):
                    for j in range(n):
                        A[i][j] = abs(idx[0] - i) + abs(idx[1] - j)
                return A

            scores = [[100000]*n for _ in range(m)]
            for idx in zeros:
                A = metropolis(idx)
                for i in range(m):
                    for j in range(n):
                        if A[i][j] < scores[i][j]:
                            scores[i][j] = A[i][j]
                            
            return scores
                        
        def algo2():
            scores = [[0]*n for _ in range(m)]
            nonzero_entries = sum(sum(mat[i]) for i in range(m))
            flips = 0
            for idx in range(10000):
                if flips >= nonzero_entries: break
                this_iter_mat = [mat[i][:] for i in range(m)]
                for i in range(m):
                    for j in range(n):

                        if this_iter_mat[i][j] == 0: continue
                        bot =  i < m - 1 and this_iter_mat[i+1][j] == 0
                        top =  i > 0 and this_iter_mat[i-1][j] == 0
                        right = j < n - 1 and this_iter_mat[i][j+1] == 0
                        left = j > 0 and this_iter_mat[i][j-1] == 0

                        if top or bot or right or left:
                            scores[i][j] = idx + 1
                            mat[i][j] = 0
                            flips += 1
                        
            return scores
              
        if num_zero / (m*n) < 0.3:
            return algo1()
        else:
            return algo2()