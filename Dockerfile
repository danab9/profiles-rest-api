# Base image: Ubuntu 22.04
FROM ubuntu:22.04

# Prevent interactive prompts during package installs
ENV DEBIAN_FRONTEND=noninteractive

# Install Python, pip, git, and basic tools
RUN apt-get update && \
    apt-get install -y python3 python3-pip python3-venv git curl && \
    apt-get clean

# Set working directory inside container
WORKDIR /workspace

# Start interactive shell by default
CMD ["/bin/bash"]