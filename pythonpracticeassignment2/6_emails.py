users = [
    {"email": "alice@example.com", "verified": True},
    {"email": "bob@example.com", "verified": False},
    {"email": "charlie@example.com", "verified": True},
    {"email": "daisy@example.com", "verified": False}
	 ]
res=list(filter(lambda x:x['verified']==True,users))
res2=list(map(lambda x:x['email'],res))
print(res2)