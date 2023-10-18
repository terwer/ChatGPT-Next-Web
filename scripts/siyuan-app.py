import subprocess
import shutil
import platform

# Set build mode
build_mode = "standalone"

# Build command
build_command = f"cross-env BUILD_MODE={build_mode} next build"

# Execute build command
subprocess.run(build_command, shell=True)

# Copy static and public folders
shutil.copytree(".next/static", f".next/{build_mode}/.next/static")
shutil.copytree("public", f".next/{build_mode}/public")