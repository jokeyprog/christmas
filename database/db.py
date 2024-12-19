import pymysql
import random

try:
    connect = pymysql.connect(host='127.0.0.1',
                            port=3306,
                            user='root',
                            password='',
                            database='christmas',
                            cursorclass=pymysql.cursors.DictCursor)
    cursor = connect.cursor()
except Exception as ex:
    print(ex)


async def registration(id_tg, username):
    cursor.execute(f"SELECT `username` FROM `users` WHERE `id_tg` = '{id_tg}'")
    result = cursor.fetchone()
    if result:
        if result['username'] != username:
            cursor.execute(f"UPDATE `users` SET `username`='{username}' WHERE `id_tg` = '{id_tg}'")
    if not result:
        cursor.execute(f"INSERT INTO `users`(`id_tg`, `username`, `send_greetings`) VALUES ('{id_tg}', '{username}', '0')")
        connect.commit()


async def get_users():
    cursor.execute(f"SELECT `id_tg`, `send_greetings` FROM `users`")
    result = cursor.fetchall()
    return result


async def send_greetings(id_tg):
    cursor.execute(f"UPDATE `users` SET `send_greetings`='1' WHERE `id_tg` = '{id_tg}'")
    connect.commit()


async def get_greeting():
    cursor.execute("SELECT COUNT(`id`) AS `count` FROM `greetings`")
    count = cursor.fetchone()
    cursor.execute(f"SELECT `text` FROM `greetings` WHERE `id` = '{random.randint(1, count["count"])}'")
    result = cursor.fetchone()
    return result


async def set_greetings_for_friend(id_tg, data):
    cursor.execute(f"SELECT `id_tg` FROM `users` WHERE `username` = '{data["username"]}'")
    result = cursor.fetchone()
    if result:
        cursor.execute(f"SELECT `id`, `username` FROM `users` WHERE `id_tg` = '{id_tg}'")
        res = cursor.fetchone()
        cursor.execute(f"SELECT `id_tg_recipient` FROM `greetings_for_friend` WHERE `id_user` = '{res['id']}' AND `id_tg_recipient` = '{result['id_tg']}'")
        re = cursor.fetchone()
        print(re)
        if re:
            return "Вы уже отправили поздравление этому другу"
        else:
            if res['username'] == None:
                print(res['username'])
                cursor.execute(f"INSERT INTO `greetings_for_friend`(`id_user`, `id_tg_recipient`, greeting) VALUES ('{res["id"]}', '{result['id_tg']}', '{data["text"]}\n\tОт одного из друзей')")
            else:
                print(res['username'])
                cursor.execute(f"INSERT INTO `greetings_for_friend`(`id_user`, `id_tg_recipient`, greeting) VALUES ('{res["id"]}', '{result['id_tg']}', '{data["text"]}\n\tОт {res['username']}')")
            connect.commit()
            return True
    else:
        return False


async def get_all_for_friends():
    cursor.execute(f"SELECT * FROM `greetings_for_friend`")
    result = cursor.fetchall()
    return result


async def get_friends(id_tg):
    lst = []
    cursor.execute(f"SELECT `id` FROM `users` WHERE `id_tg` = '{id_tg}'")
    res = cursor.fetchone()
    cursor.execute(f"SELECT `id_tg_recipient` FROM `greetings_for_friend` WHERE `id_user` = '{res['id']}'")
    results = cursor.fetchall()
    for result in results:
        cursor.execute(f"SELECT `username` FROM `users` WHERE `id_tg` = '{result['id_tg_recipient']}'")
        re = cursor.fetchone()
        if re['username'] not in lst and re['username'] != 'None' and re['username']:
            lst.append(re['username'])
    return lst


async def delete(id_tg, username):
    cursor.execute(f"SELECT `id_tg` FROM `users` WHERE `username` = '{username}'")
    id_recipient = cursor.fetchone()
    print(id_recipient)
    if id_recipient:
        cursor.execute(f"SELECT `id` FROM `users` WHERE `id_tg` = '{id_tg}'")
        id_user = cursor.fetchone()
        cursor.execute(f"SELECT `id` FROM `greetings_for_friend` WHERE `id_user` = '{id_user['id']}' AND `id_tg_recipient` = '{id_recipient['id_tg']}'")
        result = cursor.fetchone()
        print(result)
        if result:
            cursor.execute(f"DELETE FROM `greetings_for_friend` WHERE `id` = '{result['id']}'")
            connect.commit()
            return True
        else:
            return False
    else:
        return False
