# python /Users/ojiro/Desktop/programming/running-terminal-commands-blog/xargs/xargs_shapeString/test/windows/wsl/execute-diff-code.py


import time
import subprocess


start_time=time.time()

diff_quickstart_command = """echo "quickstart's diff command is start"
if diff --ignore-all-space --ignore-blank-lines test/windows/wsl/manual_quickstart.txt test/windows/wsl/auto_quickstart.txt; then
    echo "quickstart is ok"
else
    echo "quickstart is wrong"
fi
"""
subprocess.run(diff_quickstart_command, shell=True)

print()

diff_procedure_command = """echo "procedure's diff command is start"
if diff --ignore-all-space --ignore-blank-lines test/windows/wsl/manual_procedure.txt test/windows/wsl/auto_procedure.txt; then
    echo "procedure is ok"
else
    echo "procedure is wrong"
fi
"""
subprocess.run(diff_procedure_command, shell=True)

end_time=time.time()
print("かかった時間:"+str(end_time-start_time))



