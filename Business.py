import random

import time


# Decorative Welcome

print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

print("      🏢  WELCOME TO THE ULTIMATE BUSINESS GAME  🏢")

print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

print("🎯 Objective: Buy properties, collect rent & WIN!")

print("💰 Starting Balance: ₹100000 each (Player & Bot)")

print("🎲 Roll the die to move around 10 famous Indian cities")

print("🏠 Buy properties and earn rent!")

print("⚔️  Face off against the bot. The richest wins!")

print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")


# Instructions

print("\n📜 INSTRUCTIONS:")

print("1️⃣ Roll the die to move on the board (1 to 6).")

print("2️⃣ Land on a city to buy or pay rent.")

print("3️⃣ Chance cards can surprise you—good or bad!")

print("4️⃣ Game ends when both balances are ₹0.")

print("5️⃣ Winner is the one with highest net worth at the end.")

print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")


# Setup

places = {

    "Delhi": 15000, "Mumbai": 18000, "Kolkata": 12000,

    "Chennai": 10000, "Bangalore": 16000, "Hyderabad": 11000,

    "Pune": 14000, "Ahmedabad": 9000, "Jaipur": 7000, "Srinagar": 5000

}


rent = {place: price // 10 for place, price in places.items()}

states = list(places.keys())

player_balance = 100000

bot_balance = 100000

player_pos = 0

bot_pos = 0

player_props = []

bot_props = []

rounds = 0


chance_cards = [

    ("🎁 You found a treasure! Gain ₹5000", 5000),

    ("💸 Lost your wallet! Lose ₹3000", -3000),

    ("💥 Property tax! Lose ₹7000", -7000),

    ("🎉 Bonus salary! Gain ₹10000", 10000),

    ("🚧 Maintenance costs ₹2000", -2000),

    ("🔔 Festival bonus ₹4000", 4000)

]


def draw_die(number):

    faces = {

        1: ["+-------+", "|       |", "|   *   |", "|       |", "+-------+"],

        2: ["+-------+", "| *     |", "|       |", "|     * |", "+-------+"],

        3: ["+-------+", "| *     |", "|   *   |", "|     * |", "+-------+"],

        4: ["+-------+", "| *   * |", "|       |", "| *   * |", "+-------+"],

        5: ["+-------+", "| *   * |", "|   *   |", "| *   * |", "+-------+"],

        6: ["+-------+", "| *   * |", "| *   * |", "| *   * |", "+-------+"],

    }

    for line in faces[number]:

        print("   " + line)


def show_board():

    print("\n🗺️  PROPERTY BOARD")

    for i, place in enumerate(states):

        owner = "🏠 Player" if place in player_props else "🤖 Bot" if place in bot_props else "—"

        print(f"{i+1:>2}. {place:10} | ₹{places[place]:<6} | Owned by: {owner}")

    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")


def show_map():

    map_line = ""

    for i in range(len(states)):

        if i == player_pos and i == bot_pos:

            map_line += "🔁 "  # Both on same tile

        elif i == player_pos:

            map_line += "🧍 "

        elif i == bot_pos:

            map_line += "🤖 "

        else:

            map_line += "⬜ "

    print("\n📍 MAP VIEW")

    print(map_line)

    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")


def get_rent(place): return rent[place]

def get_cost(place): return places[place]


def apply_chance(balance, owner):

    if random.randint(1, 5) == 3:

        card = random.choice(chance_cards)

        print(f"\n🃏 CHANCE CARD: {card[0]}")

        balance += card[1]

        print(f"{owner} new balance: ₹{balance}")

    return balance


# Game Loop

while player_balance > 0 or bot_balance > 0:

    rounds += 1

    print(f"\n🎯 ROUND {rounds}")

    show_board()

    show_map()


    if player_balance > 0:

        input("\n▶️ Your turn! Press Enter to roll the die...")

        roll = random.randint(1, 6)

        print(f"🎲 You rolled: {roll}")

        draw_die(roll)

        player_pos = (player_pos + roll) % len(states)

        place = states[player_pos]

        print(f"➡️ You landed on {place}")


        if place in bot_props:

            rent_amt = get_rent(place)

            player_balance -= rent_amt

            bot_balance += rent_amt

            print(f"⚠️ You paid rent ₹{rent_amt} to bot.")

        elif place not in player_props:

            cost = get_cost(place)

            print(f"🏠 Price: ₹{cost}")

            buy = input("💡 Do you want to buy it? (yes/no): ").lower()

            if buy == "yes" and player_balance >= cost:

                player_props.append(place)

                player_balance -= cost

                print(f"✅ You bought {place}!")

            elif buy == "yes":

                print("❌ Not enough balance.")

            else:

                print("➡️ Skipped buying.")

        else:

            print("🛑 You landed on your own property.")


        player_balance = apply_chance(player_balance, "🧍 Player")


    if bot_balance > 0:

        print("\n🤖 Bot's turn...")

        time.sleep(1)

        roll = random.randint(1, 6)

        print(f"🤖 Bot rolled: {roll}")

        draw_die(roll)

        bot_pos = (bot_pos + roll) % len(states)

        place = states[bot_pos]

        print(f"🤖 Bot landed on {place}")


        if place in player_props:

            rent_amt = get_rent(place)

            bot_balance -= rent_amt

            player_balance += rent_amt

            print(f"💸 Bot paid you ₹{rent_amt} in rent!")

        elif place not in bot_props and bot_balance >= get_cost(place):

            bot_props.append(place)

            bot_balance -= get_cost(place)

            print(f"🤖 Bot bought {place}")

        else:

            print("🤖 Bot skipped buying.")


        bot_balance = apply_chance(bot_balance, "🤖 Bot")


    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

    print(f"🧍 Player Balance: ₹{player_balance}")

    print(f"🤖 Bot Balance   : ₹{bot_balance}")

    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")


    if player_balance <= 0 and bot_balance <= 0:

        break


# Game Over

print("\n🏁 GAME OVER 🏁")

player_worth = player_balance + sum(get_cost(p) for p in player_props)

bot_worth = bot_balance + sum(get_cost(p) for p in bot_props)


print(f"\n📊 Final Net Worth after
