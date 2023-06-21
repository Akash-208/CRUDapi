# CRUDapi
CRUD api using djnago Rest framework , Sqlite3

endpoints :

1) /users - will show all the users details available in the database
2) /new   - this endpoint allows you to create a new user by providing data in JSON format
3) /user/{id} - will show a particular user with given ID.
4) /delete/{id} - will remove a user with the given id
5) /update/{id} - will update the content of the query based on given id

   SAMPLE INPUT DATA
   ```
        {
        "name": "krish",
        "occupation": "designer",
        "phone": "123456"
    }
   ```
