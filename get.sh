modbus \
  --slave-id 1 \
  --baud 9600 \
  --parity n \
  --timeout 1.0 \
  -v \
  --byte-order=be \
  --registers data/EM340_aliases.txt \
  /dev/ttyUSB0 \
  $1

#
#  i@770/H
#--byte-order=be \
