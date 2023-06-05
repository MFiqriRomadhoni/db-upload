# Upload Image to Google Cloud Storage

This project provides a simple Flask application for uploading image files to Google Cloud Storage.

## Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/your-username/upload-image-gcs.git

2. Install the required dependencies:
    pip install -r requirements.txt

3. Set up the Google Cloud Storage credentials:
    - Download the JSON credential file from the Google Cloud Console.
    - Set the GOOGLE_APPLICATION_CREDENTIALS environment variable to the path of the credential file.

# Usage
1. Run the application:
    python app.py

2. Make a POST request to the /upload-image endpoint with an image file attached.
3. The image file will be uploaded to the specified Google Cloud Storage bucket.

# Contributors

Contributions are welcome! If you would like to contribute to this project, please follow these steps:

1. Fork the repository.

2. Create a new branch for your feature or bug fix:
    git checkout -b feature/your-feature-name

3. Make your changes and commit them:
    git commit -m "Your commit message"

4. Push your changes to your forked repository:
    git push origin feature/your-feature-name

5. Open a pull request in this repository.

# License

This project is licensed under the MIT License.

# Contact

For any questions or inquiries, please contact your-email@example.com.
