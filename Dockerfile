# ---------- Stage 1: Builder ----------
FROM python:3.10-slim AS builder

WORKDIR /app

# Install only required build deps (minimal)
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc && \
    rm -rf /var/lib/apt/lists/*

# Copy only requirements first (for caching)
COPY requirements.txt .

# Install dependencies into a clean directory
RUN pip install --no-cache-dir --default-timeout=100 --retries=5 -r requirements.txt

# ---------- Stage 2: Runtime ----------
FROM python:3.10-slim

WORKDIR /app

# Set env early (important for Prometheus multiprocess)
ENV PYTHONUNBUFFERED=1
ENV prometheus_multiproc_dir=/tmp

# Create directory for Prometheus multiprocess
RUN mkdir -p /tmp && chmod 777 /tmp

# Copy installed dependencies
COPY --from=builder /install /usr/local

# Copy app code (after deps → caching benefit)
COPY . .

# Expose correct port (Gunicorn)
EXPOSE 8000

# Run app with optimized Gunicorn config
CMD ["gunicorn", "-w", "2", "--threads", "2", "-b", "0.0.0.0:8000", "app:app"]