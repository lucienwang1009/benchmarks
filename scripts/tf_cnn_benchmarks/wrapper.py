import sys
import os

CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))

if_ps = (sys.argv[1] == 'ps')

if if_ps:
    os.environ['CUDA_VISIBLE_DEVICES']=''

cmd = '%s %s/tf_cnn_benchmarks.py %s' % (sys.executable, CURRENT_PATH, ' '.join(sys.argv[2:]))
code = os.system(cmd)
print('run %s and return %s' % (cmd, code))
