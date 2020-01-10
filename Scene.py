maxspeed = 100
acceleration = 5

def ontimestarted():
	global robocar,speed,accel,direction,bam,t,frame
	doc.ClearOutTxt()
	robocar = doc.Object("Robot")
	robocar.Position = (6600,-8600,280)
	robocar.Rotation = (0,0,-90)
	speed, bam, t, frame = 0,0,0,0
	accel = acceleration
	direction = 1
	doc.ActiveTime = 0
	robocar.DeleteAnim()
	robocar.SetFrame()
	doc.Draw()

def ontimestopped():
	global robocar
	robocar.SetFrame()
	doc.Draw()

def ontimechanged():
	global robocar,speed,accel,direction,bam,t,frame
	t = t + 1
	frame = frame + 1
	if frame>1616:
		trueSpace.Stop()
	if speed < maxspeed:
		speed = speed + accel
	if bam == 2:
		robocar.Rotate("z", 3)
	else:
		robocar.Translate(float(speed)*direction/1000, 0)
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
		elif bam == 2:
			if t>29:
				bam = 0
				t = 0
				speed = 0
				direction = -direction
				accel = -accel
	else:
		fc = robocar.FullCollisionCheck()
		if fc != None:
			bam = 1
			t = 0
			direction = -direction
			speed = 0

	doc.Draw()


