import pygame
import random
import numpy as np
import pygame_gui
from pygame_gui.elements import UIHorizontalSlider as UISlider
from pygame_gui.elements import UILabel as UILabel
from numba import jit

particles = []
window_size = 1000
pygame.init()
window = pygame.display.set_mode((window_size, window_size))
manager = pygame_gui.UIManager((window_size, window_size))
pygame.display.set_caption("Particle Sim")

sliders_and_labels = []

# Create sliders and labels for interaction rules
#RED
slider_red_red = UISlider(start_value=.6, value_range=(-1, 1), relative_rect=pygame.Rect(10, 20, 200, 20), manager=manager)
label_red_red = UILabel(pygame.Rect(180, 20, 100, 20), "R-R", manager)
sliders_and_labels.extend([slider_red_red, label_red_red])

slider_red_green = UISlider(start_value=.6, value_range=(-1, 1), relative_rect=pygame.Rect(10, 40, 200, 20), manager=manager)
label_red_green = UILabel(pygame.Rect(180, 40, 100, 20), "R-G", manager)
sliders_and_labels.extend([slider_red_green, label_red_green])

slider_red_blue = UISlider(start_value=.6, value_range=(-1, 1), relative_rect=pygame.Rect(10, 60, 200, 20), manager=manager)
label_red_blue = UILabel(pygame.Rect(180, 60, 100, 20), "R-B", manager)
sliders_and_labels.extend([slider_red_blue, label_red_blue])

slider_red_yellow = UISlider(start_value=.6, value_range=(-1, 1), relative_rect=pygame.Rect(10, 80, 200, 20), manager=manager)
label_red_yellow = UILabel(pygame.Rect(180, 80, 100, 20), "R-Y", manager)
sliders_and_labels.extend([slider_red_yellow, label_red_yellow])

#GREEN
slider_green_red = UISlider(start_value=.6, value_range=(-1, 1), relative_rect=pygame.Rect(10, 120, 200, 20), manager=manager)
label_green_red = UILabel(pygame.Rect(180, 120, 100, 20), "G-R", manager)
sliders_and_labels.extend([slider_green_red, label_green_red])

slider_green_green = UISlider(start_value=.6, value_range=(-1, 1), relative_rect=pygame.Rect(10, 140, 200, 20), manager=manager)
label_green_green = UILabel(pygame.Rect(180, 140, 100, 20), "G-G", manager)
sliders_and_labels.extend([slider_green_green, label_green_green])

slider_green_blue = UISlider(start_value=.6, value_range=(-1, 1), relative_rect=pygame.Rect(10, 160, 200, 20), manager=manager)
label_green_blue = UILabel(pygame.Rect(180, 160, 100, 20), "G-B", manager)
sliders_and_labels.extend([slider_green_blue, label_green_blue])

slider_green_yellow = UISlider(start_value=.6, value_range=(-1, 1), relative_rect=pygame.Rect(10, 180, 200, 20), manager=manager)
label_green_yellow = UILabel(pygame.Rect(180, 180, 100, 20), "G-Y", manager)
sliders_and_labels.extend([slider_green_yellow, label_green_yellow])

#BLUE
slider_blue_red = UISlider(start_value=.6, value_range=(-1, 1), relative_rect=pygame.Rect(10, 220, 200, 20), manager=manager)
label_blue_red = UILabel(pygame.Rect(180, 220, 100, 20), "B-R", manager)
sliders_and_labels.extend([slider_blue_red, label_blue_red])

slider_blue_green = UISlider(start_value=.6, value_range=(-1, 1), relative_rect=pygame.Rect(10, 240, 200, 20), manager=manager)
label_blue_green = UILabel(pygame.Rect(180, 240, 100, 20), "B-G", manager)
sliders_and_labels.extend([slider_blue_green, label_blue_green])

slider_blue_blue = UISlider(start_value=.6, value_range=(-1, 1), relative_rect=pygame.Rect(10, 260, 200, 20), manager=manager)
label_blue_blue = UILabel(pygame.Rect(180, 260, 100, 20), "B-B", manager)
sliders_and_labels.extend([slider_blue_blue, label_blue_blue])

slider_blue_yellow = UISlider(start_value=.6, value_range=(-1, 1), relative_rect=pygame.Rect(10, 280, 200, 20), manager=manager)
label_blue_yellow = UILabel(pygame.Rect(180, 280, 100, 20), "B-Y", manager)
sliders_and_labels.extend([slider_blue_yellow, label_blue_yellow])

#YELLOW
slider_yellow_red = UISlider(start_value=.6, value_range=(-1, 1), relative_rect=pygame.Rect(10, 320, 200, 20), manager=manager)
label_yellow_red = UILabel(pygame.Rect(180, 320, 100, 20), "Y-R", manager)
sliders_and_labels.extend([slider_yellow_red, label_yellow_red])

slider_yellow_green = UISlider(start_value=.6, value_range=(-1, 1), relative_rect=pygame.Rect(10, 340, 200, 20), manager=manager)
label_yellow_green = UILabel(pygame.Rect(180, 340, 100, 20), "Y-G", manager)
sliders_and_labels.extend([slider_yellow_green, label_yellow_green])

slider_yellow_blue = UISlider(start_value=.6, value_range=(-1, 1), relative_rect=pygame.Rect(10, 360, 200, 20), manager=manager)
label_yellow_blue = UILabel(pygame.Rect(180, 360, 100, 20), "Y-B", manager)
sliders_and_labels.extend([slider_yellow_blue, label_yellow_blue])

slider_yellow_yellow = UISlider(start_value=.6, value_range=(-1, 1), relative_rect=pygame.Rect(10, 380, 200, 20), manager=manager)
label_yellow_yellow = UILabel(pygame.Rect(180, 380, 100, 20), "Y-Y", manager)
sliders_and_labels.extend([slider_yellow_yellow, label_yellow_yellow])

#VELOCITY
slider_velocity = UISlider(start_value=.1, value_range=(.1, 1), relative_rect=pygame.Rect(10, 420, 200, 20), manager=manager)
label_velocity = UILabel(pygame.Rect(180, 420, 100, 20), "V", manager)
sliders_and_labels.extend([slider_velocity, label_velocity])

# Create labels to show the current slider values
label_red_red_value = UILabel(pygame.Rect(200, 20, 150, 20), f"{slider_red_red.get_current_value():.2f}", manager)
label_red_green_value = UILabel(pygame.Rect(200, 40, 150, 20), f"{slider_red_green.get_current_value():.2f}", manager)
label_red_blue_value = UILabel(pygame.Rect(200, 60, 150, 20), f"{slider_red_blue.get_current_value():.2f}", manager)
label_red_yellow_value = UILabel(pygame.Rect(200, 80, 150, 20), f"{slider_red_yellow.get_current_value():.2f}", manager)
label_green_red_value = UILabel(pygame.Rect(200, 120, 150, 20), f"{slider_green_red.get_current_value():.2f}", manager)
label_green_green_value = UILabel(pygame.Rect(200, 140, 150, 20), f"{slider_green_green.get_current_value():.2f}", manager)
label_green_blue_value = UILabel(pygame.Rect(200, 160, 150, 20), f"{slider_green_blue.get_current_value():.2f}", manager)
label_green_yellow_value = UILabel(pygame.Rect(200, 180, 150, 20), f"{slider_green_yellow.get_current_value():.2f}", manager)
label_blue_red_value = UILabel(pygame.Rect(200, 220, 150, 20), f"{slider_blue_red.get_current_value():.2f}", manager)
label_blue_green_value = UILabel(pygame.Rect(200, 240, 150, 20), f"{slider_blue_green.get_current_value():.2f}", manager)
label_blue_blue_value = UILabel(pygame.Rect(200, 260, 150, 20), f"{slider_blue_blue.get_current_value():.2f}", manager)
label_blue_yellow_value = UILabel(pygame.Rect(200, 280, 150, 20), f"{slider_blue_yellow.get_current_value():.2f}", manager)
label_yellow_red_value = UILabel(pygame.Rect(200, 320, 150, 20), f"{slider_yellow_red.get_current_value():.2f}", manager)
label_yellow_green_value = UILabel(pygame.Rect(200, 340, 150, 20), f"{slider_yellow_green.get_current_value():.2f}", manager)
label_yellow_blue_value = UILabel(pygame.Rect(200, 360, 150, 20), f"{slider_yellow_blue.get_current_value():.2f}", manager)
label_yellow_yellow_value = UILabel(pygame.Rect(200, 380, 150, 20), f"{slider_yellow_yellow.get_current_value():.2f}", manager)
label_velocity_value = UILabel(pygame.Rect(200, 420, 150, 20), f"{slider_velocity.get_current_value():.2f}", manager)

sliders_and_labels.extend([label_red_red_value, label_red_green_value, label_red_blue_value, label_red_yellow_value,
    label_green_red_value, label_green_green_value, label_green_blue_value, label_green_yellow_value,
    label_blue_red_value, label_blue_green_value, label_blue_blue_value, label_blue_yellow_value,
    label_yellow_red_value, label_yellow_green_value, label_yellow_blue_value, label_yellow_yellow_value, label_velocity_value])

#velocity_value = slider_velocity.get_current_value()

def toggle_visibility(elements, visible):
    for element in elements:
        if visible:
            element.show()
        else:
            element.hide()

def draw(surface, x, y, color, size):
    pygame.draw.circle(surface, color, (x, y), 1)

def particle(x, y, c):
    return {"x": x, "y": y, "vx": 0, "vy": 0, "color": c}

def randomxy():
    return round(random.random() * window_size + 1)

def create(number, color):
    group = np.empty((number,), dtype=[("x", np.float64), ("y", np.float64), ("vx", np.float64), ("vy", np.float64), ("color", np.unicode_, 10)])
    for i in range(number):
        group[i]["x"] = randomxy()
        group[i]["y"] = randomxy()
        group[i]["vx"] = 0
        group[i]["vy"] = 0
        group[i]["color"] = color
        particles.append(group[i])
    return group

@jit(nopython=True)
def rule(particles1, particles2, g, velocity):
    for i in range(len(particles1)):
        fx = 0
        fy = 0
        a = particles1[i]
        for j in range(len(particles2)):
            b = particles2[j]
            dx = a["x"] - b["x"]
            dy = a["y"] - b["y"]
            d = (dx*dx + dy*dy)**0.5
            if d > 0 and d < 80:
                F = g/d
                fx += F*dx
                fy += F*dy
        a["vx"] = (a["vx"] + fx)*velocity
        a["vy"] = (a["vy"] + fy)*velocity
        a["x"] += a["vx"]
        a["y"] += a["vy"]
        if a["x"] <= 0:
            a["x"] = 0
            a["vx"] *= -1
        elif a["x"] >= window_size:
            a["x"] = window_size
            a["vx"] *= -1
        if a["y"] <= 0:
            a["y"] = 0
            a["vy"] *= -1
        elif a["y"] >= window_size:
            a["y"] = window_size
            a["vy"] *= -1

red = create(1000, "red")
green = create(1000, "green")
blue = create(1000, "blue")
yellow = create(1000, "yellow")

run = True
clock = pygame.time.Clock()

sliders_and_labels_visible = True

while run:
    time_delta = clock.tick(60) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_h:
                sliders_and_labels_visible = not sliders_and_labels_visible
                toggle_visibility(sliders_and_labels, sliders_and_labels_visible)

        manager.process_events(event)

    manager.update(time_delta)

    window.fill(0)
    
    #velocity_value = slider_velocity.get_current_value()

    rule(red, red, slider_red_red.get_current_value(), slider_velocity.get_current_value())
    rule(red, green, slider_red_green.get_current_value(), slider_velocity.get_current_value())
    rule(red, blue, slider_red_blue.get_current_value(), slider_velocity.get_current_value())
    rule(red, yellow, slider_red_yellow.get_current_value(), slider_velocity.get_current_value())
    
    rule(green, red, slider_green_red.get_current_value(), slider_velocity.get_current_value())
    rule(green, green, slider_green_green.get_current_value(), slider_velocity.get_current_value())
    rule(green, blue, slider_green_blue.get_current_value(), slider_velocity.get_current_value())
    rule(green, yellow, slider_green_yellow.get_current_value(), slider_velocity.get_current_value())
    
    rule(blue, red, slider_blue_red.get_current_value(), slider_velocity.get_current_value())
    rule(blue, green, slider_blue_green.get_current_value(), slider_velocity.get_current_value())
    rule(blue, blue, slider_blue_blue.get_current_value(), slider_velocity.get_current_value())
    rule(blue, yellow, slider_blue_yellow.get_current_value(), slider_velocity.get_current_value())

    rule(yellow, red, slider_yellow_red.get_current_value(), slider_velocity.get_current_value())
    rule(yellow, green, slider_yellow_green.get_current_value(), slider_velocity.get_current_value())
    rule(yellow, blue, slider_yellow_blue.get_current_value(), slider_velocity.get_current_value())
    rule(yellow, yellow, slider_yellow_yellow.get_current_value(), slider_velocity.get_current_value())
    
    # Update slider value labels
    label_red_red_value.set_text(str("{:.2f}".format(slider_red_red.get_current_value())))
    label_red_green_value.set_text(str("{:.2f}".format(slider_red_green.get_current_value())))
    label_red_blue_value.set_text(str("{:.2f}".format(slider_red_blue.get_current_value())))
    label_red_yellow_value.set_text(str("{:.2f}".format(slider_red_yellow.get_current_value())))
    
    label_green_red_value.set_text(str("{:.2f}".format(slider_green_red.get_current_value())))
    label_green_green_value.set_text(str("{:.2f}".format(slider_green_green.get_current_value())))
    label_green_blue_value.set_text(str("{:.2f}".format(slider_green_blue.get_current_value())))
    label_green_yellow_value.set_text(str("{:.2f}".format(slider_green_yellow.get_current_value())))
    
    label_blue_red_value.set_text(str("{:.2f}".format(slider_blue_red.get_current_value())))
    label_blue_green_value.set_text(str("{:.2f}".format(slider_blue_green.get_current_value())))
    label_blue_blue_value.set_text(str("{:.2f}".format(slider_blue_blue.get_current_value())))
    label_blue_yellow_value.set_text(str("{:.2f}".format(slider_blue_yellow.get_current_value())))
    
    label_yellow_red_value.set_text(str("{:.2f}".format(slider_yellow_red.get_current_value())))
    label_yellow_green_value.set_text(str("{:.2f}".format(slider_yellow_green.get_current_value())))
    label_yellow_blue_value.set_text(str("{:.2f}".format(slider_yellow_blue.get_current_value())))
    label_yellow_yellow_value.set_text(str("{:.2f}".format(slider_yellow_yellow.get_current_value())))
    
    label_velocity_value.set_text(str("{:.2f}".format(slider_velocity.get_current_value())))

    for i in range(len(particles)):
        draw(window, particles[i]["x"], particles[i]["y"], particles[i]["color"], 3)

    manager.draw_ui(window)

    pygame.display.flip()

pygame.quit()
#exit()
