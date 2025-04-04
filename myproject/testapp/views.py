from django.shortcuts import render
import subprocess
import platform
import time

def myview(request):
    process = subprocess.Popen(['top', '-bn1'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    top_output, _ = process.communicate()

    context = {
        'name': 'PRAVEEN KRISHNA R',
        'username': 'codespace',
        'server_time_ist': time.strftime('%Y-%m-%d %H:%M:%S %Z%z', time.localtime(time.time() + 5.5*3600)),
        'top_output': top_output.splitlines(),
    }
    return render(request, 'index.html', context)