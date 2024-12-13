
import numpy as np
import pandas as pd

# Input data
num_of_balls_played = np.array([10,18,5,28,15,10,13,21,17,7,24,6,14,19,25,18])
num_of_runs_made = np.array([15,30,8,45,22,12,18,32,25,10,40,7,22,30,35,28])
overs_bowled = np.array([4,3,2,4,3,4,4,4,4,4,4,3,4,4,3,4])
runs_conceded = np.array([25,20,18,30,28,24,27,35,29,26,34,20,30,22,25,31])
wickets_taken = np.array([1,2,0,1,0,2,1,2,1,0,2,0,1,3,0,2])
dismissals = np.array([1,2,0,1,0,1,0,1,2,1,1,0,1,2,1,1])

# Calculate batting metrics
total_runs = num_of_runs_made.sum()
total_balls = num_of_balls_played.sum()
matches_played = len(num_of_runs_made)

batting_average = total_runs / matches_played
batting_strike_rate = (total_runs / total_balls) * 100

boundary_runs = num_of_runs_made[num_of_runs_made >= 4]  # Assuming boundaries are 4+
boundary_percentage = boundary_runs.sum() / total_runs * 100

# Consistency
distribution_of_scores = num_of_runs_made / total_runs

# Bowling metrics
total_runs_conceded = runs_conceded.sum()
total_overs_bowled = overs_bowled.sum()

bowling_economy = total_runs_conceded / total_overs_bowled
bowling_strike_rate = total_balls / wickets_taken.sum()

# Fielding metrics
total_catches = dismissals.sum()
fielding_contribution = total_catches / matches_played

# Combine fielding stats with bowling contribution
overall_fielding_bowling_contribution = (total_catches + wickets_taken.sum()) / matches_played

# All-Rounder Metrics
all_rounder_index = batting_strike_rate * 0.5 + bowling_economy * 0.3 + wickets_taken.sum() * 0.2
impact_factor = (num_of_runs_made.max() * wickets_taken.max()) / matches_played

# Print metrics
print("\nBatting Metrics")
print(f"Batting Average: {batting_average:.2f}")
print(f"Batting Strike Rate: {batting_strike_rate:.2f}")
print(f"Boundary Percentage: {boundary_percentage:.2f}%")

print("\nBowling Metrics")
print(f"Bowling Economy: {bowling_economy:.2f}")
print(f"Bowling Strike Rate: {bowling_strike_rate:.2f}")

print("\nFielding Metrics")
print(f"Total Catches: {total_catches}")
print(f"Fielding Contribution: {fielding_contribution:.2f}")

print("\nAll-Rounder Metrics")
print(f"All-Rounder Index: {all_rounder_index:.2f}")
print(f"Impact Factor: {impact_factor:.2f}")

# Simulations and Comparative Analysis (examples)
def simulate_extra_over_in_powerplay():
    extra_over_runs = 5  # Hypothetical runs conceded
    wickets_in_extra_over = 1  # Hypothetical wickets

    updated_overs = total_overs_bowled + 1
    updated_runs_conceded = total_runs_conceded + extra_over_runs
    updated_wickets = wickets_taken.sum() + wickets_in_extra_over

    updated_economy = updated_runs_conceded / updated_overs
    updated_strike_rate = total_balls / updated_wickets

    print("\nSimulation: Jadeja bowls an extra over in Powerplay")
    print(f"Updated Economy: {updated_economy:.2f}")
    print(f"Updated Strike Rate: {updated_strike_rate:.2f}")

simulate_extra_over_in_powerplay()


