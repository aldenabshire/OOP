
class Employee:

    def __init__(self, n, idnum, dep, job, sal):

        self.__name = n
        self.__idnumber = idnum
        self.__department = dep
        self.__jobtitle = job
        self.__salary = sal
    
    def get_name(self):
        return self.__name

    def get_id(self):
        return self.__idnumber

    def get_department(self):
        return self.__department

    def get_job(self):
        return self.__jobtitle

    def get_salary(self):
        return self.__salary
