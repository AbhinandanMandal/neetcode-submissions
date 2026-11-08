class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for ast in asteroids:
            # Only need to check if the direction of asteroid is left (crazy)
            while stack and ast<0 and stack[-1]>0:
                diff = stack[-1] + ast
                
                # If stack top is smaller than asteroid and remove stack top
                if diff<0:
                    stack.pop()
                # If stack top is larger than asteroid then asteroid finish
                elif diff>0:
                    ast = None
                    break
                else:
                    # if both of same size then both popped
                    stack.pop()
                    ast = None
                    break
            if ast is not None:
                stack.append(ast)
        return stack



