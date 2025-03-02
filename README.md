# Order-Processing

 * `pip install -r .\requirements.txt` to install all the dependencies
 * Here are the list of api's
 * Insert order - small correction instead of list of items id's I taken only one item id.
   * `curl --location --request GET 'http://127.0.0.1:8000/orders/' \
--header 'Content-Type: application/json' \
--data '{
    "status": "Completed"
}'`


 * Metrics api
 * `curl --location 'http://127.0.0.1:8000/orders/metrics'`

 * Get All orders filtered by status api
 * `curl --location --request GET 'http://127.0.0.1:8000/orders/' \
--header 'Content-Type: application/json' \
--data '{
    "status": "Completed"
}'`
 * Please ref - https://www.w3schools.com/django/django_create_virtual_environment.php link to create virtual env and running django application
 * 