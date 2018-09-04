import sys
import os

CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))

if_ps = (sys.argv[1] == 'ps')

if if_ps:
    os.environ['CUDA_VISIBLE_DEVICES']=''

os.system('%s %s/benchmark_cnn.py %s' % (sys.executable, CURRENT_PATH, ' '.join(sys.argv[2:])))
