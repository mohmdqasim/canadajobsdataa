# Canada Jobs

This is a Streamlit application that you can set up and run locally. Follow the instructions below to get started.

## Prerequisites

- Python 3.x installed on your machine
- `pip` package manager (usually comes with Python)

## Setup Instructions

### 1. Clone the Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/mohmdqasim/canadajobsdataa.git
cd canadajobsdataa
```

### 2. Create a Virtual Environment

It's a good practice to use a virtual environment to manage dependencies. You can create one using `venv`:

```bash
python3 -m venv venv
```

This will create a directory named `venv` in your project folder.

### 3. Activate the Virtual Environment

Activate the virtual environment:

- **On Windows:**

    ```bash
    venv\Scripts\activate
    ```

- **On macOS and Linux:**

    ```bash
    source venv/bin/activate
    ```

You should see the virtual environment name (e.g., `(venv)`) appear in your terminal prompt, indicating that it's active.

### 4. Install Dependencies

Install the required dependencies using `pip`:

```bash
pip install -r requirements.txt
```

This will install all the packages listed in the `requirements.txt` file.

### 5. Run the Streamlit Application

You can now run the Streamlit application with the following command:

```bash
streamlit run main.py
```

### 6. Access the Application

Once the application is running, you can access it in your web browser at:

```
http://localhost:8501
```

## Additional Notes

- To deactivate the virtual environment, simply run:

    ```bash
    deactivate
    ```

- If you add any new dependencies, don't forget to update the `requirements.txt` file:

    ```bash
    pip freeze > requirements.txt
    ```

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
