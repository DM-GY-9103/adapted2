t = 0
num_lines = 100

def setup():
  size(800, 600)
  strokeWeight(2)
  stroke(255)
  frameRate(30)

def draw():
  global t
  global num_lines
  background(0, 20)
  translate(width / 2, height / 2)

  amplitude = width / 8

  for i in range(num_lines):
    x1 = sin((t + i) / 10) * amplitude
    y1 = cos((-t + i) / 10) * amplitude + sin(((t + 1) / 10) * 50)

    x2 = sin((t + i) / 20) * (amplitude * 2) + cos(t + 1) * 10
    y2 = cos((-t + i) / 10) * (amplitude * 2)

    line(x1, y1, x2, y2)

  t += 0.05

def windowResized():
  resizeCanvas(windowWidth, windowHeight)
  background(0)
