import numpy as np
from src.cost_function import compute_cost
from src.gradient import compute_gradient


def linear_regression(X, y, learning_rate=0.01, max_iterations=1000, tolerance=1e-6, patience=20):
    n_features = X.shape[1]
    weights = np.random.randn(n_features) / np.sqrt(n_features)

    best_cost = float('inf')
    best_weight = weights.copy()
    best_iter = 0
    patience_counter = 0

    for iteration in range(max_iterations):
        current_cost = compute_cost(X=X, y=y, weights=weights)
        if best_cost - current_cost > tolerance:
            best_cost = current_cost
            best_weight = weights
            best_iter = iteration
            patience_counter = 0
        else:
            patience_counter += 1
            if patience_counter == patience:
                print(f"⏹ Early stopping at iteration {iteration}")
                break

        dw = compute_gradient(X, y, weights=weights)
        weights = weights - (learning_rate * dw)

    return best_weight, best_cost, (best_iter + 1)