class Batsman:
    def __init__(self, name):
        self.name = name
        self.total_runs = 0
        self.total_matches = 0
        self.total_balls_faced = 0
        self.fifties = 0
        self.hundreds = 0
        self.best_score = 0
        self.match_stats = []

    def add_match_stats(self, runs, balls):
        self.total_runs += runs
        self.total_balls_faced += balls
        self.total_matches += 1
        self.match_stats.append({'match': self.total_matches, 'runs': runs, 'balls': balls})

        if runs >= 50 and runs < 100:
            self.fifties += 1
        elif runs >= 100:
            self.hundreds += 1

        if runs > self.best_score:
            self.best_score = runs

    def calculate_average(self):
        return self.total_runs / self.total_matches if self.total_matches > 0 else 0

    def calculate_strike_rate(self):
        return (self.total_runs / self.total_balls_faced) * 100 if self.total_balls_faced > 0 else 0

    def display_stats(self):
        print(f"Batsman: {self.name}")
        print(f"Total Runs: {self.total_runs}")
        print(f"Total Matches: {self.total_matches}")
        print(f"Average: {self.calculate_average():.2f}")
        print(f"Strike Rate: {self.calculate_strike_rate():.2f}")
        print(f"50s: {self.fifties}")
        print(f"100s: {self.hundreds}")
        print(f"Best Score: {self.best_score}")
        print("Match-by-Match Stats:")
        for match in self.match_stats:
            print(f"Match {match['match']}: Runs {match['runs']}, Balls {match['balls']}")

# Example usage
player = Batsman("Ankit Parwatkar")

# Adding stats for multiple matches
matches = [
    {'runs': 17, 'balls': 14},
    {'runs': 45, 'balls': 29},
    {'runs': 53, 'balls': 37},
    {'runs': 0, 'balls': 4},
    {'runs': 29, 'balls': 17},
    {'runs': 62, 'balls': 38},
    {'runs': 78, 'balls': 42},
    {'runs': 12, 'balls': 8},
    {'runs': 22, 'balls': 18},
    {'runs': 45, 'balls': 31},
    {'runs': 89, 'balls': 55},
    {'runs': 91, 'balls': 47},
    {'runs': 12, 'balls': 10},
    {'runs': 0, 'balls': 2},
    {'runs': 28, 'balls': 20},
    {'runs': 40, 'balls': 22},
    {'runs': 52, 'balls': 28},
    {'runs': 50, 'balls': 26},
    {'runs': 33, 'balls': 15},
    {'runs': 16, 'balls': 14},
    {'runs': 15, 'balls': 9},
    {'runs': 4, 'balls': 8},
    {'runs': 64, 'balls': 40},
    {'runs': 30, 'balls': 18},
    {'runs': 10, 'balls': 8},
    {'runs': 101, 'balls': 49},
    {'runs': 14, 'balls': 8},
    {'runs': 20, 'balls': 16},
    {'runs': 82, 'balls': 56},
    {'runs': 38, 'balls': 26},
    {'runs': 32, 'balls': 24},
    {'runs': 44, 'balls': 40},
    {'runs': 161, 'balls': 57},
    {'runs': 8, 'balls': 16},
    {'runs': 35, 'balls': 29},
    {'runs': 48, 'balls': 36},
    {'runs': 54, 'balls': 30},
    {'runs': 41, 'balls': 29},
    {'runs': 37, 'balls': 29},
    {'runs': 88, 'balls': 52},
    {'runs': 90, 'balls': 54},
    {'runs': 49, 'balls': 31},
    {'runs': 50, 'balls': 44},
    {'runs': 66, 'balls': 42},
    {'runs': 46, 'balls': 38},
    {'runs': 115, 'balls': 70},
    {'runs': 80, 'balls': 32},
    {'runs': 8, 'balls': 12},
    {'runs': 109, 'balls': 55},
    {'runs': 8, 'balls': 22},
    {'runs': 76, 'balls': 44},
    {'runs': 29, 'balls': 11},
    {'runs': 0, 'balls': 6},
    {'runs': 0, 'balls': 2},
    {'runs': 30, 'balls': 24},
    {'runs': 59, 'balls': 37},
    {'runs': 62, 'balls': 46},
    {'runs': 31, 'balls': 29},
    {'runs': 40, 'balls': 32},
    {'runs': 19, 'balls': 15},
    {'runs': 39, 'balls': 17},
    {'runs': 55, 'balls': 17},
    {'runs': 87, 'balls': 53},
    {'runs': 18, 'balls': 12},
    {'runs': 38, 'balls': 26},
    {'runs': 13, 'balls': 17},
    {'runs': 42, 'balls': 28},
    {'runs': 30, 'balls': 22},
    {'runs': 52, 'balls': 38},
    {'runs': 88, 'balls': 44},
    {'runs': 35, 'balls': 20},
    {'runs': 47, 'balls': 31},
    {'runs': 40, 'balls': 24},
    {'runs': 78, 'balls': 54},
    {'runs': 50, 'balls': 46},
    {'runs': 19, 'balls': 13},
    {'runs': 20, 'balls': 8},
    {'runs': 48, 'balls': 16},
    {'runs': 58, 'balls': 44},
    {'runs': 0, 'balls': 4},
    {'runs': 12, 'balls': 16},
    {'runs': 43, 'balls': 33},
    {'runs': 68, 'balls': 32},
    {'runs': 38, 'balls': 26},
    {'runs': 22, 'balls': 20},
    {'runs': 70, 'balls': 28},
    {'runs': 3, 'balls': 6},
    {'runs': 9, 'balls': 12},
    {'runs': 25, 'balls': 17},
    {'runs': 27, 'balls': 18},
    {'runs': 30, 'balls': 30},
    {'runs': 80, 'balls': 32},
    {'runs': 38, 'balls': 26},
    {'runs': 31, 'balls': 25},
    {'runs': 68, 'balls': 40},
    {'runs': 28, 'balls': 26},
    {'runs': 7, 'balls': 11},
    {'runs': 28, 'balls': 26},
    {'runs': 8, 'balls': 6},
    {'runs': 52, 'balls': 26},
    {'runs': 45, 'balls': 29},
]

for match in matches:
    player.add_match_stats(match['runs'], match['balls'])

player.display_stats()
