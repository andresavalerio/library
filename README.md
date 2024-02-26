# Library

A CRUD made with :heart:, Python and MongoDB.

## Run the library application locally
1. Run a MongoDB instance locally
```sh
mkdir -p <db-path>
sudo mongod --dbpath <db-path>
```

2. Connect to your local instance
```sh
mongosh mongodb://localhost:27017/db
```

3. Test your connection
```sh
use local
db.startup_log.find({}, {"hostname": true})
```

4. Run the API
```sh
uvicorn main:app --reload
```

5. Insert data from a generic book
```sh
use library
db.books.insert(
    {
        "_id": ObjectId("65dbcc3a5c3d83b95afdca5b"),
        "title": "The Art of Computer Programming",
        "author": "Donald Knuth",
        "isbn": "0321751043",
        "year": "2011",
        "genre": "Technology"
    }
)
```

6. Test the get books endpoint
```sh
curl -X 'GET' \
  'http://127.0.0.1:8000/books/65dbcc3a5c3d83b95afdca5b' \
  -H 'accept: application/json'
```
