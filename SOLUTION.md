## Investigate and fix steps

After xdp is attached, network is not working. Investigate and fix steps:

1. `sudo bpftool prog tracelog` to check logs
2. `sudo bpftool prog show | grep xdp` to find xdp program
3. `ip link show` to find attached device
4. `sudo bpftool net detach xdpgeneric dev <dev>` to detach xdp
