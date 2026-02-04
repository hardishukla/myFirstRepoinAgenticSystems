# List of student scores
scores = [72, 45, 89, 30, 60]


for score in scores:
    if score < 50:
        print("Fail")
        continue   # skip further processing for failed scores

    print("Pass")
