import numpy as np
import matplotlib.pyplot as plt

# Kalman filter implementation
def kalman_filter(measurements, initial_state, initial_covariance, process_variance, measurement_variance):
    # Initial state estimate
    x_hat = initial_state

    # Initial covariance estimate
    P = initial_covariance

    # Kalman gain
    K = P / (P + measurement_variance)

    # Lists to store the filtered state estimates and the true states
    filtered_states = []
    true_states = []

    # Kalman filter loop
    for z in measurements:
        # Prediction step
        x_hat_minus = x_hat
        P_minus = P + process_variance

        # Update step
        K = P_minus / (P_minus + measurement_variance)
        x_hat = x_hat_minus + K * (z - x_hat_minus)
        P = (1 - K) * P_minus

        # Save filtered state estimate and true state
        filtered_states.append(x_hat)
        true_states.append(z)

    return np.array(filtered_states), np.array(true_states)

# Generate synthetic data
np.random.seed(42)
true_states = np.linspace(0, 10, 100) + np.random.normal(0, 1, 100)
measurements = true_states + np.random.normal(0, 0.5, 100)

# Kalman filter parameters
initial_state = 0
initial_covariance = 1
process_variance = 0.1
measurement_variance = 0.5

# Apply the Kalman filter
filtered_states, _ = kalman_filter(measurements, initial_state, initial_covariance, process_variance, measurement_variance)

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(true_states, label='True States', marker='o')
plt.plot(measurements, label='Measurements', marker='x')
plt.plot(filtered_states, label='Filtered States', marker='s')
plt.title('Kalman Filter Example')
plt.xlabel('Time Step')
plt.ylabel('Value')
plt.legend()
plt.show()