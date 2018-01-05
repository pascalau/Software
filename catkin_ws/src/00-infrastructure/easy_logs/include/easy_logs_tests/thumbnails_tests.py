import shutil

import duckietown_utils as dtu



@dtu.unit_test
def test_thumbnails():
    id_log = '2016-04-29-dp3auto-neptunus-1'
    cmd = ['rosrun', 'easy_logs', 'thumbnails', id_log, '-c', 'rmake']
    run_one(cmd)
    
@dtu.unit_test
def test_videos():
    id_log = '2016-04-29-dp3auto-neptunus-1/{1:3}'
    cmd = ['rosrun', 'easy_logs', 'videos', id_log, '-c', 'rmake']
    run_one(cmd)
    
def run_one(cmd):
    v = False
    cwd = dtu.create_tmpdir('run-regression')
    try:
        dtu.system_cmd_result(cwd, cmd,
              display_stdout=v,
              display_stderr=v,
              raise_on_error=True)
    finally:
        shutil.rmtree(cwd)  
    