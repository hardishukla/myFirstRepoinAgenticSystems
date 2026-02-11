name = input("Enter name: ")
marks = list(map(float, input("Enter marks of each subject: ").split()))

def greet(name):
    return f"Hello, {name}"

def score(marks):
    total = 0
    for i in marks:
        total += i
    avg = total / len(marks)
    return avg

def pass_or_fail(avg):
    if avg >= 50:
        return "Pass"
    else:
        return "Fail"

def main():
    greeting = greet(name)
    avg = score(marks)
    result = pass_or_fail(avg)

    print(greeting)
    print(f"Subjects: {len(marks)}")
    print(f"Average Score: {avg}")
    print(f"Result: {result}")

main()
