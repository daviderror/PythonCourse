salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
total_needed = 0

for months in range(months):
    if months > 0:
        spend *= (1 + increase)
    deficit = spend - salary
    if deficit > 0:
        total_needed += deficit
    total_needed = round(total_needed)


# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов

print(f"Подушка безопасности, чтобы протянуть {months + 1} месяцев без долгов:", total_needed)
