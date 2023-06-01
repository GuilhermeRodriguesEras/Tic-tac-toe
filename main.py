import pygame

pygame.init()

#scren sizes
screen_width = 500
screen_height = 500

screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('jogo da veia')

#load images
x_img = pygame.image.load('images/x.png').convert_alpha()
o_img = pygame.image.load('images/o.png').convert_alpha()
x_img_scaled = pygame.transform.scale(x_img,(100,100))
o_img_scaled = pygame.transform.scale(o_img,(100,100))

#load font
final_font = pygame.font.Font('font/OpenSans.ttf',70)

#funciton for draw text
def draw_txt(text, font, text_color, x, y):
    img = font.render(text, True, text_color)
    screen.blit(img, (x, y))

#colors
black = (0,0,0)
red = (255,0,0)

#matriz main
Matriz = [['','',''],['','',''],['','','']]

#function drawn
def draw(condiction, text):
    pygame.draw.rect(screen, (255,255,255), pygame.Rect((0,0,500,500)))
    if condiction == False:
        pygame.draw.rect(screen, black, pygame.Rect((164,0,4,500)))
        pygame.draw.rect(screen, black, pygame.Rect((328,0,4,500)))
        pygame.draw.rect(screen, black, pygame.Rect((0,164,500,4)))
        pygame.draw.rect(screen, black, pygame.Rect((0,328,500,4)))

        for i in range(3):
            for j in range(3):
                if Matriz[i][j] == 'x':
                    screen.blit(x_img_scaled,(j*164+j*4 +32,i*164 + i*4 +32))
                elif Matriz[i][j] == 'o':
                    screen.blit(o_img_scaled,(j*164+j*4 +32,i*164 + i*4 +32))
    
    else: 
        draw_txt(str(text), final_font, red, 50, screen_height/2-60)

#see if someone win
def win_condition(M):
    for i in range(3):
        if M[i][0] == M[i][1] and M[i][1] == M[i][2] and M[i][0] != '':
            return True
    for j in range(3):
        if M[0][j] == M[1][j] and M[1][j] == M[2][j] and M[0][j] != '':
            return True
    if M[0][0] == M[1][1] and M[1][1] == M[2][2] and M[0][0] != '':
        return True
    if M[0][2] == M[1][1] and M[1][1] == M[2][0] and M[0][2] != '':
        return True
    return False

#see if game ended without winner
def empate(M):
    for i in range(3):
        for j in range(3):
            if M[i][j] == '':
                return False
    return True

#change player 
def letra_atual(atual):
    if atual == 'x':
        return 'o'
    else:
        return 'x'

letra = 'x'

finished = False
text_final = ''
aux = win_condition(Matriz)

#main loop
run = True
while run:

    draw(finished, text_final)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Get the mouse click position
            mouse_pos = pygame.mouse.get_pos()
            if finished == False:
                if mouse_pos[0] <= 164:
                    aux1 = 0
                elif mouse_pos[0] <=328:
                    aux1 = 1
                else:
                    aux1 = 2
                if mouse_pos[1] <= 164:
                    aux2 = 0
                elif mouse_pos[1] <=328:
                    aux2 = 1
                else:
                    aux2 = 2

                if Matriz[aux2][aux1] == '':
                    Matriz[aux2][aux1] = letra
                    if win_condition(Matriz):
                        finished = True
                        text_final = f'Vitória Do {letra.upper()}'
                        Matriz = [['','',''],['','',''],['','','']]
                        print('vitória do '+ letra)

                    elif empate(Matriz):
                        finished = True
                        text_final = 'Empate :('

                    letra = letra_atual(letra)
            
            else:
                Matriz = [['','',''],['','',''],['','','']]
                finished = False

    pygame.display.update()

pygame.quit()
