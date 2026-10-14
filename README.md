# Atelier thématique: Principles of Reinforcement Learning

Université Lumière Lyon 2, 2026 · Pegah Alizadeh (pegah.alizadeh@univ-lyon2.fr)

In this atelier you learn reinforcement learning by building agents: short theory blocks, then you code, in pairs.
There is no exam.

## Before Session 1

1. Get the course files:
   ```bash
   git clone https://github.com/pegahani/Atelier-thematique-Principles-of-Reinforcement-Learning.git
   ```
   (or *Code → Download ZIP* on this page).
2. Set up your Python environment: follow [`setup/README.md`](setup/README.md) and run `setup/check_setup.ipynb`.

Before each session, run `git pull` in the course folder to get the new material.

## Sessions

| Session | Duration | Topic | Material |
|---|---|---|---|
| 1 | 2h | MDPs, Bellman equations, value iteration on FrozenLake | [`session-1/`](session-1/) |
| 2 | 4h | Tabular RL: Monte Carlo, TD, SARSA, Q-learning | coming soon |
| 3 | 4h | Deep RL: DQN from scratch | coming soon |
| 4 | 4h | Policy gradient, PPO, RL for LLMs | coming soon |

Sessions 3 and 4 end with a **LunarLander leaderboard**.

## Notebooks

Each notebook has three levels: 🟢 **core** (everyone finishes it), 🟠 **stretch** (if you have time) and 🔴 **bonus** (for the curious).
Each `TODO` is followed by a check cell: if it runs without error, you are on the right track.
Solutions are added to the repository after each session.

## Main references

- R. S. Sutton and A. G. Barto, *Reinforcement Learning: An Introduction*, 2nd ed., 2018. Free online: <http://incompleteideas.net/book/the-book-2nd.html>
- D. Silver, UCL course on RL (videos): <https://www.youtube.com/playlist?list=PLqYmG7hTraZDM-OYHWgPebj2MfCFzFObQ>
- Gymnasium documentation: <https://gymnasium.farama.org>

The slides reuse material from David Silver's UCL RL course (CC BY-NC 4.0).
