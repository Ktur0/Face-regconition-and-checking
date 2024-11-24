import pygame
import cv2
import os
import time
from datetime import datetime
import pyttsx3

pygame.init()
# Time
time_moc = time.time()
time_dem = time.time() 
# Open cv
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
# Khởi tạo bộ nhận diện khuôn mặt Haarcascades
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

check = False

# Other file
def dem_so_luong_file(trong_thu_muc):
    # Lấy danh sách tất cả các file trong thư mục
    files = os.listdir(trong_thu_muc)
    
    # Lọc ra chỉ các file, loại bỏ các thư mục con
    files = [f for f in files if os.path.isfile(os.path.join(trong_thu_muc, f))]
    
    # Đếm số lượng file
    so_luong_file = len(files)
    
    return so_luong_file

duong_dan_thu_muc = "App/Image"

def count_lines_in_file(file_path):
    line_count = 0
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            line_count += 1
    return line_count

# Set screen
x,y = 0,0
screen = pygame.display.set_mode((640,480))
running = True
mouse_box = pygame.Rect(x,y,30,30)
pygame.display.set_caption('Camera')

# Button
folder = pygame.image.load('App/Feature/folder.png')
cameraicon = pygame.image.load('App/Feature/camera.png')
pygame.display.set_icon(cameraicon)
folder_but = pygame.Rect(90,140,175,175)
camera_but = pygame.Rect(365,140,175,175)
circle_but = pygame.Rect(570,220,100,100)
id_frame = pygame.Rect(45,140,450,60)
name_frame = pygame.Rect(45,280,450,60)
con = True

# Menu
menu = True
menu_folder = False
menu_camera = False
font = pygame.font.Font(None,40)
font_thongbao = pygame.font.Font(None,80)
font_thongbao2 = pygame.font.Font(None,55)
text_id = font.render('Your ID is : ',True,('black'))
text_succes = font_thongbao.render('Saving susceeded!',True,('green'))
text_name = font_thongbao2.render('Enter your name and class',True,('black'))
count_click = 1
count_time = 0
text = ''
font_name = pygame.font.Font(None,50)
count_w = 1
done = False
count_time2 = 0
text_identer = font_thongbao.render('Enter your id',True,('black'))
text_nameenter = font_thongbao.render('Enter your initials',True,('black'))
idframe = False
nameframe = False
nameenter = ''
identer = ''
id_text = ''
name_text = ''
name_text1 = ''
bg = True
count_time3 = 0
stt = 1
stt2 = 0
liststt = []
background = pygame.image.load('App/Feature/bg.png')
name = []
vang = 0
check1 = 1
user = []

# Loop
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if menu == True:
        screen.blit(background,(0,0))
        screen.fill((25, 145, 209))
        pygame.draw.rect(screen,('white'),(90,140,175,175))
        pygame.draw.rect(screen,('white'),(365,140,175,175))
        screen.blit(folder,(100,150))
        screen.blit(cameraicon,(353,125))
        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y = pygame.mouse.get_pos()
            mouse_box = pygame.Rect(x,y,30,30)
            if mouse_box.colliderect(folder_but):
                menu_folder = True
                menu = False
                menu_camera = False
                con = True
                count_time = 0
                count_time2 = 0
                count_click = 1
                count_w = 1
                so_luong_file = dem_so_luong_file(duong_dan_thu_muc)
            if mouse_box.colliderect(camera_but):
                menu_folder = False
                menu = False
                menu_camera = True
                count_time = 0
                count_time2 = 0
                count_click = 1
                count_w = 1
                so_luong_file = dem_so_luong_file(duong_dan_thu_muc)
                for i in range(so_luong_file):
                    liststt.append(i)
    
    if menu_folder == True:
        
        # Camera
        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y = pygame.mouse.get_pos()
            mouse_box = pygame.Rect(x,y,30,30)
            if mouse_box.colliderect(circle_but):
                con = False
                time_moc = time.time()
        
        if con == True:
            ret, frame = cap.read()
            cv2.imwrite('App/Image/image'+ str(so_luong_file) + '.png',frame)
            image_mau = pygame.image.load('App/Image/image'+ str(so_luong_file) + '.png')
        
            screen.blit(image_mau,(0,0))
            pygame.draw.circle(screen, 'black', (570,220), 50, width=0)
        else:
            screen.blit(image_mau,(0,0))
            count_click = 1
            if count_time <= 3000:
                screen.blit(text_succes,(50,190))
            elif con == False:
                screen.fill((25, 145, 209))
                screen.blit(text_name,(50,170))
                pygame.draw.rect(screen,('white'),(50,220,530,60))

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            if count_w == 1:
                                with open('App/Text/Name.txt','a') as file:
                                    file.write('\n')
                                    file.write(text)
                                count_w = 0
                            text = ""
                            done = True
                        elif event.key == pygame.K_BACKSPACE:
                            text = text[:-1]
                        else:
                            text += event.unicode
                text_surface = font.render(text, True, (0, 0, 0))
                screen.blit(text_surface, (60, 235))

            if done == True:
                if count_time2 <= 3000:
                    screen.fill((25, 145, 209))
                    screen.blit(text_succes,(50,190))  
                else:
                    menu = True
                    menu_folder = False
                    menu_camera = False
                    con = True
                    done = False
                count_time2 += 1      
            count_time += 1
    
    if menu_camera == True:
        so_luong_file = dem_so_luong_file(duong_dan_thu_muc)
        if check1 == 1:
            vang = count_lines_in_file('App/Text/Name.txt') - 1
            thoi_gian_thuc3 = datetime.now()
            with open("App/Text/Missing.txt","a",) as file:
                file.write('\n')
                file.write(str(thoi_gian_thuc3) + ' : ' + str(vang))
            
            check1 -= 1
        if bg == True:
            ret,frame = cap.read()

            cv2.imwrite('App/Image/image.png',frame)

            image_mau = pygame.image.load('App/Image/image.png')
            screen.blit(image_mau,(0,0))

            if stt < so_luong_file:
                img1 = cv2.imread('App/Image/image'+ str(stt) + '.png')
            else:
                stt = 1
                img1 = cv2.imread('App/Image/image'+ str(stt) + '.png')
            img2 = cv2.imread('App/Image/image.png')

            gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
            gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

            # Nhận diện khuôn mặt trên ảnh 1
            faces1 = face_cascade.detectMultiScale(gray1, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

            # Nhận diện khuôn mặt trên ảnh 2
            faces2 = face_cascade.detectMultiScale(gray2, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

            if len(faces1) > 0 and len(faces2) > 0:
                x1, y1, w1, h1 = faces1[0]
                x2, y2, w2, h2 = faces2[0]

                # Cắt ảnh để lấy khuôn mặt
                face1 = gray1[y1:y1+h1, x1:x1+w1]
                face2 = gray2[y2:y2+h2, x2:x2+w2]

                # Tính giá trị tuyệt đối của sự chênh lệch giữa hai khuôn mặt
                face1 = cv2.resize(face1,(100,100))
                face2 = cv2.resize(face2,(100,100))
                    
                diff = cv2.absdiff(face1, face2)

                # Ngưỡng để tạo ảnh nhị phân
                _, threshold = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)

                count = cv2.countNonZero(threshold)
            
                if stt in liststt:
                    if count <= 3500:
                        bg = False
                        stt2 = stt
                        liststt.remove(stt)

            stt += 1

        if bg == False:
            screen.fill((25, 145, 209))
            with open('App/Text/Name.txt','r') as file:
                lines = file.readlines()
                name_text = lines[stt2]
                name.append(name_text)
                for i in range(13):
                    xet = name_text.find('10A'+ str(i+1))
                    if xet != -1:
                        khoi10 = True
                        tenlop = '10A' + str(i+1)
                    else:
                        khoi10 = False
                    xet = name_text.find('11A'+ str(i+1))
                    if xet != -1:
                        khoi11 = True
                        tenlop = '11A' + str(i+1)
                    else:
                        khoi11 = False
                    xet = name_text.find('12A'+ str(i+1))
                    if xet != -1:
                        khoi12 = True
                        tenlop = '12A' + str(i+1)
                    else:
                        khoi12 = False
            text_newsfox = font_thongbao.render('Welcome !',True,('green'))

            if count_time3 <= 180:
                screen.blit(text_newsfox,(180,210))
            else:
                a = "Welcome to class"
                engine = pyttsx3.init()
                engine.say(a)
                engine.runAndWait()
                # Lấy thời gian thực
                thoi_gian_thuc = datetime.now()
                thoi_gian_thuc2 = thoi_gian_thuc.strftime("%Y-%m-%d %H:%M:%S")

                # Định dạng thời gian theo ý muốn
                thoi_gian_dinh_dang = thoi_gian_thuc.strftime("%H")

                if (int(thoi_gian_dinh_dang) >= 7):
                    vang -= 1
                    thoi_gian_thuc3 = datetime.now()
                    with open("App/Classes/Missing.txt","a") as file:
                        file.write('\n')
                        file.write(str(thoi_gian_thuc3) + ' : ' + str(vang))
                        with open('App/Text/Name.txt','r') as file1:
                            lines = file1.readlines()
                            for i in range(1,len(lines)):
                                name_text1 = lines[i]
                                if name_text1 in name:
                                    pass
                                else:
                                    file.write('\n')
                                    file.write(name_text1)
                    a = "You are late. Hungry up"
                    engine = pyttsx3.init()
                    engine.say(a)
                    engine.runAndWait()
                    if stt2 + 1 < so_luong_file: 
                        with open('App/Classes/'+ tenlop +'.txt','a') as file:
                            # file.write('\n')
                            file.write(name_text)
                            file.write( thoi_gian_thuc2)
                            file.write(' (lated)')
                            name.append(name_text)
                    elif stt2 + 1 == so_luong_file:
                        with open('App/Classes/'+ tenlop +'.txt','a') as file:
                            file.write('\n')
                            file.write(name_text)
                            file.write('\n')
                            file.write( thoi_gian_thuc2)
                            file.write(' (lated)')
                            name.append(name_text)
                else:
                    vang -= 1
                    thoi_gian_thuc3 = datetime.now()
                    with open("App/Classes/Missing.txt","a") as file:
                        file.write('\n')
                        file.write(str(thoi_gian_thuc3) + ' : ' + str(vang))
                    if stt2 + 1 < so_luong_file:
                        with open('App/Classes/'+ tenlop +'.txt','a') as file:
                            file.write('\n')
                            file.write(name_text )
                            file.write(thoi_gian_thuc2)
                            file.write(' (on time)')
                    elif stt2 + 1 == so_luong_file:
                        with open('App/Classes/'+ tenlop +'.txt','a') as file:
                            file.write('\n')
                            file.write(name_text )
                            file.write('\n')
                            file.write(thoi_gian_thuc2)
                            file.write(' (on time)')

                bg = True

                name_text = ''
                count_time3 = 0
                
            count_time3 += 1
                

    pygame.display.update()