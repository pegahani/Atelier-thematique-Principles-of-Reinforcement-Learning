# Atelier thématique: Principles of Reinforcement Learning

Université Lumière Lyon 2, 2026 · Pegah Alizadeh (pegah.alizadeh@univ-lyon2.fr)

In this atelier you learn reinforcement learning by building agents: short theory blocks, then you code.
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
| 2 | 3h | Tabular RL: Monte Carlo, TD, SARSA, Q-learning | [`session-2/`](session-2/) |
| 3 | 3h | Function approximation: from Q-learning to DQN | [`session-3/`](session-3/) |
| 4 | 4h | Policy gradient, PPO, RL for LLMs | coming soon |

Session 4 ends with a **LunarLander leaderboard**.
To see where we are going, try the demo agent of Session 1: [`session-1/demo/`](session-1/demo/).

### Session 3 exercises

- **In class:** [`session-3/s3_mountain_car.ipynb`](session-3/s3_mountain_car.ipynb), the only notebook of the session.
  🟢 Core: Parts 1, 2 and 5, then the comparison of Part 4 together. 🟠 Stretch: Part 3.
- **Homework, DQN from scratch:** `homework_pytorch_debug.ipynb` in the folder
  [`week04_approx_rl`](https://github.com/yandexdataschool/Practical_RL/tree/master/week04_approx_rl) of Practical RL.
  Add experience replay and a target network, and solve CartPole.
- **Optional** (Sutton & Barto), at home or if you finish early:
  [`session-3/baird_student.py`](session-3/baird_student.py) (Example 11.1, the deadly triad) and
  [`session-3/mountain_car_exo.py`](session-3/mountain_car_exo.py) (Example 10.1, tile coding).

## Notebooks

Each notebook has three levels: 🟢 **core** (everyone finishes it), 🟠 **stretch** (if you have time) and 🔴 **bonus** (for the curious).
Each `TODO` is followed by a check cell: if it runs without error, you are on the right track.
Solutions are added to the repository after each session.

## Main references

- R. S. Sutton and A. G. Barto, *Reinforcement Learning: An Introduction*, 2nd ed., 2018. Free online: <http://incompleteideas.net/book/the-book-2nd.html>
- D. Silver, UCL course on RL (videos): <https://www.youtube.com/playlist?list=PLqYmG7hTraZDM-OYHWgPebj2MfCFzFObQ>
- Gymnasium documentation: <https://gymnasium.farama.org>

The slides reuse material from David Silver's UCL RL course (CC BY-NC 4.0).
