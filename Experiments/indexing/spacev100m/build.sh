#!/bin/bash
#.\IndexBuilder.exe -c buildconfig.ini -d 128 -v UInt8 -f DEFAULT -i FromFile -o sift1b -a SPANN
../../../Debug/indexbuilder -c buildconfig.ini -d 100 -v Int8 -f DEFAULT -i ./data/spacev100m_base.i8bin -o spacev100m -a SPANN
