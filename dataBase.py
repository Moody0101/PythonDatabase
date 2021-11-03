"""
Python basic data base to store passwords
"""
from json import loads, dumps
from os import system

class dataBase:
    def __init__(self, account: str=None, password: str = None, db: str = None) -> None:
        self.account = account
        self.password = password
        self.db = db
        if self.db is None:
            self.db = './dist/db.json'
    def POST(self):
        if len(open(self.db, 'r').read()) < 2:
            open(self.db, 'w+').write(
"""
{
    \"accounts\": [],
    \"passwords\": []
}
"""
        )
        if len(self.account) > 2:
            if len(self.password) > 2:
                data0 = loads(open(self.db, 'r').read()) #Loading the json object into python
                data0['accounts'].append(f"{self.account}")
                data0['passwords'].append(f"{self.password}")
                data1 = dumps(data0)
                open(self.db, 'w+').write(data1)
            else:
                raise Exception('Password is too small!!')
        else:
            raise Exception('account Name too small !!!')
    def GET(self) -> dict:
        return loads(open(self.db, 'r').read())
    def clearDb(self) -> None:
        if len(open(self.db, 'r').read()) > 2:
            open(self.db, 'w+').write(
"""
{
    \"accounts\": [],
    \"passwords\": []
}
""")
    def search(self, data: str):
        j = 0
        while j < len(self.GET()['accounts']):
            if self.GET()['accounts'] == data:
                return (
                    self.GET()['accounts'][j], 
                    self.GET()['passwords'][j], 
                )
            else:
                j += 1
        return 'data Not found'


def main(): # this function is the function that will manage the requestes
    menu = str(input("""
Which method that you want to use:
        1) GET
        2) POST
        3) CLEAR
        4) demonstrate in a live-server
        00) exit
    """))
    if menu == '1':
        getQuery = str(input("""
        1) Get all accound names
        2) Get all passwords
        3) both
        4) search
        00) return
        """))
        if getQuery == '1':
            print(dataBase().GET()['accounts'])
        elif getQuery == '2':
            print(dataBase().GET()['passwords'])
        elif getQuery == '3':
            print(dataBase().GET())
        elif getQuery == '4':
            accountName = input('account to Query : \t')
            print(dataBase().search(accountName))
        else:
            main()
    elif menu == '2':
        account = input("Account Name : \t")
        password = input("password  : \t")
        db = dataBase(account, password)
        db.POST()
        main()
    elif menu == '3':
        dataBase().clearDb()
        main()
    elif menu == '4':
        system("cd ./dist && live-server")
    else:
        exit()
if __name__ == '__main__':
    main()

