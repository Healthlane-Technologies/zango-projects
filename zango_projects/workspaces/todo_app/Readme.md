# Todo app
This is a todo app build with zango.

# App structure
```
todo_app               # app root where this readme file is located.
|
+-- migrations         # all the migrations of the todo_app are created here.
+-- todo
+-- manifest.json
+-- settings.json      # app version, modules, app_routes and package_routes are defined here
+-- Readme.md       
```

# Setting up the todo app

1. This guide assume that you have already performed all the steps give in the [zango_project guide](https://github.com/Healthlane-Technologies/zango-projects/tree/main/Readme.md).

2. After your main zango project is up and running go to `localhost:8000/platform` and login using the credentials that you created in the previous guide.

3. After you have logged in successfully, you'll see a dashboard like the one below:
<img width="1402" alt="app_panel_landing-af182a79b1f4735606e8941830997dc2" src="https://github.com/user-attachments/assets/b07e8008-8942-46b5-906c-0b05796af89b">


4. When you click on the launch new app, a panel will open from the right side of the screen. Enter the app name as `todo_app`(should be exact same), add any description and click launch app.

5. After the app creation process is complete, you'll notice a directory named `todo_app` at path `zango_projects/workspaces/` and there will be 2 more files `manifest.json` and `settings.json` inside `todo_app` direcrtory.

6. Delete `manifest.json` and `settings.json` files and copy all the files and folder present inside `zango_projects/workspaces/todo_app/` from the [zango-projects repository](https://github.com/Healthlane-Technologies/zango-projects).

7. Now run the following command to apply migrations of the todo app:
```
python manage.py ws_migrate todo_app
```

8. Congratulations! Your todo app has been successfully added to your zango project. In the next steps we will understand how to configure our todo app from our zango platform and create our first todo!
