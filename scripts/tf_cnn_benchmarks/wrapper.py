import sys
import os
import time

CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))

if_ps = (sys.argv[1] == 'ps' or sys.argv[2] == 'ps')
if_ps_worker = (sys.argv[1] == 'psworker' or sys.argv[2] == 'psworker')

if if_ps_worker:
    cmd = '%s %s/tf_cnn_benchmarks.py %s ' % (sys.executable, CURRENT_PATH, ' '.join(sys.argv[2:]))
    worker_cmd = cmd + '--ps_hosts=localhost:7890 --worker_hosts=localhost:7891 --job_name=worker --task_index=0 &'
    ps_cmd = cmd + '--ps_hosts=localhost:7890 --worker_hosts=localhost:7891 --job_name=ps --task_index=0 &'
    os.system(ps_cmd)
    time.sleep(5)
    os.system(worker_cmd)
else:
    if if_ps:
        os.environ['CUDA_VISIBLE_DEVICES']=''
        cmd = '%s %s/tf_cnn_benchmarks.py %s' % (sys.executable, CURRENT_PATH, ' '.join(sys.argv[2:]))
    else:
        cmd = '%s %s/tf_cnn_benchmarks.py %s' % (sys.executable, CURRENT_PATH, ' '.join(sys.argv[1:]))

    code = os.system(cmd)
    print('run %s and return %s' % (cmd, code))
