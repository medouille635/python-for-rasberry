from sense_hat import SenseHat
import time
from datetime import datetime
import csv
import os

s = SenseHat()
s.low_light = True

# Fichier de sauvegarde
SAVE_FILE = "temperature_log.csv"

# Initialiser le fichier CSV s'il n'existe pas
if not os.path.exists(SAVE_FILE):
    with open(SAVE_FILE, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Date', 'Heure', 'Temperature_Celsius'])

def save_temperature(temp):
    """Sauvegarde la température avec date et heure"""
    now = datetime.now()
    date_str = now.strftime("%Y-%m-%d")
    time_str = now.strftime("%H:%M:%S")
    
    with open(SAVE_FILE, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([date_str, time_str, temp])
    
    print(f"Température sauvegardée: {temp}°C à {date_str} {time_str}")

input_temperature = round(s.get_temperature())
white = (255,255,255)
nothing = (0,0,0)

def celsius():
    W = white
    O = nothing
    logo = [
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, W, W, O, W, W, O, O,
    O, W, W, O, W, O, O, O,
    O, O, O, O, W, W, O, O,
    ]
    return logo

def left1():
    W = white
    O = nothing
    logo = [
    O, W, O, O, O, O, O, O,
    W, W, O, O, O, O, O, O,
    O, W, O, O, O, O, O, O,
    O, W, O, O, O, O, O, O,
    O, W, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    ]
    return logo

def right1():
    W = white
    O = nothing
    logo = [
    O, O, O, O, O, O, W, O,
    O, O, O, O, O, W, W, O,
    O, O, O, O, O, O, W, O,
    O, O, O, O, O, O, W, O,
    O, O, O, O, O, O, W, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    ]
    return logo

def right2():
    W = white
    O = nothing
    logo = [
    O, O, O, O, W, W, W, O,
    O, O, O, O, O, O, W, O,
    O, O, O, O, W, W, W, O,
    O, O, O, O, W, O, O, O,
    O, O, O, O, W, W, W, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    ]
    return logo

def left3():
    W = white
    O = nothing
    logo = [
    W, W, W, O, O, O, O, O,
    O, O, W, O, O, O, O, O,
    O, W, W, O, O, O, O, O,
    O, O, W, O, O, O, O, O,
    W, W, W, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    ]
    return logo

def left2():
    W = white
    O = nothing
    logo = [
    W, W, W, O, O, O, O, O,
    O, O, W, O, O, O, O, O,
    W, W, W, O, O, O, O, O,
    W, O, O, O, O, O, O, O,
    W, W, W, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    ]
    return logo
    
def right3():
    W = white
    O = nothing
    logo = [
    O, O, O, O, W, W, W, O,
    O, O, O, O, O, O, W, O,
    O, O, O, O, O, W, W, O,
    O, O, O, O, O, O, W, O,
    O, O, O, O, W, W, W, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    ]
    return logo
    
def left4():
    W = white
    O = nothing
    logo = [
    W, O, W, O, O, O, O, O,
    W, O, W, O, O, O, O, O,
    W, W, W, O, O, O, O, O,
    O, O, W, O, O, O, O, O,
    O, O, W, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    ]
    return logo

def right4():
    W = white
    O = nothing
    logo = [
    O, O, O, O, W, O, W, O,
    O, O, O, O, W, O, W, O,
    O, O, O, O, W, W, W, O,
    O, O, O, O, O, O, W, O,
    O, O, O, O, O, O, W, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    ]
    return logo    

def left5():
    W = white
    O = nothing
    logo = [
    W, W, W, O, O, O, O, O,
    W, O, O, O, O, O, O, O,
    W, W, W, O, O, O, O, O,
    O, O, W, O, O, O, O, O,
    W, W, W, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    ]
    return logo 
    
def right5():
    W = white
    O = nothing
    logo = [
    O, O, O, O, W, W, W, O,
    O, O, O, O, W, O, O, O,
    O, O, O, O, W, W, W, O,
    O, O, O, O, O, O, W, O,
    O, O, O, O, W, W, W, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    ]
    return logo 
    
def left6():
    W = white
    O = nothing
    logo = [
    W, W, W, O, O, O, O, O,
    W, O, O, O, O, O, O, O,
    W, W, W, O, O, O, O, O,
    W, O, W, O, O, O, O, O,
    W, W, W, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    ]
    return logo    
    
def right6():
    W = white
    O = nothing
    logo = [
    O, O, O, O, W, W, W, O,
    O, O, O, O, W, O, O, O,
    O, O, O, O, W, W, W, O,
    O, O, O, O, W, O, W, O,
    O, O, O, O, W, W, W, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    ]
    return logo  
    
def left7():
    W = white
    O = nothing
    logo = [
    W, W, W, O, O, O, O, O,
    O, O, W, O, O, O, O, O,
    O, O, W, O, O, O, O, O,
    O, W, O, O, O, O, O, O,
    O, W, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    ]
    return logo  
    
def right7():
    W = white
    O = nothing
    logo = [
    O, O, O, O, W, W, W, O,
    O, O, O, O, O, O, W, O,
    O, O, O, O, O, O, W, O,
    O, O, O, O, O, W, O, O,
    O, O, O, O, O, W, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    ]
    return logo
    
def left8():
    W = white
    O = nothing
    logo = [
    W, W, W, O, O, O, O, O,
    W, O, W, O, O, O, O, O,
    W, W, W, O, O, O, O, O,
    W, O, W, O, O, O, O, O,
    W, W, W, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    ]
    return logo
    
def right8():
    W = white
    O = nothing
    logo = [
    O, O, O, O, W, W, W, O,
    O, O, O, O, W, O, W, O,
    O, O, O, O, W, W, W, O,
    O, O, O, O, W, O, W, O,
    O, O, O, O, W, W, W, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    ]
    return logo  
    
def left9():
    W = white
    O = nothing
    logo = [
    W, W, W, O, O, O, O, O,
    W, O, W, O, O, O, O, O,
    W, W, W, O, O, O, O, O,
    O, O, W, O, O, O, O, O,
    W, W, W, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    ]
    return logo  

def right9():
    W = white
    O = nothing
    logo = [
    O, O, O, O, W, W, W, O,
    O, O, O, O, W, O, W, O,
    O, O, O, O, W, W, W, O,
    O, O, O, O, O, O, W, O,
    O, O, O, O, W, W, W, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    ]
    return logo  
    
def left0():
    W = white
    O = nothing
    logo = [
    W, W, W, O, O, O, O, O,
    W, O, W, O, O, O, O, O,
    W, O, W, O, O, O, O, O,
    W, O, W, O, O, O, O, O,
    W, W, W, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    ]
    return logo 
    
def right0():
    W = white
    O = nothing
    logo = [
    O, O, O, O, W, W, W, O,
    O, O, O, O, W, O, W, O,
    O, O, O, O, W, O, W, O,
    O, O, O, O, W, O, W, O,
    O, O, O, O, W, W, W, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    ]
    return logo  

left_functions = {
    0: left0, 1: left1, 2: left2, 3: left3, 4: left4,
    5: left5, 6: left6, 7: left7, 8: left8, 9: left9
}

right_functions = {
    0: right0, 1: right1, 2: right2, 3: right3, 4: right4,
    5: right5, 6: right6, 7: right7, 8: right8, 9: right9
}

def combine_displays(left_func, right_func):
    left_pixels = left_func()
    right_pixels = right_func()
    
    combined = []
    for i in range(64):
        if left_pixels[i] != nothing:
            combined.append(left_pixels[i])
        else:
            combined.append(right_pixels[i])
    
    return combined

nombre_left = input_temperature // 10  
nombre_right = input_temperature % 10  

print("temperature input :")
print(input_temperature)
print("1er chiffre :")
print(nombre_left)
print("2e chiffre :")
print(nombre_right)

# Sauvegarder la température initiale
save_temperature(input_temperature)

images = [celsius]
count = 0

while True:
    left_func = left_functions[nombre_left]
    right_func = right_functions[nombre_right]
    
    combined_display = combine_displays(left_func, right_func)
    s.set_pixels(combined_display)
    time.sleep(1) 
    s.set_pixels(images[count % len(images)]())
    time.sleep(1)
    count += 1
    
    if count == 1:
        current_temp = round(s.get_temperature())
        nombre_left = current_temp // 10
        nombre_right = current_temp % 10
        
        # Sauvegarder la nouvelle température
        save_temperature(current_temp)
        
        count = 0
