"""Session 1 demo: a PPO agent learns to land on the Moon (LunarLander).

This is the agent shown at the end of Session 1. It uses the Stable-Baselines3
library: you will implement PPO yourself in Session 4.

Run it from this folder, with the course environment active (setup/README.md):

    python ppo_lunarlander_teaser.py train      # ~15-25 min on a laptop CPU, saves ppo_lunarlander.zip
    python ppo_lunarlander_teaser.py watch      # opens a window with the trained agent

A mean return of 200 or more means the task is solved.
Hyperparameters from RL Baselines3 Zoo (tuned for LunarLander).
"""
import sys

import gymnasium as gym
from stable_baselines3 import PPO
from stable_baselines3.common.env_util import make_vec_env
from stable_baselines3.common.evaluation import evaluate_policy

MODEL_PATH = "ppo_lunarlander"
TOTAL_STEPS = 1_000_000


def train():
    env = make_vec_env("LunarLander-v3", n_envs=16, seed=0)
    model = PPO(
        "MlpPolicy", env,
        n_steps=1024, batch_size=64, n_epochs=4,
        gamma=0.999, gae_lambda=0.98, ent_coef=0.01,
        verbose=1, seed=0, device="cpu",
    )
    model.learn(total_timesteps=TOTAL_STEPS, progress_bar=True)
    model.save(MODEL_PATH)
    mean, std = evaluate_policy(model, gym.make("LunarLander-v3"), n_eval_episodes=20)
    print(f"mean return over 20 episodes: {mean:.1f} +/- {std:.1f}  (200 = solved)")


def watch(n_episodes=5):
    model = PPO.load(MODEL_PATH, device="cpu")
    env = gym.make("LunarLander-v3", render_mode="human")
    for episode in range(n_episodes):
        obs, info = env.reset(seed=episode)
        done, total = False, 0.0
        while not done:
            action, _ = model.predict(obs, deterministic=True)
            obs, reward, terminated, truncated, info = env.step(action)
            total += reward
            done = terminated or truncated
        print(f"episode {episode}: return {total:.1f}")
    env.close()


if __name__ == "__main__":
    {"train": train, "watch": watch}[sys.argv[1] if len(sys.argv) > 1 else "train"]()
