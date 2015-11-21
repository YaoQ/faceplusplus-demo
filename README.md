# faceplusplus-demo
Wrap Face++ Python API to implement face recognition.

If you want to use this wrapped python script, please follow the steps below:
## Steps
### 1. Register Face++ dev Account and Create a new App
For proper operation of the development environment, you need to have created an App and got the corresponding API Key and API Secret, follow these steps:

1. Click into the Dec center page, click on “My App”, you need to regist or login in first.

2. Click the icon ![create_new_app_2](http://www.faceplusplus.com/wp-content/uploads/2013/11/create_new_app_2.png)on the center of the screen to create a new App.
![1](http://www.faceplusplus.com/wp-content/uploads/2013/11/1.png)

3. Click SUBMIT, it turns into App information interface automatically.You will see API Key and API Secret.

![2](http://www.faceplusplus.com/wp-content/uploads/2013/11/21.png)
4. Copy the API Key and API Secret to your API-related documents such as apikey.cfg (many official downloaded SDK contains this file ) , or your own program.

 
**PAY ATTENTION**: If you choose Aliyun(China) server, please use the following configuration:
```python
SERVER = 'http://api.cn.faceplusplus.com/'

API_KEY = 'YOUR_API_KEY' API_SECRET = 'YOUR_API_SECRET'
If you choose Amazon(US) server,please use the following configuration:

SERVER = 'http://api.us.faceplusplus.com/'

API_KEY = 'YOUR_API_KEY'
API_SECRET = 'YOUR_API_SECRET'

Save apikey.cfg, application configuration success!
```

### 2. Modify your API key and API secret in apikey.cfg
```
vim apikey.cfg
```
### 3. Create a new group
``` 
$ python create_group.py <group_name>
```
### 4. Add recognized face to the group
```
$ python add_new_face.py <person_name> <imag_path> <group_name>
```
### 5. Recognize a new face
```
$ python recognition.py <group_name> <image_path>
```
### 6. Run together
As to this demo, you can manually run the following commands to test face++ API service.
``` bash 
$ python create_group.py test
$ python add_new_face.py tom images/tom.jpg test
$ python add_new_face.py obama images/obama.jpg test
$ python add_new_face.py yao images/yao.jpg test
$ python recognition.py test images/test.jpg
```