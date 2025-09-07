# Need Cat
> This is your first beginning entrypoint that you must know how to make a connection with some TCP Connection program.
> nc minictf.ucs.or.id 4432

Author: rootkids

Solve:

Nc is one of the commands in linux. It stand for `Netcat`.  utility tool that uses TCP and UDP connections to read and write in a network. It can be used for both attacking and security.

Now back to the topic. We can copy - paste this `nc minictf.ucs.or.id 4432` on linux command. The template looks like this

<img width="939" height="127" alt="Screenshot 2025-09-06 100858" src="https://github.com/user-attachments/assets/dd4bedcc-89fd-4778-b791-e800c5f41bee" />

After that, we copy that command and paste it on another linux terminal.
The result of that command:

<img width="1473" height="86" alt="Screenshot 2025-09-06 100918" src="https://github.com/user-attachments/assets/677bac0c-891a-4250-85d8-ee5d9e21417b" />

Then we copy the result of the program `curl -sSfL https://pwn.red/pow | sh -s s.AAAAAQ==.9efeh53bOFSUw5X14ZdWFQ==` and send back to first linux command. and the result became like this:

<img width="871" height="344" alt="Screenshot 2025-09-06 101006" src="https://github.com/user-attachments/assets/780468ff-7aaa-4e46-b687-4d38cc94a02e" />

Btw, this is just a part of me to finisih it (because i'm lazy to screenshot 1 by one because it write one character until finish)

```
Flag: UCS{just_1ntro_for_y0u_h0w_t0_connect_1nto_TCP_CONNection}
```
