import blockchain as bc
import sys

args = sys.argv
app = bc.Application()

try:
    app.run(host='0.0.0.0', port=int(args[1]))
except:
    print("err: bad argument")
    print("ex: python bcserver.py 5000")