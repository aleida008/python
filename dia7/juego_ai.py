import pygame
import random

pygame.init()

# Tamaño de la ventana
ancho = 600
alto = 400
ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Juego de Obstáculos")

reloj = pygame.time.Clock()

# -----------------------------
# CÍRCULO
# -----------------------------
size = 15
x_inicial = ancho // 2
y_inicial = alto - 30

x = x_inicial
y = y_inicial

velocidad = 5

# -----------------------------
# META
# -----------------------------
meta_ancho = 80
meta_alto = 25

meta_x = (ancho - meta_ancho) // 2
meta_y = 10

# -----------------------------
# OBSTÁCULOS
# -----------------------------
obstaculos = [
    {
        "x": 50,
        "y": 80,
        "ancho": 120,
        "alto": 20,
        "velocidad": 3
    },
    {
        "x": 400,
        "y": 150,
        "ancho": 100,
        "alto": 20,
        "velocidad": -4
    },
    {
        "x": 100,
        "y": 220,
        "ancho": 150,
        "alto": 20,
        "velocidad": 5
    },
    {
        "x": 350,
        "y": 290,
        "ancho": 90,
        "alto": 20,
        "velocidad": -3
    }
]

# -----------------------------
# NIVEL
# -----------------------------
nivel = 1

fuente = pygame.font.Font(None, 30)

corriendo = True

while corriendo:

    # -----------------------------
    # EVENTOS
    # -----------------------------
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    # -----------------------------
    # MOVIMIENTO DEL CÍRCULO
    # -----------------------------
    teclas = pygame.key.get_pressed()

    if teclas[pygame.K_RIGHT]:
        if x < ancho - size:
            x += velocidad

    if teclas[pygame.K_LEFT]:
        if x > size:
            x -= velocidad

    if teclas[pygame.K_UP]:
        if y > size:
            y -= velocidad

    if teclas[pygame.K_DOWN]:
        if y < alto - size:
            y += velocidad

    # -----------------------------
    # MOVIMIENTO DE OBSTÁCULOS
    # -----------------------------
    for obstaculo in obstaculos:

        obstaculo["x"] += obstaculo["velocidad"]

        # Rebote en los bordes
        if obstaculo["x"] <= 0:
            obstaculo["x"] = 0
            obstaculo["velocidad"] *= -1

        if obstaculo["x"] + obstaculo["ancho"] >= ancho:
            obstaculo["x"] = ancho - obstaculo["ancho"]
            obstaculo["velocidad"] *= -1

    # -----------------------------
    # COLISIÓN CON OBSTÁCULOS
    # -----------------------------
    circulo_rect = pygame.Rect(
        x - size,
        y - size,
        size * 2,
        size * 2
    )

    for obstaculo in obstaculos:

        rect = pygame.Rect(
            obstaculo["x"],
            obstaculo["y"],
            obstaculo["ancho"],
            obstaculo["alto"]
        )

        if circulo_rect.colliderect(rect):

            # Volver al inicio
            x = x_inicial
            y = y_inicial

    # -----------------------------
    # COLISIÓN CON LA META
    # -----------------------------
    meta_rect = pygame.Rect(
        meta_x,
        meta_y,
        meta_ancho,
        meta_alto
    )

    if circulo_rect.colliderect(meta_rect):

        # Aumentar nivel
        nivel += 1

        # Volver al inicio
        x = x_inicial
        y = y_inicial

        # Cambiar ancho y velocidad
        for obstaculo in obstaculos:

            # Nuevo ancho aleatorio
            obstaculo["ancho"] = random.randint(60, 160)

            # Nueva velocidad
            velocidad_obstaculo = random.choice(
                [-1, 1]
            ) * random.randint(3 + nivel, 5 + nivel)

            obstaculo["velocidad"] = velocidad_obstaculo

            # Nueva posición horizontal
            obstaculo["x"] = random.randint(
                0,
                ancho - obstaculo["ancho"]
            )

    # -----------------------------
    # DIBUJAR FONDO
    # -----------------------------
    ventana.fill((225, 225, 255))

    # -----------------------------
    # DIBUJAR META
    # -----------------------------
    pygame.draw.rect(
        ventana,
        (30, 180, 70),
        meta_rect
    )

    # -----------------------------
    # DIBUJAR OBSTÁCULOS
    # -----------------------------
    for obstaculo in obstaculos:

        rect = pygame.Rect(
            obstaculo["x"],
            obstaculo["y"],
            obstaculo["ancho"],
            obstaculo["alto"]
        )

        pygame.draw.rect(
            ventana,
            (200, 40, 40),
            rect
        )

    # -----------------------------
    # DIBUJAR CÍRCULO
    # -----------------------------
    pygame.draw.circle(
        ventana,
        (30, 60, 200),
        (x, y),
        size
    )

    # -----------------------------
    # MOSTRAR NIVEL
    # -----------------------------
    texto_nivel = fuente.render(
        "Nivel: " + str(nivel),
        True,
        (0, 0, 0)
    )

    ventana.blit(
        texto_nivel,
        (10, 10)
    )

    # Actualizar pantalla
    pygame.display.flip()

    # 60 FPS
    reloj.tick(60)

pygame.quit()