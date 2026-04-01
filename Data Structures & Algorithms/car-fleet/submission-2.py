class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # form an array of pairs each car with speed
        # pos 1 and speed 3 will be [(1,3)]
        pairs = sorted(zip(position, speed), reverse=True)
        stack = []
        for pos, spd in pairs:
            # lets calculate the time of this cars getting to target
            time = (target - pos) / spd
            stack.append(time)
            # if the current car gets before the one in front
            # that means that the car reaches it so now are a fleet and we pop
            # the stack
            if (len(stack)>=2 and stack[-1] <= stack[-2]):
                stack.pop()
        return len(stack)
