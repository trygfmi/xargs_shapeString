# python $(find . -type f -maxdepth 3 -name "compare_diff-output.py" | grep macos)

import time
from lxml import html
import subprocess


start_time=time.time()
target_os = "macos"
manual_quickstart_file_path = f"test/{target_os}/compare-manual/"+subprocess.run("ls -1t test/macos/compare-manual | sed -n '2p'", shell=True, capture_output=True, text=True).stdout.strip()
manual_procedure_file_path = f"test/{target_os}/compare-manual/"+subprocess.run("ls -1t test/macos/compare-manual | sed -n '1p'", shell=True, capture_output=True, text=True).stdout.strip()
auto_quickstart_file_path = f"test/{target_os}/compare-auto/"+subprocess.run("ls -1t test/macos/compare-auto | sed -n '2p'", shell=True, capture_output=True, text=True).stdout.strip()
auto_procedure_file_path = f"test/{target_os}/compare-auto/"+subprocess.run("ls -1t test/macos/compare-auto | sed -n '1p'", shell=True, capture_output=True, text=True).stdout.strip()

print(auto_quickstart_file_path)
print(manual_quickstart_file_path)
print(auto_procedure_file_path)
print(manual_procedure_file_path)
print("###################################################################")

diff_quickstart_command = f"""echo "quickstart's diff command is start"
if diff --ignore-all-space --ignore-blank-lines {manual_quickstart_file_path} {auto_quickstart_file_path}; then
    echo "quickstart is ok"
    cat {auto_quickstart_file_path}
    cat {manual_quickstart_file_path}
else
    echo "quickstart is wrong"
fi
"""
subprocess.run(diff_quickstart_command, shell=True)

print()
print("###################################################################")

diff_procedure_command = f"""echo "procedure's diff command is start"
if diff --ignore-all-space --ignore-blank-lines {manual_procedure_file_path} {auto_procedure_file_path}; then
    echo "procedure is ok"
    cat {auto_procedure_file_path}
    cat {manual_procedure_file_path}
else
    echo "procedure is wrong"
fi
"""
subprocess.run(diff_procedure_command, shell=True)

print()
print("###################################################################")

end_time=time.time()
print("かかった時間:"+str(end_time-start_time))



