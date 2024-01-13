from django.shortcuts import render
from django.http import HttpResponse

import subprocess
import sys

bm_root = "/home/pauljohns/Documents/baremetal/"

def blinky(request):
    blinky_path = "blink_led/"
    pa = bm_root + blinky_path
    blinky = "blinky"
    full_path = bm_root + blinky_path + blinky
    subprocess.run([full_path, 'start'])
    return HttpResponse("hello")
