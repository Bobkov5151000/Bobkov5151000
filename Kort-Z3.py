# Допишите скрипт для расчета средней температуры
# Постарайтесь посчитать количество дней на основе week_temp.
# Так наш скрипт сможет работать c данными за любой период

week_temp = (26, 29, 34, 32, 28, 26, 23)
sum_temp = sum(week_temp)
days = len(week_temp)
mean_temp = sum_temp / days
print(int(mean_temp))
