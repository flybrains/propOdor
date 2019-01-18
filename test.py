import gym
env = gym.make('MountainCar-v0')
for i_episode in range(20):
    observation = env.reset()
    for t in range(100):
        env.render()
        print(env.observation_space)
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        if done:
            print("Episode finished after {} timesteps".format(t+1))
            break