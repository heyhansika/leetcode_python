class Solution:
    def combinationSum(self, candidates, target):
        result = []

        def backtrack(start, target, path):
            # Base case
            if target == 0:
                result.append(path[:])
                return
            if target < 0:
                return

            # Try all possibilities
            for i in range(start, len(candidates)):
                # Choose
                path.append(candidates[i])

                # Recur (same index i because repetition allowed)
                backtrack(i, target - candidates[i], path)

                # Backtrack
                path.pop()

        backtrack(0, target, [])
        return result
