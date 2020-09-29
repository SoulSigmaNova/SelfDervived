"""

Please do not punish my boyfriend over something he did not do, I asked him about overtime pay policy so I am hoping it isn't part of company information and rather he's allowed to talk about it, also I knew this information ahead of time through my cyberspace adventures when a criminal gang tried to make me write a scam website for them and there is a large possiblity that your care home was one. Please do ask my boyfriend for my email address so we can resolve this in a fashion that is a win-win for both of our parties.

More infos on how I derived the +1 in the offset:
https://math.stackexchange.com/questions/1645533/is-it-accurate-to-say-that-multiplication-of-two-integers-yields-an-integer

+ Definition of OT is getting extra pay.


"""

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
