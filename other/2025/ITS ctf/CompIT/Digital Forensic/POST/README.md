# 『POST』
> aku mencoba mengirim pesan rahasia ke google

<img width="804" height="418" alt="image" src="https://github.com/user-attachments/assets/6ef4ead7-555e-40c8-a6e0-80483b116205" />

Author: hyall

# 『The challenge』

We're given pcap file. To open this file, we need wireshark. Here the result:

<img width="940" height="322" alt="image" src="https://github.com/user-attachments/assets/f2e77a1a-971e-42c8-9f04-c35ea2ea083e" />

Seems interesting, let solve!

# 『Solving challenge』
> Solve by: pemula

Based on problem, the clue is `POST` so we must filter just show post. Here the result:

<img width="774" height="424" alt="image" src="https://github.com/user-attachments/assets/4096b1b6-e230-4a6a-8f81-e5ce59242572" />

<img width="753" height="413" alt="image" src="https://github.com/user-attachments/assets/f3681a0a-f652-4a1b-ab8c-06415b28331a" />

Each post will send 1 word for flag. So we must write it on notepad

# 『Flag』

<img width="827" height="233" alt="image" src="https://github.com/user-attachments/assets/beba816c-40d0-45b4-a754-27be331a5d2e" />

```
Flag: compit{http_network_forensic_633f851c}
```
