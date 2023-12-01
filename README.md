# Flask ChatBot Application

This is a simple Flask web application that integrates a ChatterBot with OpenAI's GPT-3.5-turbo model. Users can interact with the chatbot by typing questions, and the application stores user input in a MariaDB database.

## Getting Started

Follow these steps to set up the Flask ChatBot application on your local machine.

### Prerequisites

- Python 3.x installed
- Pip (Python package installer)
- MariaDB or MySQL server installed

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/your-repository.git
    cd your-repository
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Set up the MariaDB database:

    - Create a new database named `chatbot`.
    - Update the database connection details in `app.py` and `store_info` function.

4. Set up your OpenAI API key:

    - Replace `'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'` with your OpenAI API key in `app.py`.

5. Run the application:

    ```bash
    python app.py
    ```

6. Open your web browser and go to [http://localhost:5000](http://localhost:5000) to interact with the chatbot.

## Usage

- Type your questions in the input field and press "Send" to receive responses from the chatbot.
- The application stores user inputs in the MariaDB database.

## Additional Notes

- Customize the chat container styles in `login.html` to match your design preferences.
- Ensure your system has proper internet connectivity to interact with the OpenAI GPT-3.5-turbo model.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

