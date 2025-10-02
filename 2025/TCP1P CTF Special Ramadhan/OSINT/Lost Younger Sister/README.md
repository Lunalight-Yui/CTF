# 『Lost Younger Sister』
> Help Jieyab find the Violet, please read the attachment

> The flag is is name of the bus stop in the photo

> [Zip file](https://tcp.1pc.tf/assets/aa69878a995e15aa4ae0ea26d780ad63e27a028fb78af556ffe5d474ed13880a/lostyoungersister_attachment.zip) 

# 『Format Flag』
> Example Flag : TCP1P{KARIMUN JAWA 11 A}

# 『Hints』
> *Pro tips: Check the case sensitive! Check the street view

Author: Jieyab89

# 『The Challenge』

We're given 4 files and 1 zip. Here all the list:

<img width="783" height="201" alt="image" src="https://github.com/user-attachments/assets/3b899c1f-f4c1-42a6-a4ca-3a659adf073b" />

Here is a pdf file:

<img width="788" height="819" alt="image" src="https://github.com/user-attachments/assets/80b8b6f9-bf89-4902-a15e-4d3b18f2c0b3" />

# 『Solving Challenge』

To solve, you can go to `Violet Password Manager.kdbx` file and double click. It should be looks like this:

<img width="551" height="279" alt="Screenshot 2025-10-02 084012" src="https://github.com/user-attachments/assets/9dc31768-d326-44b8-82fa-e553c6f741e2" />

If you can't open like this, you should go to this link: https://keepass.info/help/kb/kdbx.html and to understand how to use it. The download on this link:
https://keepass.info/download.html

Then, we must search the password. On the pdf files, it mention the password: `The password is her birth date`. Where i can find? here the conversation mention:

<img width="737" height="166" alt="image" src="https://github.com/user-attachments/assets/9e981f73-9a2f-4820-9dd4-5307b08f99e5" />

After that, i found her birth date. here the result on pdf files:

<img width="793" height="482" alt="image" src="https://github.com/user-attachments/assets/234eb21d-db3a-4471-ada0-fbcffd1e0f70" />

But it was incorrect. So i try another one that `Marin` mention. Her pet, `Ogipedro`, and it success!!

<img width="870" height="633" alt="image" src="https://github.com/user-attachments/assets/7a9fa0b6-0b65-49c2-ac99-1008429acb00" />

So we can right click and click `Edit Entry` on Icloud Backup. and the result:

<img width="654" height="629" alt="image" src="https://github.com/user-attachments/assets/f3e8f0b4-a397-4947-8a24-4ae022c98d8c" />

By inserting `Ogipedro10022001` on zip file, we can get the image. The result:

![find this location](https://github.com/user-attachments/assets/c5b19aa5-f2d3-4982-af3e-158c1932d8e6)

So how to detect where is this place? There are 2 ways:

- From number on motorcycle and car `BG ...` and you can check on this website: https://auto2000.co.id/berita-dan-tips/plat-bg-daerah-mana-tips (Palembang)
- From Whatsapp number: `0898-001-1111`. If you insert this keyword: `WA: 0898-001-1111` on google, you will get this one: <img width="1919" height="915" alt="image" src="https://github.com/user-attachments/assets/e682b6b1-12fd-497a-8465-80fbf34974ae" />

So, one of the picture that **ALMOST** same as the chall is this one: 

<img width="339" height="328" alt="image" src="https://github.com/user-attachments/assets/80f6c37e-b98f-48ca-9a32-92d505630a51" />

After i open, i suddenly realizes this picture is the same on picture. The picture that i mean:

![aaaaaa](https://github.com/user-attachments/assets/1b5ed4ce-b155-4a25-b0aa-fc2fd2833343)

And that place was `SD Muhammadiyah 6 Palembang`. So, from this information we will get the place on google maps. I find 2 bussways stop on this google maps:

<img width="928" height="572" alt="image" src="https://github.com/user-attachments/assets/b09385ae-3e6e-4b17-af07-4823a611e019" />

From the angle, the school should be on right place and one of the bus stop on the left side. And we found the flag

<img width="977" height="406" alt="image" src="https://github.com/user-attachments/assets/a939f6d2-683e-4bb9-9dae-8afb74e755a6" />

```
Flag: TCP1P{JPO SMP MUHAMMADIYAH 10 B}
```
