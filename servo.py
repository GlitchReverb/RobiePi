import RPi.GPIO as GPIO
from time import sleep
servo = [8,10,16,18,3]

GPIO.setmode(GPIO.BOARD)
for i in servo:
	GPIO.setup(i, GPIO.OUT)
tounge=GPIO.PWM(8, 50)
mouth=GPIO.PWM(10, 50)
leftArm=GPIO.PWM(16, 50)
rightArm=GPIO.PWM(18, 50)
test=GPIO.PWM(3, 50)


tounge.start(0)
mouth.start(0)
leftArm.start(0)
rightArm.start(0)
test.start(0)
def setAngle(angle,servo):
	duty = angle / 18 + 2
	if servo == 8:
		GPIO.output(servo, True)
		tounge.ChangeDutyCycle(duty)
		sleep(1)
		GPIO.output(servo, False)
		tounge.ChangeDutyCycle(0)
	elif servo == 10:
		GPIO.output(servo, True)
		mouth.ChangeDutyCycle(duty)
		sleep(1)
		GPIO.output(servo, False)
		mouth.ChangeDutyCycle(0)
	elif servo == 16:
		GPIO.output(servo, True)
		leftArm.ChangeDutyCycle(duty)
		sleep(1)
		GPIO.output(servo, False)
		leftArm.ChangeDutyCycle(0)
	elif servo == 18:
		GPIO.output(servo, True)
		rightArm.ChangeDutyCycle(duty)
		sleep(1)
		GPIO.output(servo, False)
		rightArm.ChangeDutyCycle(0)
	elif servo ==  3:
		GPIO.output(8, True)
		GPIO.output(10, True)
		tounge.ChangeDutyCycle(duty)
		mouth.ChangeDutyCycle(duty)
		sleep(1)
		GPIO.output(8, False)
		GPIO.output(10, False)
		tounge.ChangeDutyCycle(0)
		mouth.ChangeDutyCycle(0)
	return
"""
setAngle(90,8)
setAngle(90,10)
setAngle(90,16)
setAngle(90,18)


setAngle(180,8)
setAngle(180,10)
setAngle(180,16)
setAngle(180,18)


setAngle(90,8)
setAngle(90,10)
setAngle(90,16)
setAngle(90,18)

setAngle(0,3)
setAngle(90,3)
setAngle(180,3)
setAngle(90,3)
"""
setAngle(90,3)
setAngle(180,3)
setAngle(90,3)

tounge.stop()
mouth.stop()
leftArm.stop()
rightArm.stop()
test.stop()
GPIO.cleanup()
