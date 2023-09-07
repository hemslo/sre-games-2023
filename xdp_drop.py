from bcc import BPF
import sys
import time
import os


def main():
    device = os.environ.get("DEVICE")
    if device is None:
        print(f"Usage: DEVICE=<ifdev> {sys.argv[0]}")
        print(f"e.g.: DEVICE=cni0 {sys.argv[0]}")
        exit(1)
    bpf = BPF(src_file="xdp_drop.c", cflags=["-w", "-DRETURNCODE=XDP_DROP"])
    fn = bpf.load_func("xdp_prog_drop", BPF.XDP)
    time.sleep(int(os.environ.get("SLEEP_TIME", 0)))
    bpf.attach_xdp(device, fn, 0)
    print("Dropping packets, hit CTRL+C to stop")
    while True:
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            print("Removing filter from device")
            bpf.remove_xdp(device, 0)
            break


if __name__ == '__main__':
    main()
