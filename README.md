#

The essential part of this repo is an alias (aka symbols or registers) file, EM340_aliases.txt for the tool modbus-cli, for use with the Carlo Gavazzi EM340 modbus energy meter.

Using this file, one can access particular registers on the EM340 by using aliases instead of the register addresses.

    modbus 39/
    modbus i@770/H

    modbus

I have manually built this list from this PDF (https://gavazzi.se/app/uploads/2020/11/em330_em340_et330_et340_cp.pdf).

