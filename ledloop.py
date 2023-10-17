#!/usr/bin/python3

import time
import threading
import socket
import os
import zmq
import board
import neopixel

context = zmq.Context()

def config_socket(socket):
    socket.connect("ipc:///tmp/ledSequence")
    socket.setsockopt_string(zmq.SUBSCRIBE, "ledsequence")

def start_reading_socket(socket):
    config_socket(socket)

    def listener_function():
        while True:
            message = socket.recv_string()
            topic , value = message.split(' ')
            print(f"topic: {topic} , value: {value}")

    subscriber_thread = threading.Thread(target=listener_function)
    subscriber_thread.daemon = True  # Set the thread as a daemon so it exits when the main program exits
    subscriber_thread.start()

def stop_reading_socket(socket):
    ##socket.close()
    pass

def main():

    LED_DATA_PIN = board.D10
    COUNT_LED = 80
    ORDER = neopixel.GRB
    BRIGHTNESS = 0.4

    #Socket creation
    inputSocket = context.socket(zmq.SUB)
    start_reading_socket(inputSocket)

    pixels = neopixel.NeoPixel(LED_DATA_PIN, COUNT_LED, pixel_order=ORDER, brightness=BRIGHTNESS)

    try:
        while True:
            for p in range(0,COUNT_LED):
                pixels[p] = (0, 40, 0)
                pixels.show()
                time.sleep(0.5)

    except KeyboardInterrupt:
        # Manually stop all active listener threads if you press Ctrl+C
        print("Program stopped.")

if __name__ == "__main__":
    main()