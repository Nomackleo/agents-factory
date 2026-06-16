# Base template for Agent Factory Ecosystems
FROM ubuntu:22.04

# Install basic dependencies
RUN apt-get update && apt-get install -y \
    curl \
    git \
    python3 \
    python3-pip \
    nodejs \
    npm \
    && rm -rf /var/lib/apt/lists/*

# Set up Antigravity environment variables
ENV ANTIGRAVITY_WORKSPACE=/app
ENV ANTIGRAVITY_ENV=production

# Set working directory
WORKDIR /app

# Copy the entire generated ecosystem
COPY . .

# Expose standard Antigravity ports if needed
EXPOSE 8080

# Default command to run the Antigravity ecosystem
CMD ["python3", "-m", "http.server", "8080"]
