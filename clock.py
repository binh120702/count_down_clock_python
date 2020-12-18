import pygame
from datetime import datetime 

pygame.init()   

screen = pygame.display.set_mode((600,500))
background_color = (166, 245, 187)
button_color = (224, 143, 72)
clock_color = (150,150,150)
time_out = pygame.mixer.Sound("alarm_sound.WAV")

# init variables
circle_center = (300,350)
size_rect = (50, 50)
size_rect_bigger = (150, 50)
text_color = (0,0,0)
counting = False
time_down = int(300)
pre_time = 0
# create button
cor_1 = (100, 50)
cor_2 = (200, 50)
cor_3 = (100, 150)
cor_4 = (200, 150)
cor_5 = (330, 50)
cor_6 = (330, 150)
button_1 = pygame.Rect(cor_1, size_rect)
button_2 = pygame.Rect(cor_2, size_rect)
button_3 = pygame.Rect(cor_3, size_rect)
button_4 = pygame.Rect(cor_4, size_rect)
button_5 = pygame.Rect(cor_5, size_rect_bigger)
button_6 = pygame.Rect(cor_6, size_rect_bigger)

# create text
font = pygame.font.Font('freesansbold.ttf', 50)
font_time = pygame.font.Font('NimbusSanL-BolIta.otf', 60)
text_plus = font.render('+', True, text_color)
text_minus = font.render('-', True, text_color)
text_start = font.render('start', True, text_color)
text_stop = font.render('stop', True, text_color)
text_reset = font.render('reset', True, text_color)

while True:
    screen.fill(background_color)

    # display buttons
    pygame.draw.rect(screen, button_color, button_1)
    pygame.draw.rect(screen, button_color, button_2)
    pygame.draw.rect(screen, button_color, button_3)
    pygame.draw.rect(screen, button_color, button_4)
    pygame.draw.rect(screen, button_color, button_5)
    pygame.draw.rect(screen, button_color, button_6)

    # display texts
    # screen.blit(text_plus, button_1)
    screen.blit(text_plus, (cor_1[0]+10, cor_1[1]))
    screen.blit(text_plus, (cor_2[0]+10, cor_2[1]))
    screen.blit(text_minus, (cor_3[0]+15, cor_3[1]))
    screen.blit(text_minus, (cor_4[0]+15, cor_4[1]))
    screen.blit(text_start, (cor_5[0]+15, cor_5[1]))

    if not counting:
        screen.blit(text_reset, (cor_6[0]+15, cor_6[1]))
    else:
        screen.blit(text_stop, (cor_6[0]+15, cor_6[1]))

    # print time    
    cur_time = datetime.now().strftime("%H:%M:%S")
    cur_time_to_sec = int(cur_time[3:5])*60+ int(cur_time[6:8])
    time_temp = time_down
    if counting:
        time_temp = time_down-cur_time_to_sec+pre_time
    minute = int(time_temp/60)
    second = int(time_temp%60)
    final_time = str(minute)+':'
    if (minute<10):
        final_time = '0'+final_time
    if (second<10): 
        final_time = final_time+'0'
    final_time = final_time + str(second)
    text_time = font_time.render(str(final_time), True, text_color, None)
    screen.blit(text_time, (100,100))
    if time_temp==0 and counting:
        counting = False
        time_out.play()
        import time
        time.sleep(1)
        time_out.stop()
        time_down = 300
        continue

    # display clock
    time_passed = cur_time_to_sec - pre_time

    if counting:
        percent_display = time_passed/time_down
        print(percent_display)
        pygame.draw.rect(screen, (252, 65, 3), (100,300,400*(1-percent_display),50))
    pygame.draw.rect(screen, (0,0,0), (100,300,400,50), 5)

    for event in pygame.event.get():
        # quit game
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)
            x,y = event.pos
            if button_1.collidepoint(x,y) and not counting:
                time_down+=60
            if button_2.collidepoint(x,y) and not counting:
                time_down+=1
            if button_3.collidepoint(x,y) and time_down>=60 and not counting:
                time_down-=60
            if button_4.collidepoint(x,y) and time_down>0 and not counting:
                time_down-=1
            if button_5.collidepoint(x,y) and not counting:
                counting = True
                pre_time = cur_time_to_sec
            if button_6.collidepoint(x,y):
                if counting:
                    counting = False
                time_down = 300
        pass
    pygame.display.flip()
