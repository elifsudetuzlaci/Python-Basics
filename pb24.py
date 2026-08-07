#Analysis of students grade projects

"""
-reading csv file+
-calculations+
-filtering+
-virtualization of srudents grade
-gatter al of them in class structure of oop 
-false managment

data_set

"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class StudentsGradesAnalysisSystem:
    def __init__(self,fileway):
        self.fileway=fileway
        self.df=None

    def read_data(self):
        try:
            self.df=pd.read_csv(self.fileway)

            if self.df.empty:
                raise ValueError("csv file is empty")


            important_colums={"name","age","department","grade"}


            if not important_colums.issubset(self.df.columns):
                raise ValueError(
                    f"csv file colum couldn't find "
                    f"important colums: {important_colums}"
                )

            self.df["grade"]=pd.to_numeric(self.df["grade"],errors="raise")

            print("reading file is sucseeded")
            print(self.df)
        except FileNotFoundError:
            print(f"error: {self.fileway} couldn't found")
        except pd.errors.EmptyDataError:
            print("csv is empty")
        except ValueError as error:
            print(f"error: {error}")    
        except Exception as e:
            print(f"Unexpected error: {e}")

    def calculatewithnumpy(self):
        try:
            if self.df is None:
                raise ValueError("First load the data")

            grades=self.df["grade"].to_numpy()

            print(f"average {np.mean(grades)}")
            print(f"maximum {np.max(grades)}")
            print(f"minimum {np.min(grades)}")
            print(f"standard deviation {np.std(grades)}")
        except ValueError as error:
            print(f"error {error}")
        except Exception as e:
            print(f"Unexpecpted error .{e}")

    def filtering_with_pandas(self):
        try:
            if self.df is None:
                raise ValueError("First must read data")

            print("results of filtering with pandas")

            high_grades=self.df[self.df["grade"]>80]
            print(f"students who get grade above than 80:\n {high_grades}")

            AI_eng_students=self.df[self.df["department"]=="AI eng"]
            print(f"AI eng Department:\n {AI_eng_students}")

            Older_than=self.df[self.df["age"]>22]
            print(f"these students older than 22:\n {Older_than}")  

        except ValueError as error:
            print(f"error{error}")
        except Exception as e:
            print(f"unexpected situation: {e}")

    def draw_graphics(self):
        try:
            if self.df is None:
                raise ValueError("first data should be read")
            plt.figure(figsize=(10,5))

            plt.bar(self.df["name"],self.df["grade"])
            plt.title("Graphics of students grade ")
            plt.xlabel("students name")
            plt.ylabel("notlar")


            plt.tight_layout()
            plt.show()
        except Exception as e:
                print(f"unexpected situation: {e}")

    def run_all_analysis(self):

        self.read_data()

        if self.df is None:
            print("analysis has stoped!")
            return

        self.calculatewithnumpy()

        self.filtering_with_pandas()
        self.draw_graphics()

if __name__=="__main__":

 fileway="students_notes.csv"
 system=StudentsGradesAnalysisSystem(fileway)

 system.run_all_analysis()