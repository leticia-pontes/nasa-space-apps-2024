# NASA Space Apps Challenge 2024

This project is an interactive data visualization application using Dash and Plotly, which presents an interactive map with data from cities and their populations.

## Technologies Used

- Python 3.9
- Dash
- Plotly
- Pandas
- Docker

## Prerequisites

Before running the project, make sure you have the following installed:

- [Docker](https://www.docker.com/get-started)
- [WSL](https://docs.microsoft.com/en-us/windows/wsl/install) (if using Windows)

## Settings

1. **Clone the repository**:
   ```bash
   git clone https://github.com/leticia-pontes/nasa-space-apps-2024
   cd nasa-space-apps-2024
   ```

2. **Build the Docker Image**:
   From the project root, run the command below to build the Docker image:
   ```bash
   docker build -t nasa-project-2024 .
   ```

3. **Run the Container**:
   After building the image, run the container with the command:
   ```bash
   docker run -d -p 5000:5000 --name nasa-project-container nasa-project-2024
   ```

## Access the Application

After running the container, you can access the interactive application in your browser at:
```
http://localhost:8050/
```

## Project Structure

```plaintext
.
├── assets/
├── src/
│   ├── utils/
│   │   ├── download_file.py
│   ├── app.py
│   ├── earth_engine.py
│   ├── geocode.py
│   └── image_processor.py
├── .gitignore
├── Dockerfile
├── README.md
├── entrypoint.sh
├── requirements.txt
```

## How It Works

1. **Entrypoint**: `entrypoint.sh` is the initialization script that downloads necessary data before starting the application.

2. **Dash Application**: `app.py` configures the Dash application, defines the layout and callbacks for user interaction.

3. **Dependencies**: Dependencies are installed in the container during the build process through the `Dockerfile`.
