# congee_mockup
Congee return your http request message

For the first time should run the following command to build the image and container:

   ```bash
   docker-compose up --build
   ```
Then
   ```bash
   docker-compose down
   ```
And up again
   ```bash
   docker-compose up -d
   ```

   The application will be available on `http://localhost:5000`. You can test it by sending GET, POST, or other HTTP requests, and it will echo back the received data.

