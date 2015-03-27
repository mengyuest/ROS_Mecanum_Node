import parameters

class class_pid():
    #error = 0
    sumError = 0
    dError = 0
    prevError = 0
    lastError = 0
    setPoint = 0
    outVel = 0
        
# set the new request of the velocity (should be used when a new command came) 
    def init(self, level):
        self.setPoint = level
        self.para = parameters.parameters()

# calculate the velocity for calibration (should be used in certain freq)
    def cal(self, nextPoint):
        error = self.setPoint - nextPoint
        self.sumError += error
#        print(self.para.decay)
#        self.sumError *= self.para.decay
        self.dError = self.lastError - self.prevError
        self.prevError = self.lastError
        self.lastError = error
#        print("check", "error=", error, " sumError = ", self.sumError, " dError = ", self.dError)
        print "p: %.3f i: %.3f d: %.3f" % ( error, self.sumError, self.dError)
        self.outVel +=  (self.para.proportion * error + self.para.integral * self.sumError + self.para.derivative * self.dError)        
        self.outVel = (self.outVel if(self.outVel < self.para.threshold) else self.para.threshold)
        self.outVel = (self.outVel if(self.outVel > -1*self.para.threshold) else -1 * self.para.threshold)

#        print("outVel = ", self.outVel)
#        print("")
#        print("")
        return self.outVel


#    def class_pid():        
#        self.error = 0
#        self.sumError = 0
#        self.dError = 0
#        self.preError = 0
#        self.lastError = 0
        
