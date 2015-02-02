import class_pid


def func(request):
    if request < 0.3:
        respond = 0
    elif request >= 3.0:
        respond = 3.0
    elif request <2.4:
        respond = 0.5 * request ** 2 - 0.207 * request + 0.0171
    else:
        respond = request 
    return respond

pid_control = class_pid.class_pid()

out_speed = 0.0

#set vel to 1.8
pid_control.init(1.8)
out_speed = func(1.8)
print (out_speed)
for i in range(0,5):
    #print(out_speed, pid_control.cal(out_speed), func(pid_control.cal(out_speed))) 
    temp1 = out_speed
    pid_control.cal(temp1)
    temp2 = pid_control.outVel
    temp3 = func(temp2)
    out_speed = temp3 
    print "realSpeed: %.3f  Control: %.3f  Result: %.3f \n" %(temp1, temp2, temp3)

pid_control.init(0.7)
print (out_speed)
for i in range(0,5):
    #print(out_speed, pid_control.cal(out_speed), func(pid_control.cal(out_speed))) 
    temp1 = out_speed
    pid_control.cal(temp1)
    temp2 = pid_control.outVel
    temp3 = func(temp2)
    out_speed = temp3
    print "realSpeed: %.3f  Control: %.3f  Result: %.3f \n" %(temp1, temp2, temp3)


pid_control.init(2.1)
print (out_speed)
for i in range(0,5):
    #print(out_speed, pid_control.cal(out_speed), func(pid_control.cal(out_speed))) 
    temp1 = out_speed
    pid_control.cal(temp1)
    temp2 = pid_control.outVel
    temp3 = func(temp2)
    out_speed = temp3
    print "realSpeed: %.3f  Control: %.3f  Result: %.3f \n" %(temp1, temp2, temp3)


pid_control.init(2.5)
print (out_speed)
for i in range(0,5):
    #print(out_speed, pid_control.cal(out_speed), func(pid_control.cal(out_speed))) 
    temp1 = out_speed
    pid_control.cal(temp1)
    temp2 = pid_control.outVel
    temp3 = func(temp2)
    out_speed = temp3
    print "realSpeed: %.3f  Control: %.3f  Result: %.3f \n" %(temp1, temp2, temp3)

