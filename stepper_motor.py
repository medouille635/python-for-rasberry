import RPi.GPIO as GPIO
import time

# --- Configuration des broches ---
DIR_PIN = 27       # Sens de rotation
STEP_PIN = 17      # Signal de pas
ENABLE_PIN = 22    # Activation du driver (LOW = activé)

# --- Paramètres du moteur ---
STEP_DELAY = 0.001  # Délai entre les pas (plus petit = plus rapide)
STEPS_PER_REV = 200 # Nombre de pas pour un tour (ex : 200 pour un NEMA17)

# --- Initialisation des GPIO ---
GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR_PIN, GPIO.OUT)
GPIO.setup(STEP_PIN, GPIO.OUT)
GPIO.setup(ENABLE_PIN, GPIO.OUT)

# Active le driver
GPIO.output(ENABLE_PIN, GPIO.LOW)

try:
    while True:
        # --- Rotation dans un sens ---
        GPIO.output(DIR_PIN, GPIO.HIGH)
        print("Rotation horaire")
        for _ in range(STEPS_PER_REV):
            GPIO.output(STEP_PIN, GPIO.HIGH)
            time.sleep(STEP_DELAY)
            GPIO.output(STEP_PIN, GPIO.LOW)
            time.sleep(STEP_DELAY)
        time.sleep(1)

        # --- Rotation dans l'autre sens ---
        GPIO.output(DIR_PIN, GPIO.LOW)
        print("Rotation antihoraire")
        for _ in range(STEPS_PER_REV):
            GPIO.output(STEP_PIN, GPIO.HIGH)
            time.sleep(STEP_DELAY)
            GPIO.output(STEP_PIN, GPIO.LOW)
            time.sleep(STEP_DELAY)
        time.sleep(1)

except KeyboardInterrupt:
    print("Arrêt du programme")

finally:
    GPIO.output(ENABLE_PIN, GPIO.HIGH)  # Désactive le driver
    GPIO.cleanup()
