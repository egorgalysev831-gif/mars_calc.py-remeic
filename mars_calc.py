import time
import os
import random
import msvcrt

# --- ИСХОДНЫЕ ДАННЫЕ ---
money = 50000000000       # Бюджет в $
metal = 500000            # Тонны стали
fuel = 1000000            # Тонны топлива

ships_on_orbit = 0        # Корабли на орбите
tankers_launched = 0      # Запущенные танкеры
people_on_mars = 0        # Население Марса

current_month = 1
current_year = 2026
months_until_window = 26  # Таймер до окна

steel_mills = 1
fuel_plants = 1
launch_pads = 1

while True:
    # 1. АВТОМАТИЧЕСКИЙ ВЫВОД ИНТЕРФЕЙСА
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("=" * 65)
    print(f"🚀 STARSHIP MARS LOGISTICS AI v2.0 (REALISTIC HARDCORE)")
    print(f"📅 Дата: {current_month:02d}.{current_year} г. | До окна на Марс: {months_until_window} мес.")
    print("=" * 65)
    print(f"💰 Бюджет SpaceX: ${money:,.0f}")
    print(f"📦 Склады: {metal:,} т. стали | ⛽ Топливо: {fuel:,} т.")
    print(f"🏭 Инфраструктура: Заводы: {steel_mills} | НПЗ: {fuel_plants} | Космодромы: {launch_pads}")
    print("-" * 65)
    print(f"🛸 Флот на орбите Земли: {ships_on_orbit} / 1000 шт.")
    print(f"🛢️ Прогресс дозаправки танкерами: {tankers_launched} из {ships_on_orbit * 5}")
    print(f"🔴 НАСЕЛЕНИЕ МАРСА: {people_on_mars:,} человек")
    print("=" * 65)
    
    print("\n■ ДОСТУПНЫЕ КОМАНДЫ (Введите номер):")
    print("1. Построить пассажирский Starship (-200т стали, -$50млн)")
    print("2. Запустить танкер для дозаправки (-4600т топлива, -$5млн)")
    print("3. Построить новый стартовый стол (-$1млрд)")
    print("4. Нажать для пропуска месяца (подождать)")
    print("-" * 65)

    # Режим автоматического полета, когда окно открылось
    if months_until_window <= 0:
        print("\n🔥 ВНИМАНИЕ! ОТКРЫЛОСЬ АСТРОНОМИЧЕСКОЕ ОКНО! ЗАПУСК ФЛОТА НА МАРС!")
        
        # Считаем заправленные корабли с правильными отступами
        if ships_on_orbit > 0 and tankers_launched >= (ships_on_orbit * 5):
            ready_to_go = ships_on_orbit
        else:
            ready_to_go = tankers_launched // 5
            if ready_to_go > ships_on_orbit:
                ready_to_go = ships_on_orbit

        if ready_to_go > 0:
            successful_ships = 0
            for _ in range(ready_to_go):
                if random.random() > 0.03:  # 3% шанс аварии
                    successful_ships += 1
            
            new_colonists = successful_ships * 100
            people_on_mars += new_colonists
            
            print(f"✈️ Из {ready_to_go} кораблей до Марса долетели {successful_ships}!")
            print(f"🧑‍🚀 На Марс прибыло +{new_colonists:,} колонистов!")
            
            ships_on_orbit -= ready_to_go
            tankers_launched = 0
        else:
            print("❌ Ни один корабль не был заправлен на орбите. Окно упущено!")
        
        months_until_window = 26  # Сброс таймера
        print("\nНажмите любую клавишу, чтобы продолжить...")
        msvcrt.getch()
        continue

    # ОБРАБОТКА ДЕЙСТВИЙ ИГРОКА
    char = msvcrt.getch()
    try:
        choice = char.decode('utf-8')
    except:
        continue

    if choice == '1':
        if money >= 50000000 and metal >= 200:
            money -= 50000000
            metal -= 200
            ships_on_orbit += 1

    elif choice == '2':
        if fuel >= 4600 and money >= 5000000:
            money -= 5000000
            fuel -= 4600
            tankers_launched += 1

    elif choice == '3':
        if money >= 1000000000:
            money -= 1000000000
            launch_pads += 1

    elif choice == '4':
        current_month += 1
        months_until_window -= 1
        if current_month > 12:
            current_month = 1
            current_year += 1
        
        # Ресурсы капают за пропущенный месяц
        metal += steel_mills * 15000
        fuel += fuel_plants * 80000
