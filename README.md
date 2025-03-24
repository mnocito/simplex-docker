# Simplex Playwright Docker

This Docker container runs a Python script using Simplex and Playwright.

## Setup

### Option 1: Using a .env file

1. Create a `.env` file in the project root with your Simplex API key:
   ```
   SIMPLEX_API_KEY=your_api_key_here
   ```

2. Build the Docker image:
   ```bash
   docker build -t simplex-playwright .
   ```

3. Run the container:
   ```bash
   docker run simplex-playwright
   ```

### Option 2: Passing API key directly

You can also pass the API key as an environment variable when running the container:

```bash
docker run -e SIMPLEX_API_KEY=your_api_key_here simplex-playwright
```

## Security Notes
- The `.env` file is already in the `.gitignore` file.

## Files

- `Dockerfile` - Contains the container configuration
- `main.py` - The Python script that runs on container startup
- `.env` - Contains your Simplex API key (create this file locally)