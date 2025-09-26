FROM python:3.13-slim

RUN apt-get update \
 && apt-get install -y --no-install-recommends curl \
 && curl -LsSf https://astral.sh/uv/install.sh | sh \
 && rm -rf /var/lib/apt/lists/*

ENV PATH="/root/.local/bin:${PATH}"

ENV VIRTUAL_ENV=/opt/venv
ENV PATH="$VIRTUAL_ENV/bin:${PATH}"

WORKDIR /app

COPY pyproject.toml uv.lock* ./
RUN uv venv "$VIRTUAL_ENV" \
 && uv sync --no-dev --frozen

COPY . .

RUN useradd -m appuser && chown -R appuser:appuser /app /opt/venv
USER appuser

EXPOSE 8000
ENV PORT=8000

CMD ["python", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
