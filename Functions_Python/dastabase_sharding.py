# This function decides which shard (or group chat) a user goes into
def get_shard(user_id, num_shards):
    # Using modulo to pick a shard; it's like picking a squad based on your ID number.
    return user_id % num_shards

# This function stores user data in the right shard
def store_user_data(user_id, data, shards):
    shard_id = get_shard(user_id, len(shards))
    shards[shard_id][user_id] = data
    #Store the data in the appropriate shard
    # This is like putting your stuff in the right group chat.
    # For example, if your user_id is 101 and you have 3 shards, you'd go to shard 2 (101 % 3 = 2).
    # If the user_id is 202, you'd go to shard 1 (202 % 3 = 1).
    # If the user_id is 303, you'd go to shard 0 (303 % 3 = 0).
    # This is a simple way to distribute users across different shards.
    print(f"User {user_id} data stored in shard {shard_id}")

# Create a few shards (like separate group chats)
shard1 = {}
shard2 = {}
shard3 = {}
shards = [shard1, shard2, shard3]

# Simulate storing some user data
store_user_data(101, {"name": "Alice", "score": 2000}, shards)
store_user_data(202, {"name": "Bob", "score": 1500}, shards)
store_user_data(303, {"name": "Charlie", "score": 3000}, shards)

# Check out what each shard holds
print("Shard 0:", shards[0])
print("Shard 1:", shards[1])
print("Shard 2:", shards[2])
