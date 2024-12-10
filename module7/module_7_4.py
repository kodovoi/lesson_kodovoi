# Входные данные
team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2
challenge_result = 'Победа команды Волшебники данных!'

# Использование %
# Переменные: количество участников первой команды (team1_num)
team1_str = "В команде Мастера кода участников: %d !" % team1_num
print(team1_str)

# Переменные: количество участников в обеих командах (team1_num, team2_num)
teams_str = "Итого сегодня в командах участников: %d и %d !" % (team1_num, team2_num)
print(teams_str)

# Использование format()
# Переменные: количество задач решённых командой 2 (score_2)
team2_score_str = "Команда Волшебники данных решила задач: {} !".format(score_2)
print(team2_score_str)

# Переменные: время за которое команда 2 решила задачи (team1_time)
team1_time_str = "Волшебники данных решили задачи за {:.1f} с !".format(team1_time)
print(team1_time_str)

# Использование f-строк
# Переменные: количество решённых задач по командам: score_1, score_2
scores_str = f"Команды решили {score_1} и {score_2} задач."
print(scores_str)

# Переменные: исход соревнования (challenge_result)
challenge_result_str = f"Результат битвы: {challenge_result}"
print(challenge_result_str)

# Переменные: количество задач (tasks_total) и среднее время решения (time_avg)
tasks_total_str = f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!."
print(tasks_total_str)
