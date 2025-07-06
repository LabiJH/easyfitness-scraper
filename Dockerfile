FROM python:3.9.23-bookworm

ENV VIRTUAL_ENV="/opt/venv"
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install dependencies:
COPY requirements.txt .
RUN pip install -r requirements.txt

# Run the Application
COPY main.py .
COPY .env .
CMD ["python", "-u", "main.py"]