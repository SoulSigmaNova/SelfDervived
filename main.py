def calc_overtime(required_hours,worked_hours,hourly_salary,offset=0,factor=0):
    overtime_hours=worked_hours-required_hours
    if (overtime_hours<0):
        return worked_hours*hourly_salary
    else:
        if(offset>0):
            return (required_hours*hourly_salary)+((hourly_salary+offset)*(overtime_hours))
        if (factor>0):
            return (required_hours*hourly_salary)+((hourly_salary*factor)*(overtime_hours))
    return 0

ret=calc_overtime(12,13,10,1)
print(ret)