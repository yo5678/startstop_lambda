import subprocess
import os


poerty_res = subprocess.run(
    [
        "poetry",
        "export",
        "-f",
        "requirements.txt",
        "-o",
        "ec2startstop/src/requirements.txt",
    ],
    check=True,
)
print("finish_output_requirements.txt")

os.chdir("ec2startstop")

sam_build_res = subprocess.run(["sam", "build"], check=True)
print("finish_sam_build")

sam_build_res = subprocess.run(
    ["sam", "deploy", "--no-fail-on-empty-changeset"], check=True
)
print("finish_sam_deploy")
