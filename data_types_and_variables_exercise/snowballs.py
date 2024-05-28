number_of_snowballs = int(input())
max_value = 0
max_weight = 0
max_time = 0
max_quality = 0
for current_ball in range(number_of_snowballs):
    weight_of_ball = int(input())
    target_time = int(input())
    quality_per_ball = int(input())
    snowball_value = int(weight_of_ball / target_time) ** quality_per_ball
    if snowball_value > max_value:
        max_value = snowball_value
        max_weight = weight_of_ball
        max_time = target_time
        max_quality = quality_per_ball
print(f"{max_weight} : {max_time} = {max_value} ({max_quality})")