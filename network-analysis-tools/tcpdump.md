---
layout: default
---

# Tcpdump

**`"ANYONE CAN SEE A FOREST FIRE. SKILL LIES IN SNIFFING THE FIRST SMOKE." - ROBERT A HEINLEIN.`**

Network Analysis tool/Utility. \(looking under the hood\)

Can be stored in a file or print on a screen.

tcpdump -h

```text
tcpdump version tcpdump version 4.9.2 -- Apple version 83.200.2
libpcap version 1.8.1 -- Apple version 79.250.1
LibreSSL 2.2.7
Usage: tcpdump [-aAbdDefhHIJKlLnNOpqStuUvxX#] [ -B size ] [ -c count ]
                [ -C file_size ] [ -E algo:secret ] [ -F file ] [ -G seconds ]
                [ -i interface ] [ -j tstamptype ] [ -M secret ] [ --number ]
                [ -Q in|out|inout ]
                [ -r file ] [ -s snaplen ] [ --time-stamp-precision precision ]
                [ --immediate-mode ] [ -T type ] [ --version ] [ -V file ]
                [ -w file ] [ -W filecount ] [ -y datalinktype ] [ -z postrotate-command ]
[ -g ] [ -k ] [ -o ] [ -P ] [ -Q met[ --time-zone-offset offset ]
                [ -Z user ] [ expression ]
```

* NOTE: 
  * super user required
  * triggers DNS traffic

## Check available interfaces

`tcpdump -D`

## Capture all interfaces

`-i any`

## Count \(stops at\)

`-c n`

## No reverse or ptr lookup

`-n`

## Set capture size

`-s96` \( default 96 bytes\)

Quick Note:

* seq number: after first it represents relative seq number by default.

## compound expression

`tcpdump -i eth0 -n "host 192xxxx and (port 80 or port 443)"`

Quick Note:

* paranthesis around the port number otherwise it wont be interpreted differently and also quotes around expression otherwise paranthesis will be treated differently in bash.

## More filters

`"src net 192.168.0.0/16" and not dst net 192.168.0.0/16 and not dst net 10.0.0.0/18"`

## Mac based filter

`-e (to see capture)`

## Protocol type filter

`-i any ip6`

## only for syn

`"tcp[tcpflags] & tcp-syn !=0"`

## only for tcp reset

`"tcp[tcpflags] & tcp-rst !=0"`

## Adjusting output

-XX \(hex format as well as asci format\)

-A \(only asci HTTP data\)

-vvv \(Verbosity\)

-K \(ignore checksum error\)

-q \(minimal display output\)

-t \(removes timestamp\)

-ttt \(time diff between two packets\)

-ttttt \(time since first packet\)

## Advanced header filtering

### TCP Segment structure

TCP segment consists of header & data.

**TCP header**

```text
0               8               16               24            32
|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|
|          Source Port          |       Destination Port        |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                        Sequence Number                        |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                    Acknowledgment Number                      |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|  Data |       |C|E|U|A|P|R|S|F|                               |
| Offset|  Res. |W|C|R|C|S|S|Y|I|            Window             | 
|       |       |R|E|G|K|H|T|N|N|                               |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+--+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|           Checksum            |         Urgent Pointer        |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                    Options                    |    Padding    |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
```

**Source port**

16 bit field that holds the port address of application that is sending the data segment.

**Destination port**

16 bit field that holds the port address of the application in the host that is receiving the data segment.

**Sequence Number**

32 bit field that holds the sequence number i.e the byte number of the first byte that is sent in that particular segment. This is used to reassemble the message at the recivening end if the segments are recieved out of order.

**Acknowledgement Number**

32 bit field that holds the acknowledgement number, i.e, the byte number that the receiver expects to receive next. It is an acknowledgment for the previous bytes being received successfully.

**Data offset \(HLEN\)**

This is a 4 bit field that indicates the length of the TCP header by number of 4-byte words in the header, i.e, if the header is of 20 bytes\(min length of TCP header\), then this field will hold 5 \(because 5 x 4 = 20\) and the maximum length: 60 bytes, then it’ll hold the value 15\(because 15 x 4 = 60\). Hence, the value of this field is always between 5 and 15.

The purpose of the data offset is to tell the upper layers where the data starts. The TCP header can be anywhere from 5-15 words long. So you need to know where the header ends and the data begins.

**Reserved**

For future use and should be set to zero.

**Control Flags**

Contains 9 1-bit flags \(control bits\) as follows:

**Window size**

This field tells the window size of the sending TCP in bytes.

**Checksum**

This field holds the checksum for error control. It is mandatory in TCP as opposed to UDP.

**Urgent pointer**

This field \(valid only if the URG control flag is set\) is used to point to data that is urgently required that needs to reach the receiving process at the earliest. The value of this field is added to the sequence number to get the byte number of the last urgent byte.

**Options and padding**

### Filter data packets

The flags are defined in the 14th byte of the TCP header.

In order to filter data packets we will have to look into packets with ACK and PSH are represented by the fourth and fifth bits of the 14th byte from TCP header \(above table\).

| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| C | E | U | `A` | `P` | R | S | F |
| W | C | R | `C` | `S` | S | Y | I |
| R | E | G | `K` | `H` | T | N | N |

Calculating required bits: `echo "$((2#00011000))"`

So, this means; you would want to filter using `'tcp[13] = 24'`

e.g: `tcpdump -A - n 'tcp[13] = 24'`

## Calculating flag's position

_You count the bytes \(8 bits\) from the top, numbering them at 0:_

* So _"Source Port"_ & _"Destination Port"_ would make up bytes 0, 1, 2, & 3.
* The next row, _"Sequence Number"_, would be 4-7.
* _"Acknowledge Number"_ would be bytes 8-11.
* _"Data Offset" & "Res."_ would be byte 12.
* That takes you to byte 13, the bits in this byte are the flags.

### Flag details

| Flag Name | Header | Location | Purpose |
| :---: | :---: | :---: | :---: |
| CWR | TCP | 8-bit | Congestion Window Reduced \(CWR\) |
| ECE | TCP | 9-bit | ECE: ECN Echo |
| ECT | IP | 14-bit | ECN Capable Transport |
| CE | IP | 15-bit | Congestion Experienced |
| URG |  | 16-bit | Urgent |
| ACK |  |  | Acknowledgement \(Acknowledges received data\) |
| PSH |  |  | Request for Push |
| RST |  |  | Reset \(Aborts a connection in response to an error\) |
| SYN |  |  | Syn \(Initiates a connection\) |
| FIN |  |  | Fin \(Closes a connection\) |

\(ECN : Explicit Congestion Notification\)

### Bit order

I'll also mention that the number stored in byte 13 is ordered such that:

* bit 1 = _FIN_
* bit 2 = _SYN_
* bit 4 = _RST_
* bit 8 = _PSH_
* bit 16 = _ACK_
* bit 32 = _URG_

### Filtering data packets only

To do this, we will look for packets that have the PSH and ACK flags turned on. All packets sent and received after the initial 3-way handshake will have the ACK flag set. The PSH flag 709 is used to enforce immediate delivery of a packet and is commonly used in interactive Application Layer protocols to avoid buffering.

We can pass this number to tcpdump with 'tcp\[13\] = 24' as a display filter to indicate that we only want to see packets with the ACK and PSH bits set \("data packets"\) as represented by the fourth and fifth bits \(24\) of the 14th byte of the TCP header. Bear in mind, the tcpdump array index used for counting the bytes starts at zero, so the syntax should be \(tcp\[13\]\).

### Matching PSH-ACK packets

`tcpdump -i eth1 'tcp[13] = 24'`

* Reference:
  * [https://www.tcpdump.org/](https://www.tcpdump.org/)
  * [https://hackertarget.com/tcpdump-examples/](https://hackertarget.com/tcpdump-examples/)
  * [https://danielmiessler.com/study/tcpdump/](https://danielmiessler.com/study/tcpdump/)
  * [https://packetlife.net/blog/2011/mar/2/tcp-flags-psh-and-urg/](https://packetlife.net/blog/2011/mar/2/tcp-flags-psh-and-urg/)
  * [https://en.wikipedia.org/wiki/Transmission\_Control\_Protocol](https://en.wikipedia.org/wiki/Transmission_Control_Protocol)
  * [https://gist.github.com/bom-d-van/b3ab3e6e924e31bacebae3a508cbd3eb](https://gist.github.com/bom-d-van/b3ab3e6e924e31bacebae3a508cbd3eb)
  * [https://serverfault.com/questions/922988/tcpdump-tcp-header-offset-13](https://serverfault.com/questions/922988/tcpdump-tcp-header-offset-13)

