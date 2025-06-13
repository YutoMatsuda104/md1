traindata = []
current_time = 300

def setup():
    global img
    size(1000, 800)
    img = loadImage("Rline.png")
    image(img, 0, 0, width, height)
    
    import csv
    
    with open("traindata.csv") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        
        for row in reader:
            train_name = row[0]
            time = int(row[1])
            x = int(row[3])
            y = int(row[4])
            
            traindata.append((train_name, time, x, y))
            
def draw():
    global img, traindata, current_time
    image(img, 0, 0, width, height)
    
    for train_name, time, x, y in traindata:
        if time == current_time:
            train_image = loadImage("Rtrain.png")
            image(train_image, x, y, 50, 50)
            
    fill(0)
    textSize(150)
    Atime = "{:02d}:{:02d}".format(current_time // 60, current_time % 60)
    text(Atime, 40, 150)

def keyPressed():
    global current_time
    
    if key == 'n' or key == 'N':
        current_time += 1
    elif key == 'b' or key == 'B':
        current_time -= 1
    elif key == 'j' or key == 'J':
        current_time = getCurrentTime()

def mouseMoved():
    update_time()

def update_time():
    global current_time
    current_time = int(map(mouseX, 0, width, 300, 1500))

def getCurrentTime():
    import datetime
    now = datetime.datetime.now()
    current_hour = now.hour
    current_minute = now.minute
    current_time = current_hour * 60 + current_minute
    return current_time
    text(Atime,40,150)
