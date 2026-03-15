# 『Patient Records』

no image this time, forgot to ss

## 『The challenge』

![challs](/2026/intern/PsychCTF%202026/misc/Patient%20Records/image/challs.png)

## 『Highlight vulnerability and parts of interesting』

So this is heap exploitation without pie and canary. It use UAF (use after free) to pointing from one to another pointer. furthermore of explanation: i put it on reference section

you can use [dogbolt](https://dogbolt.org/) to see the file (this is online website) or you can use another decompiler (like ida, ghidra, etc) to decompile the file. Adn for the challs is heap exploitation - use after free

## 『Solving Challenge』
> solve by Lylera

Because this is my first time solve heap exploitation (using ai off course :<), i tried my best to explain it.

There is 1 part function of interesting in here:

```c
int64_t delete_patient()
{
    if (!patient_count)
        return puts("[ERROR] No patients to discharge.");
    
    printf("[DISCHARGE] Patient index (0-%d): ", patient_count - 1);
    int32_t rax_5 = read_int();
    
    if (rax_5 < 0 || rax_5 >= patient_count)
        return puts("[ERROR] Invalid patient index.");
    
    free(*((rax_5 << 3) + &patients));
    return printf("[DISCHARGED] Patient #%d released.\n", rax_5);
}
```

on delete function, there is `free` function which mean you can deallocate the previouse memory and reallocate the new one, while the program still holds the old pointer thinking the original data is still there. Because of this, you can reallocate it to the real one (after delete it) and the data still there because not make it `NULL`. For the explanation of free function: [geek - free function](https://www.geeksforgeeks.org/c/free-function-in-c-library-with-examples/)

after that, you can abuse on function `create_note` to pointing the win function.

So the step:

- create the admit of the patient (example: rua, 9, headache for the dummy)
- delete patient (after we make it)
- create note (pointing to win function with some exploit)
- view patient (with index: 0)
- flag~

![solp](/2026/intern/PsychCTF%202026/misc/Patient%20Records/image/solp.png)

solver script: [solver.py](/2026/intern/PsychCTF%202026/misc/Patient%20Records/challs/solver.py)

## 『Flag』
```
psych{d4ngl1ng_p01nt3rs_1n_th3_p4t13nt_f1l3s_7b3e9a2d}
```

## 『Reference』

- [azrea-lab](https://azeria-labs.com/heap-exploitation-part-1-understanding-the-glibc-heap-implementation/)
- [101 heap exploitation](https://ctf101.org/binary-exploitation/heap-exploitation/)