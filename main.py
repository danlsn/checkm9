from dotenv import load_dotenv
from sqlalchemy.dialects.postgresql import psycopg2
import logging
import models

# Load Environment Variables
load_dotenv()

logging.basicConfig(filename='logs/main.log', encoding='utf-8', level=logging.DEBUG)
logging.getLogger('sqlalchemy.dialects.postgresql').setLevel(logging.DEBUG)


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
