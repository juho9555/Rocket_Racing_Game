# 로켓 레이싱 게임
# 검은 은하에 별을 추가한 배경
# 로켓 1,2 중 누가 먼저 선에 들어오는지 대결하는 게임
import turtle
import random

# === 화면 설정 ===
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("🚀 Rocket Rush 🚀")

screen.tracer(0)  # 별 배경 빠르게 그리기

# === 별 배경 ===
stars = turtle.Turtle()
stars.hideturtle()
stars.penup()

# 별 색상 (빨간색 추가!)
star_colors = ["white", "light yellow", "light blue", "light gray", "cyan", "pink", "red"]

for _ in range(300):  # 별 300개
    x = random.randint(-300, 300)
    y = random.randint(-250, 300)
    stars.goto(x, y)
    stars.color(random.choice(star_colors))
    stars.dot(random.randint(1, 4))

screen.update()
screen.tracer(1)  # 다시 애니메이션 켜기

# === 로켓 1 ===
rocket_one = turtle.Turtle()
rocket_one.shape("arrow")
rocket_one.color("red")
rocket_one.shapesize(3, 1)  # 길쭉한 느낌
rocket_one.penup()
rocket_one.goto(-50, -250)
rocket_one.setheading(90)  # 위쪽으로

# === 로켓 2 ===
rocket_two = rocket_one.clone()
rocket_two.color("cyan")
rocket_two.goto(50, -250)

# === 결승선 ===
goal = turtle.Turtle()
goal.hideturtle()
goal.color("white")
goal.penup()
goal.goto(-200, 200)
goal.pendown()
goal.forward(400)

# === 연기/불꽃 효과 ===
def draw_blast(rocket):
    blast = turtle.Turtle()
    blast.hideturtle()
    blast.speed(0)
    blast.penup()

    colors = ["orange", "red", "yellow"]
    for i in range(5):
        blast.goto(
            rocket.xcor() + random.randint(-10, 10),
            rocket.ycor() - random.randint(20, 40)
        )
        blast.color(random.choice(colors))
        blast.dot(random.randint(5, 10))

    for i in range(2):
        blast.goto(
            rocket.xcor() + random.randint(-15, 15),
            rocket.ycor() - random.randint(40, 60)
        )
        blast.color("gray")
        blast.dot(random.randint(4, 8))

# === 주사위 ===
die = [1, 2, 3, 4, 5, 6]

for _ in range(50):
    if rocket_one.ycor() >= 200:
        print("🚀 Rocket One Wins! 🚀")
        break
    elif rocket_two.ycor() >= 200:
        print("🚀 Rocket Two Wins! 🚀")
        break
    else:
        input("🚀 Rocket One: Press Enter to ignite!")
        outcome = random.choice(die)
        print(f"Rocket One thrust power: {outcome}")
        rocket_one.forward(20 * outcome)
        draw_blast(rocket_one)

        if rocket_one.ycor() >= 200:
            print("🚀 Rocket One Wins! 🚀")
            break

        input("🚀 Rocket Two: Press Enter to ignite!")
        outcome = random.choice(die)
        print(f"Rocket Two thrust power: {outcome}")
        rocket_two.forward(20 * outcome)
        draw_blast(rocket_two)

        if rocket_two.ycor() >= 200:
            print("🚀 Rocket Two Wins! 🚀")
            break

turtle.done()
