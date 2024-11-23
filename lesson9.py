# loops

while True:
    print("hello,loop")
    break  # stop the loop from running



scores = [90, 76, 54, 89, 95, 65, 36, 78, 74, 54,89,90,75,43,67,80,67,57,84,35]
print(scores)
#for each loop
for score in scores:
    if score >= 30 and score <= 70 and score % 2 == 0:
       print(score)