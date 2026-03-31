# Last updated: 3/31/2026, 9:36:36 PM
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet = []
        cars = []
        for i in range(len(position)):
            ti = (target - position[i])/speed[i]
            cars.append((position[i], speed[i], ti))
        cars.sort(key = lambda x: x[0], reverse = True)
        print(cars)
        for i in range(len(cars)):
            if not fleet: 
                fleet.append(cars[i][2])
                continue
            if cars[i][2]>fleet[-1]:
                fleet.append(cars[i][2])
        return len(fleet)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        