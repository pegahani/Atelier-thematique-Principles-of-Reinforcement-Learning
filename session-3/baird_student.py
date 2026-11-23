#######################################################################
# Baird's Counterexample (Sutton & Barto, 2nd ed.), Chapter 11
# Goal: observe divergence of off-policy TD(0) with linear function approximation
#
# Part I — Understanding
# Q1. Which components of the "deadly triad" are present here?
#     (bootstrapping, function approximation, off-policy)
# Q2. Why is the true value function well-defined, yet TD(0) can diverge?
#
# Part II — Implement TD(0)
# TODO 1: Implement the feature map x(s) used in Baird's counterexample.
# TODO 2: Implement v_hat(s) = w^T x(s).
# TODO 3: Implement off-policy TD(0) update using samples from behavior policy.
#
# Part III — Experiments
# Q3. Plot ||w|| over time. Does it explode?
# Q4. Try smaller alpha. Does divergence slow down?
# Q5 (optional). Replace TD(0) update with a Monte Carlo-style update. Does it diverge?
#
# Run:
#   python baird_student.py
#######################################################################

import numpy as np
import matplotlib.pyplot as plt

# --- MDP setup (7 states: 6 "upper" + 1 "lower") ---
NUM_STATES = 7
UPPER_STATES = list(range(6))
LOWER_STATE = 6

# Feature dimension in the canonical construction
FEATURE_DIM = 8

# Hyperparameters
GAMMA = 0.99
ALPHA = 0.01
ITERATIONS = 20000
SEED = 0

rng = np.random.default_rng(SEED)


def phi(state: int) -> np.ndarray:
    """
    Feature vector phi(s) for Baird's counterexample.

    Canonical construction (one common version):
      - For upper states i in {0,...,5}:
          phi_i = 2, phi_7 = 1, others 0
      - For lower state:
          phi_7 = 2, others 0

    TODO 1: Implement and return phi(s) as a length-FEATURE_DIM vector.
    """
    x = np.zeros(FEATURE_DIM, dtype=float)

    # TODO 1a: set features for upper states
    # if state in UPPER_STATES:
    #     x[state] = 2.0
    #     x[-1] = 1.0

    # TODO 1b: set features for lower state
    # else:
    #     x[-1] = 2.0

    return x


def v_hat(w: np.ndarray, state: int) -> float:
    """
    Linear value approximation v_hat(s) = w^T phi(s).

    TODO 2: Implement.
    """
    # TODO 2: return float(np.dot(w, phi(state)))
    return 0.0


def sample_behavior_state() -> int:
    """
    Behavior distribution: sample only from the 6 upper states.
    This mimics the off-policy sampling that causes trouble.
    """
    return int(rng.choice(UPPER_STATES))


def next_state_from_behavior(state: int) -> int:
    """
    Transition used in the classic demo:
    from any upper state, transition to the lower state.
    (Reward is always 0 in this counterexample.)
    """
    return LOWER_STATE


def run_offpolicy_td0(alpha: float) -> tuple[np.ndarray, np.ndarray]:
    """
    Runs off-policy TD(0) on Baird's counterexample.
    Returns:
      norms[t] = ||w_t||
      ws[t]    = w_t (for optional deeper analysis)
    """
    # Start with a nonzero weight vector to better visualize divergence
    w = np.ones(FEATURE_DIM, dtype=float)

    norms = np.zeros(ITERATIONS, dtype=float)
    ws = np.zeros((ITERATIONS, FEATURE_DIM), dtype=float)

    for t in range(ITERATIONS):
        s = sample_behavior_state()
        s_next = next_state_from_behavior(s)
        r = 0.0

        # TODO 3a: compute TD error
        # delta = r + GAMMA * v_hat(w, s_next) - v_hat(w, s)

        # TODO 3b: TD(0) update with linear FA (semi-gradient for prediction):
        # w <- w + alpha * delta * phi(s)

        norms[t] = np.linalg.norm(w)
        ws[t, :] = w

    return norms, ws


def main():
    norms, _ = run_offpolicy_td0(ALPHA)

    plt.figure()
    plt.plot(norms)
    plt.xlabel("Iterations")
    plt.ylabel(r"$\|w_t\|_2$")
    plt.title(f"Baird Counterexample: off-policy TD(0), alpha={ALPHA}")
    plt.tight_layout()
    plt.show()

    # Q4 experiment suggestion:
    # try ALPHA in [0.005, 0.001] and compare divergence speed.


if __name__ == "__main__":
    main()