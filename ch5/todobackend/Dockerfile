# Development build
FROM alpine AS build
LABEL application=todobackend

# Install basic utilities
RUN apk add --no-cache bash git

# Install Python 3
RUN apk add --no-cache python3 && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 --no-cache-dir install --upgrade pip

# Install build dependencies
RUN apk add --no-cache gcc python3-dev libffi-dev musl-dev linux-headers mariadb-dev
RUN pip3 install wheel

# Copy requirements
COPY /src/requirements* /build/
WORKDIR /build

# Build and install requirements
RUN pip3 wheel -r requirements_test.txt --no-cache-dir --no-input
RUN pip3 install -r requirements_test.txt -f /build --no-index --no-cache-dir

# Copy source code
COPY /src /app
WORKDIR /app

# Test entrypoint
CMD ["python3", "manage.py", "test", "--noinput"]

# Production build
FROM alpine
LABEL application=todobackend

# Install dependencies
RUN apk add --no-cache bash mariadb-client-libs

# Install Python 3
RUN apk add --no-cache python3 && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 --no-cache-dir install --upgrade pip

COPY --from=build /build /build
COPY --from=build /app /app
WORKDIR /app

RUN pip3 install -r /build/requirements.txt -f /build --no-index --no-cache-dir
RUN rm -rf /build