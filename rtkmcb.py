## @package RtkMCB
#  API library for the RyanTeck motor driver board
"""[rtkmcb]

API library for the RyanTeck motor driver board
"""
import RPi.GPIO as GPIO
import time, signal, atexit

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

M1_A = 17
M1_B = 18

M2_A = 22
M2_B = 23

BASE_FREQ = 5000

class Motor():

	def __init__(self, forward, backward):
		self.pin_forward  = forward
		self.pin_backward = backward
		GPIO.setup(forward, GPIO.OUT,initial = 0)
		GPIO.setup(backward,GPIO.OUT,initial = 0)
		self.pwm_forward  = GPIO.PWM(forward,  BASE_FREQ)
		self.pwm_backward = GPIO.PWM(backward, BASE_FREQ)

	def forwards(self, speed):
		GPIO.output(self.pin_backward,0)
		self.pwm_backward.stop()
		
		if speed == 100:
			self.pwm_forward.stop()
			time.sleep(0.02)
			GPIO.output(self.pin_forward, 1)
		else:
			self.pwm_forward.start(speed)

	def backwards(self, speed):
		GPIO.output(self.pin_forward,0)
		self.pwm_forward.stop()
		
		if speed == 100:
			self.pwm_backward.stop()
			time.sleep(0.02)
			GPIO.output(self.pin_backward, 1)
		else:
			self.pwm_backward.start(speed)

	def stop(self):
		self.pwm_forward.stop()
		self.pwm_backward.stop()
		GPIO.output(self.pin_forward,0)
		GPIO.output(self.pin_backward,0)

	def speed(self, speed):
		if speed >= -100 and speed < 0:
			self.backwards(abs(speed))
		if speed <= 100 and speed > 0:
			self.forwards(speed)
		if speed == 0:
			self.stop()

class MCB():
	def __init__(self):
		self.motor_left  = Motor(M1_A, M1_B)
		self.motor_right = Motor(M2_A, M2_B)

	def speed(self, speed_left, speed_right = None):
		if speed_right == None:
			speed_right = speed_left
		self.motor_left.speed(speed_left)
		self.motor_right.speed(speed_right)

	def stop(self):
		self.motor_left.stop()
		self.motor_right.stop()
	
	def left(self, speed):
		if( speed < 0 ):
			return False
		self.motor_right.speed(speed)
		self.motor_left.speed(-speed)

	def right(self, speed):
		if( speed < 0 ):
			return False
		self.motor_right.speed(-speed)
		self.motor_left.speed(speed)

	def turn(self, speed):
		self.motor_right.speed(-speed)
		self.motor_left.speed(speed)

	def forwards(self, speed):
		self.motor_left.forwards(speed)
		self.motor_right.forwards(speed)

	def backwards(self, speed):
		self.motor_left.backwards(speed)
		self.motor_right.backwards(speed)
	
mcb = MCB()

atexit.register(lambda: GPIO.cleanup())
