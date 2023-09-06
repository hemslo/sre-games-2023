from bcc import BPF
import sys
import time


def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <ifdev>")
        print(f"e.g.: {sys.argv[0]} eth0")
        exit(1)
    device = sys.argv[1]
    bpf = BPF(src_file="xdp_drop.c", cflags=["-w", "-DRETURNCODE=XDP_DROP"])
    fn = bpf.load_func("xdp_prog_drop", BPF.XDP)
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
