from django.shortcuts import render
from django.http import HttpResponse
import os
import subprocess
import sys

from dotenv import load_dotenv

load_dotenv()

bm_root = os.getenv("BM_ROOT")
print('------------ bm root', bm_root)
def blinky(request):
    blinky_path = "blink_led/"
    pa = bm_root + blinky_path
    blinky = "blinky"
    full_path = bm_root + blinky_path + blinky
    subprocess.run([full_path, 'start'])
    return HttpResponse("hello")
