from slidin import db
def fetch_userId(user_names):
	userIds = []
	for user_name in user_names:
		user = User.query.filterby(username=user_name).first()
		userIds.append(user.id)
	return userIds



