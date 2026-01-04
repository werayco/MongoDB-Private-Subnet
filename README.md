# 1. Start container
docker compose up -d

# 2. Initialize replica set
```console
docker exec -it mongo-rs mongosh --eval "rs.initiate({_id: 'rs0', members: [{_id: 0, host: 'mongo-rs:27017'}]})"
```

# 3. Verify the replica set is running
```console
docker exec -it mongo-rs mongosh --eval "rs.status()"
```

# 4.  Add this as a environmental variable for the rencie application 
```console
MONGO = mongodb://mongo-rs:27017/?directConnection=true
```