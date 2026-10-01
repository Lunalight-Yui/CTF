FROM debian:bookworm-slim

RUN apt-get update && apt-get install -y socat && rm -rf /var/lib/apt/lists/*

RUN useradd -m -s /bin/false ctfuser
WORKDIR /home/ctfuser

COPY nexus_core /home/ctfuser/nexus_core
COPY flag.txt /home/ctfuser/flag.txt

RUN chown -R root:root /home/ctfuser && \
    chmod 755 /home/ctfuser && \
    chmod 755 /home/ctfuser/nexus_core && \
    chmod 444 /home/ctfuser/flag.txt

USER ctfuser
EXPOSE 7654

CMD ["socat", "TCP-LISTEN:7654,reuseaddr,fork", "EXEC:/home/ctfuser/nexus_core,stderr"]