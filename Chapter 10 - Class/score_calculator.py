


class Student():
    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    
    def __init__(self, cls, firstName, lastName, idNumber,):
        self.cls = cls
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    
    def scores(self, scores):
        self.testScores = scores


    def calculate(self):
        total = 0

        for Score in self.testScores:
            total += Score

        avg = total / len(self.testScores)

        if 90 <= avg <= 100:
            return 'A+'
        if 80 <= avg < 90:
            return 'A'
        if 70 <= avg < 80:
            return 'A-'
        if 55 <= avg < 70:
            return 'B+'
        if 40 <= avg < 55:
            return 'B'
        return 'F'



student = Student( 10, 'Ratul', 'Hossain', '18BD0917', [100, 90, 80])
result = student.calculate()
print(result)



student2 = Student(8, 'Rabeya', 'Hossain', '18BD0918', [75, 80, 90])
result = student2.calculate()
print(result)
print(student2.cls)






