# A program meant to see whether you passed your driver's license exam or not
# (And if you didn't, man, sitting in the DMV again SUCKS)
correct_answers = ['B', 'D', 'A', 'A', 'C', 'A', 'B', 'A', 'C', 'D', 'B', 'C', \
                   'D', 'A', 'D', 'C', 'C', 'B', 'D', 'A']
def main():
    file = make_file()
    check_file(file)
# A function meant to make a student's answer file
def make_file():
    file = open('student_answers.txt', 'w')
    for i in range(20):
        answer = input("input the student's answer to the test lol ")
        file.write(answer + '\n')
    file.close()
# A function to read, check the answer file, and display the wrong answer
# count
def check_file(file):
    file = open('student_answers.txt', 'r')
    count = 0
    index = 0
    wrong_answer = 0
    wrong_list = []
    for i in file:
        answer = i
        if answer.rstrip('\n') == correct_answers[index]:
            count += 1
            index += 1
        else:
            wrong_list.append(index + 1)
            index += 1
            wrong_answer += 1
    if count >= 15:
        print('Woohoo! You passed the test! Now go die in a car accident.')
        print('Here is the wrong answer count:', wrong_answer)
        print('Here are the numbers of the questions you missed:', wrong_list)
    else:
        print("Aww. You didn't pass. Go kill yourself on a bike.")
        print('Here is the wrong answer count:', wrong_answer)
        print('Here are the numbers of the questions you missed:', wrong_list)
main()
