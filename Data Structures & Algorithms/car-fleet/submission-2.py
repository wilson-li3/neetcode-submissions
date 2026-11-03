class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # taking position - i / speed = the amount of time it will take
        # so we should probably sort by position bc position is limiting factor
        cars = []
        stack = []
        for i in range(len(position)):
            cars.append((position[i], speed[i]))
        cars = sorted(cars)
        for i in range(len(cars) - 1, -1, -1):
            if not stack or (target - cars[i][0]) / cars[i][1] > stack[-1]:
                stack.append((target - cars[i][0]) / cars[i][1])
        return len(stack)

        # 0, 1, 4, 7
        # 1, 2, 2, 1