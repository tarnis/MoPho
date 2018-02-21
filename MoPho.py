from flask import Flask
from flask import render_template, request
import RobotCore
import time
app = Flask(__name__, static_url_path='/static')
RC = RobotCore.RobotCore()          # Create a new Robot Core object
RC.Init()                           # Set the board up (checks the board is connected)
RC.ResetEpo()                       # Reset the stop switch (EPO) state
                                    # if you do not have a switch across the two pin header then fit the jumper
# Servo Settings
servoMin = -1.0
servoMax = +1.0
startupDelay = 0.5
stepDelay = 0.1
rateServo1 = 0.01
rateServo2 = 0.01
motorSpeed = 0.0
servoH = 0.0
servoV = 0.0
TurnRight = 0.0
TurnLeft = 0.0

RC.SetServoPosition(1,0)
RC.SetServoPosition(2,0)
print "Done"
a=1
@app.route("/")
def index():
    return render_template('robot.html')
@app.route('/left_side')
def left_side():
    data1="LEFT"
    TurnLeft = TurnLeft + .1
    RC.SetMotor1(motorSpeed)
    RC.SetMotor2(motorSpeed + TurnLeft)
    return 'true'
@app.route('/right_side')
def right_side():
   data1="RIGHT"
   TurnRight = TurnRight + .1
   RC.SetMotor1(motorSpeed + TurnRight)
   RC.SetMotor2(motorSpeed)
   return 'true'
@app.route('/up_side')
def up_side():
   data1="FORWARD"
   motorSpeed = .1
   RC.SetMotors(1)
   return 'true'
   print "Forward"
@app.route('/down_side')
def down_side():
   data1="BACK"
   motorSpeed = motorSpeed - .1
   RC.SetMotors(motorSpeed)
   return 'true'
@app.route('/stop')
def stop():
   data1="STOP"
   motorSpeed = 0
   RC.MotorsOff()
   return  'true'
if __name__ == "__main__":
 print "Start"
 app.run(host='192.168.12.1', port=5010)
