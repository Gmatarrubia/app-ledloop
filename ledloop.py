#!/usr/bin/python3

import time
import threading
import socket
import os
import zmq
import board
import neopixel

context = zmq.Context()

# Global configuration
LED_DATA_PIN = board.D10
COUNT_LED = 80
ORDER = neopixel.GRB
BRIGHTNESS = 0.4
PIXELS = neopixel.NeoPixel(LED_DATA_PIN, COUNT_LED, pixel_order=ORDER, brightness=BRIGHTNESS)

def config_socket(socket):
    socket.connect("ipc:///tmp/ledSequence")
    socket.setsockopt_string(zmq.SUBSCRIBE, "ledsequence")

def config_thread(target_function, event):
    target_args = [event]
    thread = threading.Thread(target=target_function, args=(target_args))
    thread.daemon = True  # Set the thread as a daemon so it exits when the main program exits
    return thread

def led_on(event):
    print("led_on")
    while True:
        for p in range(0,COUNT_LED):
            PIXELS[p] = (0, 40, 0)
            PIXELS.show()
            time.sleep(0.5)
            if event.is_set():
                break
        if event.is_set():
            break
    event.clear()
    return

def led_off(event):
    print("led_off")
    PIXELS.fill((0,0,0))
    PIXELS.show()
    event.clear()
    return


def main():

    # Socket creation
    inputSocket = context.socket(zmq.SUB)
    config_socket(inputSocket)

    # Change sequence event (aka killing event)
    change_sec = threading.Event()

    leds_thread = config_thread(led_on, change_sec)
    leds_thread.start()
    print("hey dude")
    try:
        while True:
            print("something")
            message = inputSocket.recv_string()
            topic , value = message.split(' ')
            print(f"topic: {topic} , value: {value}")

            def kill_led_thread():
                if leds_thread.is_alive():
                    change_sec.set()
                    leds_thread.join()

            if topic == "ledsequence":
                if value == "on":
                    kill_led_thread()
                    leds_thread = config_thread(led_on, change_sec)
                    leds_thread.start()
                elif value == "off":
                    kill_led_thread()
                    leds_thread = config_thread(led_off, change_sec)
                    leds_thread.start()

    except KeyboardInterrupt:
        # Manually stop all active listener threads if you press Ctrl+C
        print("Program stopped.")

if __name__ == "__main__":
    main()
