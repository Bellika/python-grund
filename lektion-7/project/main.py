from models import User, load_users, save_user, UserDB, load_users_db, save_user_db
from api import fetch_iss_data, save_iss_data, iss_location

if __name__ == '__main__':
    new_user = User(username='Markus', password='password')
    save_user(new_user)
    print(load_users())

    iss_data = fetch_iss_data()
    save_iss_data(iss_data)
    print('ISS-data saved')

    iss_location()

    new_user_db = UserDB(username='Markus', password='sommar')
    save_user_db(new_user_db)

