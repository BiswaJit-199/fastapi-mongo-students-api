# FastAPI MongoDB Students API
This project demonstrates a simple CRUD(Create, Read, Update, Delete) Api for managing a students database using FastAPI & MongoDB
## Project Stucture

>app/ <br />
>>__init__.py <br />
>>crud.py <br />
>>database.py <br />
>>main.py <br />
>>models.py <br />
>>schemas.py <br />
>>routers/ <br />
>>>__init__.py <br />
>>>students.py <br />

## Setup Instructions
### Prerequisites
- Python 3.7+
- MongoDB

### Installation
1. **Clone the repository:**
   ```sh
   https://github.com/BiswaJit-199/fastapi-mongo-students-api.git
   cd  fastapi-mongo-students-api
   ```
2. **Intall the dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
3. **Set up MongoDB:**
   Ensure MongoDB is running on your Machine. check `/app/database.py` for configuration.
4. **Run the FastAPI applicatio:**
   ```sh
   uvicorn app.main:app --reload
   ```
5. **Open the Browser:**
   Navigate to `http://127.0.0.1:8000/docs` to see the Swagger UI and test the API endpoints.
## API Endpoints
- `POST /student/create`: Create a new student
- `GET /students`: Retrive all students
- `GET /student/{id}`: Retrive a student by ID
- `PUT /student/{id}`: Update a student by ID
- `DELETE /student/{id}`: Delete a student by ID

## License
This project is licensed under the MIT License.
____
> [!IMPORTANT]
> `MongoDB_URL="mongodb://127.0.0.1:27017"` <br />
> `DATABASE_NAME="fastapi_database"` <br />
> `COLLECTION_NAME="students"` <br />

> [!NOTE]
> Check `/output_images/` for output.
