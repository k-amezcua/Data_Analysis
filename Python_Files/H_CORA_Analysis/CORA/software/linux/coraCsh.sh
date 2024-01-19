#!/bin/csh -f
#
# CORAplus install directory
setenv INST_PATH Installation_Path
#
# execute CORAplus
$INST_PATH/CORAplus_4.0.5 $argv[*]
#
