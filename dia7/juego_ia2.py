import random
import pygame

pygame.init()
ancho = 600
alto = 400
ventana = pygame.display.set_mode((ancho, alto))
reloj = pygame.time.Clock()

# Configuración del jugador
size = 15
inicio_x, inicio_y = ancho // 2, alto - 30
x, y = inicio_x, inicio_y
velocidad = 4

# Definir la meta en la parte superior medio
meta = pygame.Rect(ancho // 2 - 40, 0, 80, 25)

# Lista de obstáculos (rectángulos con posición, tamaño y velocidad)
obstaculos = [
    {"rect": pygame.Rect(50, 100, 100, 20), "vel": 3},
    {"rect": pygame.Rect(300, 180, 130, 20), "vel": -4},
    {"rect": pygame.Rect(150, 260, 90, 20), "vel": 5},
]


def cambiar_dificultad():
  for obs in obstaculos:
    # Cambiar ancho de forma aleatoria (entre 60 y 160 píxeles)
    obs["rect"].width = random.randint(60, 160)
    # Incrementar o cambiar velocidad aleatoriamente manteniendo la dirección
    direccion = 1 if obs["vel"] > 0 else -1
    obs["vel"] = random.randint(3, 8) * direccion


corriendo = True
while corriendo:
  for evento in pygame.event.get():
    if evento.type == pygame.QUIT:
      corriendo = False

  # Movimiento con el teclado
  teclas = pygame.key.get_pressed()
  if teclas[pygame.K_RIGHT] and x < ancho - size:
    x += velocidad
  if teclas[pygame.K_LEFT] and x > size:
    x -= velocidad
  if teclas[pygame.K_UP] and y > size:
    y -= velocidad
  if teclas[pygame.K_DOWN] and y < alto - size:
    y += velocidad

  # Crear un rectángulo para la colisión del círculo
  jugador_rect = pygame.Rect(x - size, y - size, size * 2, size * 2)

  # Actualizar y mover obstáculos
  for obs in obstaculos:
    obs["rect"].x += obs["vel"]

    # Rebote en los bordes de la ventana
    if obs["rect"].right >= ancho or obs["rect"].left <= 0:
      obs["vel"] = -obs["vel"]

    # Colisión con obstáculos (vuelve al inicio)
    if jugador_rect.colliderect(obs["rect"]):
      x, y = inicio_x, inicio_y

  # Colisión con la meta (reinicia posición y cambia obstáculos)
  if jugador_rect.colliderect(meta):
    x, y = inicio_x, inicio_y
    cambiar_dificultad()

  # Dibujar elementos en la ventana
  ventana.fill((225, 225, 255))

  # Dibujar meta (color verde)
  pygame.draw.rect(ventana, (40, 180, 40), meta)

  # Dibujar obstáculos (color rojo)
  for obs in obstaculos:
    pygame.draw.rect(ventana, (200, 50, 50), obs["rect"])

  # Dibujar círculo del jugador
  pygame.draw.circle(ventana, (30, 60, 200), (x, y), size)

  pygame.display.flip()
  reloj.tick(60)

pygame.quit()