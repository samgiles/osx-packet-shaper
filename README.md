# Packet Shaper

Shapes packets on Mac OS X, useful for debugging network applications under different network conditions.

## Usage

```SHELL
shaper [-h] -d DELAY -bw BANDWIDTH -pl PACKET_LOSS
arguments:
  -h, --help       show this help message and exit
  -d DELAY         The network propagation delay
  -bw BANDWIDTH    The up and down bandwidth in KBit/s
  -pl PACKET_LOSS  The percentage of packets lost
```
