#!/usr/bin/python3
import Crypto.Util.number as nb
import argparse

# Initialize the Parser
parser = argparse.ArgumentParser(description ='Plain text to long converter')
  
# Adding Arguments
parser.add_argument('pt', 
                    type = str,
                    help ='Plain Text')
m = parser.parse_args().pt
pt = nb.bytes_to_long(m.encode('utf-8'))

## Change n and e here
n = 24713797430690594222395463232755979441235204168969837473804233232745361940112453164738324992068941061597231100739341266493628844571251820573004817362887419462270310850741074968373417461728588649248923609176771249368899291906340258033721719437505102599726831313060941556774519118390148917058344981529963610252306747878170490354356920113273685410221620096548233208401870259421011689015130767731288589470639256355335866496463076629314016348135007471673454411641179551637737003004114455565329548478010749122899971275003037457765040806645883870944559797535608038816014862215723598899047710913985172892372149464990981240031

e = 65537

ct = pow(pt,e,n)
print("Plain text: " + m, end="\n\n")
print("Cipher Text in long form (ct):", ct, end="\n\n")