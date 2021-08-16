questions = open("questions.txt", "r")  # read from questions.txt

question_list = [line.strip() for line in questions]
questions.close()

score = 0
total = len(question_list)

for line in question_list:
    # split equation with `=` into question and answer
    q, a = line.split("=")

    # print question and wait for user to input their answer
    ans = input(f"{q}=")

    if a == ans:
        score += 1

result = open("result.txt", "w")

result.write(f"Your final score is {score}/{total}.")
result.close()