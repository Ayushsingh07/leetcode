class Solution: 
    def pathSum(self, root: TreeNode, targetSum: int) -> list[list[int]]:

        def Count(node:TreeNode)->list[list[int]]:
            if not node:
                return []
            if not node.left and not node.right:
                return [[node.val]]
			   
            return [[node.val]+x for x in Count(node.left) + Count(node.right)]
        
        return [x for x in Count(root) if sum(x) == targetSum]