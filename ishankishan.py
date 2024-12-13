
import numpy as np
import pandas as pd

# Input data
num_of_balls_played = np.array([25,30,8,41,14,31,20,24,35,9,37,6,15,20,30,28,])
num_of_runs_made = np.array([35,48,5,61,19,42,25,36,50,12,55,10,20,30,45,38])
overs_bowled = np.array([0])
runs_conceded = np.array([0])
wickets_taken = np.array([0])
dismissals = np.array([2,1,0,0,1,1,0,2,1,0,1,0,1,1,2,0])

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


