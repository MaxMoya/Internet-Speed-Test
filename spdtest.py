print('Welcome to the Speedtest!')

import speedtest
import time

st = speedtest.Speedtest()
print('Loading Servers...')
st.get_servers()
time.sleep(.5)
print('Choosing Server...')
st.get_best_server()
print('Download Speed:')
inter1 = int(st.download() / 1024 / 1024)
print(inter1,'mbps')
time.sleep(1)
print('Upload Speed:')
inter2 = int(st.upload() / 1024 / 1024)
print(inter2,'mbps')