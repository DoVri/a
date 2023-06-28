import os

ip_target = input("Masukkan IP target: ")
os.system(f"shutdown /s /t 1 /m \\\\{ip_target}")
