# Project Setup and Execution Guide

This guide provides step-by-step instructions for setting up and running the project, which involves starting a JSON API server, ensuring Redis is running, and executing a Jupyter notebook.

## Prerequisites

Before you start, ensure you have the following installed:

- Node.js and npm: These are required to set up and run the JSON server.
- Redis: You'll need Redis to cache and retrieve data.

## Step 1: Verify Node.js and npm Installation

First, check if Node.js and npm are installed by running the following commands in your terminal:

```bash
node --version
npm --version
```

If these commands don't return version numbers, you need to install Node.js and npm. Visit [Node.js official website](https://nodejs.org/) for installation instructions.

## Step 2: Set Up the JSON Server

1. Install `json-server` globally using npm:

   ```bash
   npm install -g json-server
   ```

2. Start the JSON server with your data file (e.g., `students.json`):

   ```bash
   json-server --watch students.json
   ```

   This command will start the JSON server, watching your `students.json` file for changes and serving the data at `http://localhost:3000`.

## Step 3: Install and Run Redis

Ensure Redis is installed and running on your machine:

- For installation instructions, visit the [Redis official website](https://redis.io/download).

- After installation, you can start the Redis server by running:

  ```bash
  redis-server
  ```

  This command will start the Redis server, and you should see a message indicating that the server is running.

## Step 4: Running the Jupyter Notebook

Ensure you have Jupyter installed. If not, you can install it via pip:

```bash
pip install notebook
```

After installing Jupyter, navigate to the directory containing your `assignment.ipynb` file and run:

```bash
jupyter notebook
```

This command will start the Jupyter notebook server and open the interface in your web browser.

- Open `assignment.ipynb` within the Jupyter interface.

- Run the cells sequentially to execute the project code.

## Additional Information

- Make sure all dependencies and libraries used in the `assignment.ipynb` notebook are installed using pip (e.g., `requests`, `redis`, `pandas`).

- Ensure the configurations in your notebook, especially those related to Redis and the JSON server, are correct and correspond to your setup.

By following these steps, you should be able to set up and run the project successfully.
