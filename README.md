# Evergreen Messages Back-end

For run this project:

1. Ensure you have python 3.9+ and pip
2. Create a virtual environment for Python
~~~
pip install virtualenv
virtualenv -p pyhton env
~~~
3. Activate your virtual environment

    For Windows
    ~~~
    source env/Scripts/activate
    ~~~

    For Linux

    ~~~
    source env/bin/activate
    ~~~

4. Install the requirements
~~~
pip install -r requirements.txt
~~~

5. Run the project
~~~
uvicorn app:app --reload --port {your_port}
~~~
By default it will be launched in port 8000