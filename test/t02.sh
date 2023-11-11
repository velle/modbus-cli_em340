modbus \
  --slave-id 1 \
  --baud 9600 \
  --parity n \
  --timeout 0.5 \
  -v \
  -S \
  --registers data/EM340_aliases.txt \
  /dev/ttyUSB0 \
  44/i
