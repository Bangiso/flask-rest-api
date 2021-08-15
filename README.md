# flask-rest-api
Basic flask api, probable not well implemented. To run the api:

`sh start.sh`

This will set up environment and start the app.

It requires mysql db connection, add your credentials in daos.StudentDAO file.

Create db resources

`CREATE database StudentDB;`

```
CREATE TABLE StudentDB.students(
	id int,
	name varchar(255),
	gpa double,
	PRIMARY KEY (id)
);
```
Add data
```
insert into StudentDB.students(id,name, gpa )  values (1, 'Aphiwe', 40),(2, 'Aphiwe2', 67),(3, 'Aphiwe2', 25);
```
# Endpoints
`GET   /api/students`

`GET   /api/students/{id}`

`POST   /api/students/add`

see commands.sh file






