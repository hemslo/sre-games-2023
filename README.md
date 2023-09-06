# sre-games-2023

## POC

1. start VM `limactl start k3s.yaml`
2. SHELL1: shell into VM `limactl shell k3s`
3. SHELL1: start a test pod `kubectl run test -ti --rm --image=alpine`
4. SHELL1: install curl `apk add curl`
5. SHELL1: test network is working `curl -I https://www.google.com`
6. SHELL2: start another shell from host `limactl shell k3s`
7. SHELL2: attach xdp `sudo python3 xdp_drop.py cni0`
8. SHELL1: verify network is not working `curl -I https://www.google.com`
9. SHELL2: detach xdp by pressing `Ctrl+C`
10. SHELL1: verify network is working again `curl -I https://www.google.com`


## Investigate and fix steps

After xdp is attached, network is not working. Investigate and fix steps:

1. `sudo bpftool prog tracelog` to check logs
2. `sudo bpftool prog show | grep xdp` to find xdp program
3. `ip link show` to find attached device
4. `sudo bpftool net detach xdpgeneric dev <dev>` to detach xdp

## Hints

1. [eCHO episode 11: Exploring bpftool with Quentin Monnet](https://www.youtube.com/watch?v=1EOLh3zzWP4)
2. [eCHO episode 13: XDP Hands-on Tutorial](https://www.youtube.com/watch?v=YUI78vC4qSQ)
