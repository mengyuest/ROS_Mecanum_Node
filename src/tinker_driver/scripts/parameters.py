class parameters:
    times = 0.0
    scale_from = 0.00
    scale_to = 0.00
    pi = 0.00   
    
    r = 0.00
    rr = 0.00
    lx = 0.00
    ly = 0.00

    send_vel_rate = 0
    send_odom_rate = 0

    proportion = 0
    integral = 0
    derivative = 0
 
    def __init__(self):
        self.times = 1.0        #Twist cmd_vel means [times*meter] per sec
        self.scale_from = 0.005556*2  #receive info(0-1000) to  rad per sec 
        self.scale_to = 940.00*0.33  #meter per sec to operate command(0-1000)
        self.pi = 3.1415926535 
        
        self.r = 0.08           #wheel radius (meters)
        self.rr = 0.01          #wheel roller radius (meters)
        self.lx = 0.25          #semi-dist between wheels in the row(meters)
        self.ly = 0.26          #semi-dist between wheels in the col(meters)

        self.send_vel_rate = 6  #frequency about send vel to base
        self.send_odom_rate = 20 #frequency about send msg to odom topic
        
        self.monitor_rate = 3   #frequency about monitor the twist & odom
        self.proportion = 0.2       #pid parameters ->p
        self.integral = 0.00        #pid parameters ->i
        self.derivative  = 0.00     #pid parameters ->d
        self.decay = 0.4          #pid parameters -> decay rate for integral
        self.threshold = 1.5
        self.wthreshold = 1.5
        
        self.maxV1 = {'Vx': 0.5, 'Vy': 0.3, 'Vz': 1.0}
        self.maxV2 = {'Vx': -0.1, 'Vy': -0.1, 'Vz': -0.1}
        self.minV1 = {'Vx': 0.1, 'Vy': 0.1, 'Vz': 0.1}
        self.minV2 = {'Vx': -0.5, 'Vy': -0.3, 'Vz': -1.0}
        
        self.a1 = {'Vx': 0.5, 'Vy': 0.5, 'Vz': 0.5}
        self.a2 = {'Vx': 0.5, 'Vy': 0.5, 'Vz': 0.5}
        self.b1 = {'Vx': 0.5, 'Vy': 0.5, 'Vz': 0.5}
        self.b2 = {'Vx': 0.5, 'Vy': 0.5, 'Vz': 0.5}

