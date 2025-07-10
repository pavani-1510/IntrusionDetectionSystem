import pyshark
import pandas as pd

cap = pyshark.FileCapture('/home/pavani/Documents/VSCODE/IntrusionDetectionSystem/capture.pcap')
data = []
for pkt in cap:
    try:
        data.append({
            'time': pkt.sniff_time,
            'src': pkt.ip.src,
            'dst': pkt.ip.dst,
            'proto': pkt.highest_layer,
            'length': pkt.length
        })
    except AttributeError:
        continue
df = pd.DataFrame(data)
df.to_csv('packets.csv', index=False)