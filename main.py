import pandas as pd
import openpyxl
import re

# df = pd.read_csv('C:/Users/family/Desktop/Programming/Bad Actors/Copy of Liberal Arts AHC and Undecided Summer 2023 ENR 2023.05.01.csv')
df = pd.read_csv('C:/Users/family/Desktop/Programming/Bad Actors/Bad_Actors.csv')
pd.set_option('display.max_columns', None)
print(df.dtypes)
df.sort_values(by=['Employee ID'])
# df['Cum Units Passed'] = df['Cum Units Passed'].str.replace(',','').astype(float)
# df['Cum Units Pass'] = df['Cum Units Passed'].astype(float)
df = df[df['Cum Units Passed'] == 0]
df['Cum Units Taken'] = df['Cum Units Taken'].astype(float)
print(df.dtypes)
df = df[df['Cum Units Taken'] > 11]
df = df[df['Major'] != 'Retail Management-AA']
df = df[df['Major'] != 'Retail Management-AB']
df = df[df['Major'] != 'Retail Management-AC']
df = df[df['Major'] != 'Retail Management-CT']
df = df.fillna(0)
df = df[df['Enrollment Drop Date'] == 1]
df.to_excel('Test.xlsx')

df.reset_index(inplace=True)

class ScoreCount:
    score = 0
    def __init__(self, id, df):
        self.id = id
        self.df = df

    def course_total(self):
        student_df = self.df[self.df['Employee ID'] == self.id]
        print(student_df)
        if len(student_df) > 3:
            student_df1 = student_df[student_df['Session Code'] == '6DB']
            if len(student_df1) >= 3:
                ScoreCount.score += 1
                # potential_bad_actors.append(self.id)
            student_df2 = student_df[student_df['Session Code'] == '6S']
            if len(student_df2) >= 3:
                ScoreCount.score += 1
                # potential_bad_actors.append(self.id)
            student_df3 = student_df[student_df['Session Code'] == '6T']
            if len(student_df3) >= 3:
                ScoreCount.score += 1
                # potential_bad_actors.append(self.id)


    def email_address(self):
        student_df = self.df[self.df['Employee ID'] == self.id]
        student_df = student_df.reset_index()
        hotmail = re.search("hotmail", student_df.loc[0, 'Email'])
        yahoo = re.search("yahoo", student_df.loc[0, 'Email'])

        if hotmail or yahoo:
            ScoreCount.score += 1

    def student_age(self):
        student_df = self.df[self.df['Employee ID'] == self.id]
        student_df = student_df.reset_index()
        if student_df.loc[0, 'Current Age'] > 30:
            ScoreCount.score =+ 1
        print('id', self.id, 'score', ScoreCount.score)
        for i in range(len(self.df)):
            if id == self.df.loc[i, 'Employee ID']:
                score_df = self.df.loc[i,'Enrollment Drop Date'] = ScoreCount.score
                return score_df
        # self.df = self.df[self.df['Enrollment Drop Date'] == 'yes']

        # for i in range(len(df)):
        #     if id == df.loc[i, 'Employee ID']:
        #         count = + 1

student_ids = []
potential_bad_actors = []
for i in range(len(df)):
    if df.loc[i,'Employee ID'] not in student_ids:
        student_ids.append(df.loc[i, 'Employee ID'])

for id in student_ids:
    student = ScoreCount(id=id, df=df)
    student.course_total()
    student.email_address()
    score_df = student.student_age()

df.to_excel('Bad_Actors.xlsx')


print(len(student_ids))
print(len(potential_bad_actors))


