with open("test.jpg", "rb") as f:
    data = bytearray(f.read())

# Mencari marker SOF0 (0xFF, 0xC0) atau SOF2 (0xFF, 0xC2)
sof_index = -1
for marker in [b"\xff\xc0", b"\xff\xc1", b"\xff\xc2"]:
    idx = data.find(marker)
    if idx != -1:
        sof_index = idx
        break

if sof_index != -1:
    # Height berada di offset +5 dan +6 dari awal marker SOF
    height_offset = sof_index + 5

    # Ambil height lama
    old_height = int.from_bytes(
        data[height_offset : height_offset + 2], "big"
    )

    # Tambahkan tinggi gambar (misal ditambah 300-500 piksel)
    new_height = old_height + 400
    data[height_offset : height_offset + 2] = new_height.to_bytes(2, "big")

    with open("fixed_flag.jpg", "wb") as f:
        f.write(data)

    print(
        f"Height diubah dari {old_height}px ke {new_height}px! Cek file fixed_flag.jpg"
    )
else:
    print("Marker SOF tidak ditemukan.")
