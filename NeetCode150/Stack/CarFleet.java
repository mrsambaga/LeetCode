package NeetCode150.Stack;

import java.util.Arrays;

public class CarFleet {
    public int carFleet(int target, int[] position, int[] speed) {
        int[][] cars = new int[position.length][2];
        for (int i = 0; i < position.length; i++) {
            cars[i] = new int[]{position[i], speed[i]};
        }

        Arrays.sort(cars, (a, b) -> Integer.compare(b[0], a[0]));

        int fleet = 0;
        double fleetDuration = 0;

        for (int i = 0; i < position.length; i++) {
            double timeToTarget = (double)(target - cars[i][0]) / cars[i][1];
            if (timeToTarget > fleetDuration) {
                fleet++;
                fleetDuration = timeToTarget;
            }
        }

        return fleet;
    }
}

// In this problem, we need to pair up cars with their position and speed.
// Then we sort the cars by their position in descending order.
// This is because we want to start with the car that is farthest from the target because cars can't catch up to each other.
// We then calculate the time it takes for each car to reach the target.
// If the time it takes for a car to reach the target is greater than the fleet duration, add a new fleet.
// Otherwise, the car is part of the current fleet.
// The time complexity is O(n log n) because we sort the cars by their position, and the rest of the operations are O(n).
// The space complexity is O(n) because we create a new array to store the cars.

