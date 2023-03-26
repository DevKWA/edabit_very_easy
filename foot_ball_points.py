def foot_ball_points(wins, draws, losses):
    football_points = (wins * 3) + (draws * 1) + (losses * 0)
    return football_points


print(foot_ball_points(3, 4, 2))
print(foot_ball_points(5, 0, 2))
print(foot_ball_points(0, 0, 1))
