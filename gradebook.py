gradebook = [[61, 74, 69, 62, 72, 66, 73, 65, 60, 63, 69, 63, 62, 61, 64, 1],
             [73, 80, 78, 76, 76, 79, 75, 73, 76, 74, 77, 79, 76, 78, 72, 1],
             [90, 92, 93, 92, 88, 93, 90, 95, 100, 99, 100, 91, 95, 99, 96, 1],
             [96, 89, 94, 88, 100, 96, 93, 92, 94, 98, 90, 90, 92, 91, 94, 1],
             [76, 76, 82, 78, 82, 76, 84, 82, 80, 82, 76, 86, 82, 84, 78, 1],
             [93, 92, 89, 84, 91, 86, 84, 90, 95, 86, 88, 95, 88, 84, 89, 1],
             [63, 66, 55, 67, 66, 68, 66, 56, 55, 62, 59, 67, 60, 70, 67, 1],
             [86, 92, 93, 88, 90, 90, 91, 94, 90, 86, 93, 89, 94, 94, 92, 1],
             [89, 80, 81, 89, 86, 86, 85, 80, 79, 90, 83, 85, 90, 79, 80, 1],
             [99, 73, 86, 77, 87, 99, 71, 96, 81, 83, 71, 75, 91, 74, 72, 1]]


def get_average_assignment(gradebook):
    assavg = []
    for x in range(len(gradebook[0])):
        sum = 0
        for list in gradebook:
            sum += list[x]
        assavg.append(sum / 10)
    return assavg

def get_average_student(gradebook):
    stuavg = []
    for x in range(len(gradebook)):
        sumstudent = 0
        for score in gradebook[x]:
            sumstudent += score
        stuavg.append(sumstudent / 15)
    return stuavg


def main():
    assavg = get_average_assignment(gradebook)
    stuavg = get_average_student(gradebook)
    print("Assignment Averages:")
    for x in range(1,(len(gradebook[0])+1)):
        print(f"Assignment {x}: {assavg[x-1]:.2f}")
    print("\n")
    for x in range(1,(len(gradebook)+1)):
        print(f"Student {x}: {stuavg[x-1]:.2f}")



main()
