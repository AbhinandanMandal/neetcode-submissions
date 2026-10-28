class Solution:
    def minOperations(self, logs: List[str]) -> int:
        operations = list()
        for cmd in logs:
            if cmd == '../':
                if operations:
                    operations.pop()
            elif cmd == './':
                continue
            else:
                operations.append(cmd)
        return len(operations)
        