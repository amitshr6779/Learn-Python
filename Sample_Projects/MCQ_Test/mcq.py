from ques import Question

ques_lists = [
    "No. of continets ?\n(a) 6\n(b) 7\n(c) 5\n(d) 9\n\n",
    "Color of Mango ?\n(a) grenn\n(b) yellow\n(c) red\n(d) orange\n\n"
]

questions = [ 
    Question(ques_lists[0], "b"),
    Question(ques_lists[1], "b")
]

def exam_report(exam_questions):
    score = 0
    for ques in exam_questions:
        answers = input(ques.prompt)
        if answers == ques.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(exam_questions)) + " correct")

exam_report(questions)
