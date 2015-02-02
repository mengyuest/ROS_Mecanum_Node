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
        self.times = 0.1        #Twist cmd_vel means [times*meter] per sec
        self.scale_from = 0.005556*2  #receive info(0-1000) to  rad per sec 
        self.scale_to = 940.00*0.33  #meter per sec to operate command(0-1000)
        self.pi = 3.1415926535 
        
        self.r = 0.08           #wheel radius (meters)
        self.rr = 0.01          #wheel roller radius (meters)
        self.lx = 0.25          #semi-dist between wheels in the row(meters)
        self.ly = 0.26          #semi-dist between wheels in the col(meters)

        self.send_vel_rate = 6  #frequency about send vel to base
        self.send_odom_rate = 6 #frequency about send msg to odom topic
        
        self.monitor_rate = 3
        self.proportion = 0.2        #pid parameters ->p
        self.integral = 0.000          #pid parameters ->i
        self.derivative  = 0.000         #pid parameters ->d
