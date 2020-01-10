from TSsupport import rand

# --- Global constants :

MaxSpeed = 100
Acceleration = 5
# --- Scene 1 constants
# StartPosition = (6600,-8600,280)
# StartRotation = (0,0,-90)
# --- Scene 2 constants
StartPosition = (-7370,-470,280)
StartRotation = (0,0,0)

def ontimestarted():
	global robocar,speed,accel,bam,t,frame,MoveDirection,RotDirection
	doc.ClearOutTxt()
	doc.ActiveTime = 0
	robocar = doc.Object("Robot")
	robocar.DeleteAnim()
	robocar.Position = StartPosition
	robocar.Rotation = StartRotation
	speed, bam, t, frame = 0,0,0,0
	accel = Acceleration
	MoveDirection = 1
	RotDirection = 1
	robocar.SetFrame()
	doc.Draw()

def ontimestopped():
	global robocar
	robocar.SetFrame()
	doc.Draw()

def ontimechanged():
	global robocar,speed,accel,bam,t,frame,MoveDirection,RotDirection
	t = t + 1
	frame = frame + 1
	if frame>1616:
		trueSpace.Stop()
	if speed < MaxSpeed:
		speed = speed + accel
	if bam == 2:
		robocar.Rotate("z", RotDirection*3)
	else:
		robocar.Translate(float(speed)*MoveDirection/1000, 0)
	if not (frame % 4):	# record each fourth frame
		doc.ActiveTime = frame / 4
		robocar.SetFrame()
	if bam !=0:
		if bam == 1:
			if t == 10:
				accel = -accel
			elif t > 20:
				bam = 2
				t = 0
				if rand() < 0.3:
					RotDirection = -RotDirection
		elif bam == 2:
			if t>29:
				bam = 0
				t = 0
				speed = 0
				MoveDirection = -MoveDirection
				accel = -accel
	else:
		fc = robocar.FullCollisionCheck()
		if fc != None:
			bam = 1
			t = 0
			MoveDirection = -MoveDirection
			speed = 0
	doc.Draw()
