import EmployeeClass as e
import PayrollDeductionClass as p

def main():
    
    name = 'Jimmy Smith'
    idnumber = '58475'
    depart = 'IT'
    title = 'Developer'
    salary = 6800

    employee = e.Employee(name, idnumber, depart, title, salary)

    print()
    print('Name, ID Number, Department, Job Title, Monthly Salary')
    print(employee.get_name(), ', ', employee.get_id(), ', ', employee.get_department(), ', ' ,employee.get_job(), ', $' , format(employee.get_salary(), ',.2f'), sep='')

    desc1 = 'food court'
    desc2 = 'gift contribution'
    desc3 = 'vending machine'
    date1 = '8/14/2022'
    date2 = '8/12/2022'
    date3 = '8/17/2022'
    date4 = '8/22/2022'
    date5 = '8/5/2022'
    charge1 = 22.50
    charge2 = 25.00
    charge3 = 15.25
    charge4 = 3.00
    charge5 = 2.75
    empid1 = '39119'
    empid2 = '58475'
    empid3 = '21547'

    deduction1 = p.PayrollDeduction(desc1, date1, charge1, empid1)
    deduction2 = p.PayrollDeduction(desc2, date2, charge2, empid2)
    deduction3 = p.PayrollDeduction(desc1, date3, charge3, empid3)
    deduction4 = p.PayrollDeduction(desc3, date4, charge4, empid2)
    deduction5 = p.PayrollDeduction(desc3, date5, charge5, empid2)

    print()
    print('Description, Date, Charge, EmployeeID')
    print(deduction1.get_description(), ', ', deduction1.get_date(), ', ', deduction1.get_charge(), ', ', deduction1.get_empid(), sep='')
    print(deduction2.get_description(), ', ', deduction2.get_date(), ', ', deduction2.get_charge(), ', ', deduction2.get_empid(), sep='')
    print(deduction3.get_description(), ', ', deduction3.get_date(), ', ', deduction3.get_charge(), ', ', deduction3.get_empid(), sep='')
    print(deduction4.get_description(), ', ', deduction4.get_date(), ', ', deduction4.get_charge(), ', ', deduction4.get_empid(), sep='')
    print(deduction5.get_description(), ', ', deduction5.get_date(), ', ', deduction5.get_charge(), ', ', deduction5.get_empid(), sep='')

    print()
    print('*** Employee Pay ***')
    print('Name:', employee.get_name())
    print('ID Numbder:', employee.get_id())
    print('Department:', employee.get_department())
    print('Gross Pay: $', format(employee.get_salary(), ',.2f'), sep='')
    print('Net Pay: $', format(employee.get_salary() - deduction2.get_total_charge(charge2, charge4, charge5), ',.2f'), sep='')
    print()

main()



