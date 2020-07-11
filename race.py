from random import randint
import simpy

num_robots = 3
sim_time = 30  # seconds
time_tick = 0.5

class Robot:
    def move(self, env, robot_id):
        pos = 0
        while True:
            pos += randint(1,2)
            print(f"{env.now} r_{robot_id} moved to {pos}")
            yield env.timeout(time_tick)

env = simpy.Environment()

for i in range(num_robots):
    r = Robot()
    env.process(r.move(env, robot_id=i))

env.run(until=sim_time)
