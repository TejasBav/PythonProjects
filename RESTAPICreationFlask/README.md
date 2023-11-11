#Creating REST API using Flask

Creating virtual enviroment
python -m venv .venv

Installing flask
pip install flask

Installing ORM flask-sqlcalchemy
pip install flask-sqlalchemy

Creating requirements.txt
pip freeze > requirements.txt

Setting below Flask environment variables in windows and run flask in powershell only:
![image](https://github.com/TejasBav/PythonProjects/assets/148721897/1f9dba9f-4c15-4e63-95ed-b564c6e96b89)
if you want to run flask in debug mode to get updated flask while you are developing, use below command:
flask run --debug

if you kill terminal and reopen again, you will have to run above command everytime

Creating db and app
![image](https://github.com/TejasBav/PythonProjects/assets/148721897/d7b1d799-7995-4dd9-8d28-3f39167c7974)


Open interactive python in cmdshell
python

Importing db from app-
from app import db

Creating table-
db.create_all()

Everytime you have to use something from your app. import it
from app import Drink

Create drink object-
drink = Drink(name = 'Grape Soda', description='Tastes like Grape')

Showing drink-
![image](https://github.com/TejasBav/PythonProjects/assets/148721897/b5423459-90fd-46f8-a9ea-a735ea2033c6)

Adding it to table-
![image](https://github.com/TejasBav/PythonProjects/assets/148721897/92379a74-de77-4887-adab-752f70f6319d)

Showing all drinks-
![image](https://github.com/TejasBav/PythonProjects/assets/148721897/96701dee-d8ae-48a4-9d9e-4e9ae8840665)

Adding one more drink
![image](https://github.com/TejasBav/PythonProjects/assets/148721897/81f0e86c-d401-4404-981a-2a110c21d8a6)

Adding get_drinks() and get_drink() methods-
![image](https://github.com/TejasBav/PythonProjects/assets/148721897/bcbf5200-43e7-4294-99ad-08a5cf8235b5)
![image](https://github.com/TejasBav/PythonProjects/assets/148721897/b3c9b215-af31-4336-87ab-b1e742c3714a)
![image](https://github.com/TejasBav/PythonProjects/assets/148721897/0fc307bd-eeb6-4c80-957f-1b405b78c2e8)

Adding add_drink():
![image](https://github.com/TejasBav/PythonProjects/assets/148721897/423a5d39-754e-48aa-9009-cec9e8bb0d05)

![image](https://github.com/TejasBav/PythonProjects/assets/148721897/aa48fb47-595a-465e-8a60-cd63b0692ca0)
![image](https://github.com/TejasBav/PythonProjects/assets/148721897/29a63723-faeb-4ac5-8cd8-73ed7695efaa)
![image](https://github.com/TejasBav/PythonProjects/assets/148721897/4dc7c3d3-35ff-4ac6-b5ee-2b238e1b5f25)

adding delete_drink()
![image](https://github.com/TejasBav/PythonProjects/assets/148721897/3062ea8c-2075-42af-bc37-25aeb26a4d4e)
![image](https://github.com/TejasBav/PythonProjects/assets/148721897/830dce11-eb88-4d15-b7a6-04f7e3b62348)

Deleting drink 3
![image](https://github.com/TejasBav/PythonProjects/assets/148721897/3781c020-94a8-4ee3-a425-55dd23dac80e)

Deleting drink 3 again
![image](https://github.com/TejasBav/PythonProjects/assets/148721897/0daec0fd-6e6e-4305-b0c7-9cc594f78c1d)

Adding update_drink()
![image](https://github.com/TejasBav/PythonProjects/assets/148721897/0d032c71-8f18-4923-ac7c-f94795386ef6)
![image](https://github.com/TejasBav/PythonProjects/assets/148721897/c5a53b5d-aae8-4111-b7b3-1bbc24af32b0)
![image](https://github.com/TejasBav/PythonProjects/assets/148721897/ee85a4a4-610e-4ef6-baa8-6698c0fabb52)











